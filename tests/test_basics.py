#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase
from fluxon import Graph, Node, Edge


class Instantiation(TestCase):

    def _test_instance(self, class_, *args):
        try:
            class_(*args)
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


class Consistency(TestCase):

    def test_node_owner(self):
        g = Graph()
        g.fran
        self.assertIs(g.fran.owner, g)

    def test_edge_owner(self):
        g = Graph()
        g.fran.writes.code
        edge = g.fran[0]
        self.assertIs(edge.owner, g)

    def test_node_chained_owner(self):
        g = Graph()
        g.fran.writes.code
        self.assertIs(g.code.owner, g)

    def test_node_uniqueness(self):
        g = Graph()
        g.fran
        g.fran
        self.assertEqual(sum(map(lambda n: n.name == 'fran', g)), 1)

    def test_edge_non_uniqueness(self):
        g = Graph()
        g.fran.writes.code
        g.fran.writes.tests
        self.assertEqual(sum(map(lambda e: e.name == 'writes', g.fran)), 2)

    def test_edge_dest(self):
        g = Graph()
        g.fran.writes.code
        edge = g.fran[0]
        self.assertIs(edge.dest, g.code)


class Metadata(TestCase):

    def test_node_md(self):
        g = Graph()
        g.fran(type='human', tests_code=True)
        self.assertDictEqual({'type': 'human', 'tests_code': True}, g.fran.md)

    def test_edge_md(self):
        g = Graph()
        g.fran.writes(frequency='always', quality=10).tests
        edge = g.fran[0]
        self.assertDictEqual({'frequency': 'always', 'quality': 10}, edge.md)
