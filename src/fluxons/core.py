from dataclasses import dataclass, field


class Graph(list):
    '''
    A Graph is a list of Nodes.
      Nodes should be created already belonging to a Graph.
        They will be created on-the-fly when first accessed,
        i.e., `g.earth` will create (and return!) a Node
        called `earth` inside `g` (using the internal `__getattr__` trick).
    '''
    def __getattr__(self, a):
        '''
        This method is called when the graph has no member called `a`.
        This is a trigger to create a new node called `a`.
        Future calls to `g.a` will return the once created node,
        as they are unique by name.
        '''
        new_node = Node(name=a, owner=self)
        setattr(self, a, new_node)  # to avoid duplicity
        super().append(new_node)  # to ease grouping
        return new_node


@dataclass
class Node(list):
    '''
    A Node is a list of Edges.
      Edges should be created already belonging to a node.
        They will be created on-the-fly when first accessed,
        i.e., `g.earth.orbits` will create (and return!) an Edge
        called `orbits` inside `g.earth` (using the `__getattr__` trick).
    '''
    name: str
    owner: Graph
    # meta data:
    md: dict = field(default_factory=dict)

    def __getattr__(self, a):
        '''
        This method is called when the node has no member called `a`.
        This is interpreted as a trigger to create a new edge called `a`
        originating from the node.
        IMPORTANT: contrary to the case of the Graph, this method does not
                   creates a member called `a`, so future calls of `n.a`
                   will also trigger this method.
                   Edges are not unique by its name.
        '''
        new_edge = Edge(name=a, owner=self.owner)
        self.append(new_edge)
        return new_edge

    def __call__(self, **kwargs):
        '''
        This is called when the node is used as a funtion, with the
        intention of updating its metadata with kwargs, even when it is
        being created, because the `__getattr__` part is solved first.
        Example:
          `g.earth(radius=6380e3)` will create a node called `earth` and
          a key/value pair `g.earth.md['radius'] = 6380e3`.
        '''
        self.md.update(kwargs)
        # Notice that returns itself so it does not interferes with
        # the chaining of nodes and edges.
        return self


@dataclass
class Edge:
    name: str
    owner: Graph
    dest: Node = None
    # meta data:
    md: dict = field(default_factory=dict)

    def __getattr__(self, a):
        '''
        This method is called when the edge has no member called `a`,
        which will be almost always, because, as in the node case,
        no member `a` is created.
        The idea is being able to chain an intercalation of nodes and edges
        that may not exist until that point, i.e.,
        `g.node1.edge1.node2.edge2.node3`.
        Notice how the edge delegates to the graph the access or creation
        of the destination node.
        '''
        self.dest = getattr(self.owner, a)
        # TODO: why dont `setattr(self, a)`?
        return self.dest

    def __call__(self, **kwargs):
        '''
        This is called when the edge is used as a funtion, with the
        intention of updating its metadata with kwargs, even when it is
        being created, because the `__getattr__` part is solved first.
        Example:
          `g.earth.orbits(eccentricity=0.0167).sun` will create an edge
          called `orbits` and a key/value pair
          `g.earth.orbits.md['eccentricity'] = 0.0167`.
        '''
        self.md.update(kwargs)
        # Notice that returns itself so it does not interferes with
        # the chaining of nodes and edges.
        return self
