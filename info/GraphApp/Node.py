class Node:
  def __init__(self, id) -> None:
    self._id = id
    self._neighbours = set()

  def get_id(self) -> any:
    return self._id
  
  def get_neighbours(self) -> set:
    return self._neighbours

  def add_neighbour(self, node) -> None:
    self.get_neighbours().add(node)
  
  def __str__(self) -> str:
    return f'{self.get_id()}'
