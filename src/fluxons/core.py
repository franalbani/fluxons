from dataclasses import dataclass, field

class Graph(list):
    def __getattr__(self, a):
        new_node = Node(name=a, owner=self)
        setattr(self, a, new_node)  # to avoid duplicity
        super().append(new_node)  # to ease grouping
        return new_node


@dataclass
class Node(list):
    name: str
    owner: Graph
    md: dict = field(default_factory=dict)

    def __getattr__(self, a):
        new_edge = Edge(name=a, owner=self.owner)
        self.append(new_edge)
        return new_edge

    def __call__(self, **kwargs):
        self.md.update(kwargs)
        return self


@dataclass
class Edge:
    name: str
    owner: Node
    dest: Node = None
    md: dict = field(default_factory=dict)

    def __getattr__(self, a):
        self.dest = getattr(self.owner, a)
        return self.dest

    def __call__(self, **kwargs):
        self.md.update(kwargs)
        return self
