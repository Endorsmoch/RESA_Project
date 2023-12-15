from GraphApp.Node import *

class Device(Node):
  def __init__(self, id, ips, visited) -> None:
    super().__init__(id)
    self._ips = ips
    self._visited = visited

  def get_ips(self):
    return self._ips
  
  def set_ips(self, ips):
    self._ips = ips
  
  def get_visited(self):
    return self._visited
  
  def set_visited(self, visited):
    self._visited = visited
