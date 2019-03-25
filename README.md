# fluxons

Python library for easy graph creation.

# Short description

Powered by python's magic `__getattr__` and `__call__`,
allows its users to express relations like:

```
g.fran.writes.fluxons
```
that will create *on-the-fly* the nodes `fran` and `fluxons`
as members of `g` and the edge `writes` as member of `fran`
pointing to `fluxons`.

Chain relations are possible:
```
g.fran.writes.fluxons.in.python
```
with the expected results.

Nodes and Edges can be called as functions to store metadata
inside them:
```
g.fran(type='human').writes(lang='python').fluxons(type='code')
```
Useful for `graphviz` later use.

**REMEMBER:** nodes are unique; edges are not.

# How to combine with `graphviz`

```
from fluxons import Graph
g = Graph()
g.fran.writes.fluxons

from graphviz import Digraph
dg = Digraph()
[dg.node(n.name, **n.md) for n in g]
[dg.edge(n.name, e.dest.name, **e.md) for n in g for e in n]
dg.render('/tmp/fluxons_graph')
```

# Caveats

* As edges are not unique (by design), they should not be referenced
as an attribute of its origin node; this will create a new edge with
the same name.
* Creating an edge *on-the-fly* without creating its destination is pointless
as its reference will be lost.
* Node and Edges names must be valid python variable names.
* Node and Edges names cannot be the same as List members.
* Node and Edges names cannot be `name`, `owner`, `md` or `dest`.

# Usage

## Installation in a virtualenv

* `python -m venv venv`
* `. venv/bin/activate`
* `pip install -U pip`
* `pip install .`

## Run tests

* `python -m unittest discover tests`
