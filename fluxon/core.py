#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from attr import attrs, attrib, Factory


class Graph(list):

    def __getattr__(self, a):
        new_node = Node(name=a, owner=self)
        setattr(self, a, new_node)  # to avoid duplicity
        super().append(new_node)  # to ease grouping
        return new_node


@attrs
class Node(list):
    name = attrib()
    owner = attrib(repr=False)
    md = attrib(default=Factory(dict))

    def __getattr__(self, a):
        new_edge = Edge(name=a, owner=self.owner)
        self.append(new_edge)
        return new_edge

    def __call__(self, **kwargs):
        self.md.update(kwargs)
        return self


@attrs
class Edge:
    name = attrib()
    owner = attrib(repr=False)
    dest = attrib(default=None)
    md = attrib(default=Factory(dict))

    def __getattr__(self, a):
        self.dest = getattr(self.owner, a)
        return self.dest

    def __call__(self, **kwargs):
        self.md.update(kwargs)
        return self
