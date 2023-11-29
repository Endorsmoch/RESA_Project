import unittest
from GraphApp.Node import *

class NodeTest(unittest.TestCase):
  def setUp(self):
    self.node1 = Node(1)
    self.node2 = Node(2)

  def test_add_neighbour(self):
    self.node1.add_neighbour(self.node2)
    self.assertTrue(self.node2 in self.node1.get_neighbours())

  def test_dont_add_neighbour(self):
    self.assertTrue(self.node2 not in self.node1.get_neighbours())

  def test_to_string(self):
    self.assertEqual(str(self.node1), '1')

  def test_invalid_to_string(self):
    self.assertNotEqual(str(self.node1), '2')
