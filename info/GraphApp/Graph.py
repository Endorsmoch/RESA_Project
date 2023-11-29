from GraphApp.Node import *

class Graph:
  def __init__(self) -> None:
    self._nodes = set()

  def get_nodes(self) -> set:
    return self._nodes

  def get_node(self, id) -> Node:
    for node in self.get_nodes():
      if node.get_id() == id:
        return node
    return None

  def add_node(self, node) -> None:
    if isinstance(node, Node) and node not in self.get_nodes():
      self.get_nodes().add(node)

  def add_relationship(self, node1, node2) -> None:
    if self.__are_nodes(node1, node2) and self.__have_been_added(node1, node2) and self.__are_not_the_same(node1, node2):
      node1.add_neighbour(node2)
      node2.add_neighbour(node1)

  def __are_nodes(self, node1, node2) -> bool:
    return isinstance(node1, Node) and isinstance(node2, Node)

  def __have_been_added(self, node1, node2) -> bool:
    return node1 in self.get_nodes() and node2 in self.get_nodes()
  
  def __are_not_the_same(self, node1, node2) -> bool:
    return node1.get_id() != node2.get_id()

