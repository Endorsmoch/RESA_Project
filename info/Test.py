import unittest
from GraphApp.NodeTest import *
from GraphApp.GraphTest import *

TEST_SUITES = [
  unittest.TestLoader().loadTestsFromTestCase(NodeTest),
  unittest.TestLoader().loadTestsFromTestCase(GraphTest)
]

runner = unittest.TextTestRunner(verbosity=2)
for test_suite in TEST_SUITES:
  runner.run(test_suite)
