#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from fluxon import Graph, Node, Edge


class Instantiation(TestCase):

    def _test_instance(self, c, *args):
        try:
            c(*args)
        except Exception as e:
            self.fail('%r was raised' % e)


    def test_graph(self):
        self._test_instance(Graph)


    def test_node(self):
        self._test_instance(Node, 'some_name', 'some_owner')


    def test_edge(self):
        self._test_instance(Edge, 'some_name', 'some_owner')


    def test_node_creation_on_first_ref(self):
        g = Graph()
        g.fran
        self.assertIn('fran', map(lambda n: n.name, g))


    def test_edge_creation_on_first_ref(self):
        g = Graph()
        g.fran.writes.tests
        self.assertIn('writes', map(lambda e: e.name, g.fran))
