import unittest
from DeviceApp.DeviceManager import *

class DeviceManagerTest(unittest.TestCase):
  def setUp(self):
    self.device_manager = DeviceManager()

  def test_load_config_nodes_quantity(self):
    config = {"id": "mac-add-1", "neighbours": [], "ips": ["192.168.10.1", "172.16.1.1"]}
    self.device_manager.load_configuration(config)
    
    self.assertEqual(len(self.device_manager.get_nodes()), 1)

  def test_load_config_node_appears(self):
    node_id = "mac-add-1"
    config = {"id": node_id, "neighbours": [], "ips": ["192.168.10.1", "172.16.1.1"]}
    self.device_manager.load_configuration(config)

    self.assertTrue(self.device_manager.get_node(node_id) is not None)

  def test_load_config_node_data(self):
    node_id = "mac-add-1"
    node_neighbours = []
    node_ips = ["192.168.10.1", "172.16.1.1"]
    config = {"id": node_id, "neighbours": node_neighbours, "ips": node_ips}
    self.device_manager.load_configuration(config)
    device = self.device_manager.get_node(node_id)

    self.assertEqual(device.get_id(), node_id)
    self.assertEqual(len(device.get_neighbours()), len(node_neighbours))
    self.assertEqual(len(device.get_ips()), len(node_ips))
    self.assertTrue(device.get_visited())

  def test_next_device_without_neighbours(self):
    config = {"id": "mac-add-1", "neighbours": [], "ips": ["192.168.10.1", "172.16.1.1"]}
    self.device_manager.load_configuration(config)
    
    self.assertTrue(self.device_manager.get_next_device() is None)

  def test_load_complex_nodes_quantity(self):
    config = {"id": "mac-add-1", "neighbours": [{"id": "mac-add-2", "ips": ["192.168.10.6"]}], "ips": ["192.168.10.1", "172.16.1.1"]}
    self.device_manager.load_configuration(config)
    
    self.assertEqual(len(self.device_manager.get_nodes()), 2)

  def test_load_complex_config_node_appears(self):
    node_id = "mac-add-2"
    config = {"id": "mac-add-1", "neighbours": [{"id": node_id, "ips": ["192.168.10.6"]}], "ips": ["192.168.10.1", "172.16.1.1"]}
    self.device_manager.load_configuration(config)

    self.assertTrue(self.device_manager.get_node(node_id) is not None)

  def test_load_complex_config_node_data(self):
    node_id = "mac-add-2"
    node_ips = ["192.168.10.6"]
    config = {"id": "mac-add-1", "neighbours": [{"id": node_id, "ips": ["192.168.10.6"]}], "ips": ["192.168.10.1", "172.16.1.1"]}
    self.device_manager.load_configuration(config)
    device = self.device_manager.get_node(node_id)

    self.assertEqual(device.get_id(), node_id)
    self.assertEqual(len(device.get_ips()), len(node_ips))
    self.assertFalse(device.get_visited())

  def test_next_device_with_neighbours(self):
    config = {"id": "mac-add-1", "neighbours": [{"id": "mac-add-2", "ips": ["192.168.10.6"]}], "ips": ["192.168.10.1", "172.16.1.1"]}
    self.device_manager.load_configuration(config)
    
    self.assertTrue(self.device_manager.get_next_device() is not None)

  def test_next_device_node_is_expected(self):
    node_id = "mac-add-2"
    config = {"id": "mac-add-1", "neighbours": [{"id": node_id, "ips": ["192.168.10.6"]}], "ips": ["192.168.10.1", "172.16.1.1"]}
    self.device_manager.load_configuration(config)

    self.assertEqual(self.device_manager.get_next_device().get_id(), node_id)

  def test_load_more_complex_nodes_quantity(self):
    config = {"id": "mac-add-1", "neighbours": [{"id": "mac-add-2", "ips": ["192.168.10.6"]}, {"id": "mac-add-3", "ips": ["192.168.10.10"]}], "ips": ["192.168.10.1", "172.16.1.1"]}
    self.device_manager.load_configuration(config)
    
    self.assertEqual(len(self.device_manager.get_nodes()), 3)

  def test_load_neighbour_config_node_data(self):
    node1_id = "mac-add-1"
    node2_id = "mac-add-2"
    config1 = {"id": node1_id, "neighbours": [{"id": node2_id, "ips": ["192.168.10.6"]}], "ips": ["192.168.10.1", "172.16.1.1"]}
    config2 = {"id": node2_id, "neighbours": [{"id": node1_id, "ips": ["192.168.10.1", "172.16.1.1"]}], "ips": ["192.168.10.6"]}
    self.device_manager.load_configuration(config1)
    self.device_manager.get_next_device()
    self.device_manager.load_configuration(config2)
    
    self.assertEqual(len(self.device_manager.get_nodes()), 2)
    self.assertTrue(self.device_manager.get_node(node1_id) is not None)
    self.assertTrue(self.device_manager.get_node(node1_id).get_visited())
    self.assertTrue(self.device_manager.get_node(node2_id) is not None)
    self.assertTrue(self.device_manager.get_node(node2_id).get_visited())
    self.assertTrue(self.device_manager.get_next_device() is None)
