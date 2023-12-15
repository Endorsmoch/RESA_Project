import unittest
from GraphApp.Graph import *
from GraphApp.Node import *

class GraphTest(unittest.TestCase):
  def setUp(self):
    self.graph = Graph()

    self.node1_id = "id-1"
    self.node1 = Node(self.node1_id)

    self.node2_id = "id-2"
    self.node2 = Node(self.node2_id)

  def test_add_node(self):
    self.graph.add_node(self.node1)
    self.assertTrue(self.node1 in self.graph.get_nodes())

  def test_add_many_nodes(self):
    self.graph.add_node(self.node1)
    self.graph.add_node(self.node2)
    self.assertTrue(self.node1 in self.graph.get_nodes() and self.node2 in self.graph.get_nodes())

  def test_add_the_same_node_twice(self):
    self.graph.add_node(self.node1)
    self.graph.add_node(self.node1)
    self.assertEqual(len(self.graph.get_nodes()), 1)

  def test_adding_not_a_node(self):
    self.graph.add_node(1)
    self.graph.add_node('')
    self.graph.add_node({})
    self.graph.add_node([])
    self.assertEqual(len(self.graph.get_nodes()), 0)

  def test_get_node(self):
    self.graph.add_node(self.node1)
    self.assertEqual(self.graph.get_node(self.node1_id), self.node1)

  def test_get_non_existing_node(self):
    self.assertTrue(self.graph.get_node(self.node2_id) is None)

  def test_add_relationship(self):
    self.graph.add_node(self.node1)
    self.graph.add_node(self.node2)
    self.graph.add_relationship(self.node1, self.node2)
    IS_N1_NEIGHBOUR = self.node2 in self.node1.get_neighbours()
    IS_N2_NEIGHBOUR = self.node1 in self.node2.get_neighbours()
    self.assertTrue(IS_N1_NEIGHBOUR and IS_N2_NEIGHBOUR)

  def test_relate_nodes_twice(self):
    self.graph.add_node(self.node1)
    self.graph.add_node(self.node2)
    self.graph.add_relationship(self.node1, self.node2)
    self.graph.add_relationship(self.node1, self.node2)
    N1_NEIGHBOUR_LEN = len(self.node1.get_neighbours())
    N2_NEIGHBOUR_LEN = len(self.node2.get_neighbours())
    self.assertTrue(N1_NEIGHBOUR_LEN == 1 and N2_NEIGHBOUR_LEN == 1)

  def test_relate_same_node(self):
    self.graph.add_node(self.node1)
    self.graph.add_relationship(self.node1, self.node1)
    self.assertEqual(len(self.node1.get_neighbours()), 0)

  def test_relate_something_aside_a_node(self):
    self.graph.add_relationship('', {})
    self.graph.add_relationship(0, [])
    self.assertEqual(len(self.graph.get_nodes()), 0)

  def test_relate_non_existing_nodes(self):
    self.graph.add_relationship(self.node1, self.node2)
    N1_NEIGHBOUR_LEN = len(self.node1.get_neighbours())
    N2_NEIGHBOUR_LEN = len(self.node2.get_neighbours())
    self.assertTrue(N1_NEIGHBOUR_LEN == 0 and N2_NEIGHBOUR_LEN == 0)
