from fluxons import Graph

g = Graph()

g.moon.orbits.earth.orbits.sun(shape='circle')
g.mercury.orbits.sun
g.mars.orbits.sun
g.phobos.orbits.mars(color='red', fontcolor='red')
g.deimos.orbits.mars
g.curiosity.landed_on.mars

g.earth(color='green', fontcolor='green')


from graphviz import Digraph as DG

dg = DG()

[dg.node(n.name, **n.md) for n in g]
[dg.edge(n.name, e.dest.name, label=e.name, **e.md) for n in g for e in n]
# label=e.name can be omitted

# Notice how the node metadata controls graphviz attributes.

dg.graph_attr = {
        'color': '#FFB000',
        'bgcolor': '#00000000',
        }
dg.node_attr={
        'color': '#FFB000',
        'fontcolor': '#FFB000',
        'fontname': 'Terminess Nerd Font Mono',
        'shape': 'rect'
        }
dg.edge_attr = {
        'color': 'cyan',
        'fontcolor': 'cyan',
        'fontname': 'Terminess Nerd Font Mono',
        }
dg.render('solar_system',
          engine='circo',
          format='svg',
          cleanup=True)
