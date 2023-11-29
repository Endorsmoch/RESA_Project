from GraphApp.Graph import *
from DeviceApp.Device import *

class DeviceManager(Graph):
  def load_configuration(self, config: dict) -> None:
    main_device = self.get_node(config["id"])

    if main_device is not None:
      main_device.set_visited(True)
    else:
      main_device = Device(config["id"], set(config["ips"]), True)
      self.add_node(main_device)

    for neighbour in config["neighbours"]:
      device = self.get_node(neighbour["id"])

      if device is None:
        device = Device(neighbour["id"], set(neighbour["ips"]), False)
        self.add_node(device)
      
      self.add_relationship(main_device, device)

  def get_next_device(self) -> Device:
    for device in self.get_nodes():
      if not device.get_visited():
        return device
    return None
