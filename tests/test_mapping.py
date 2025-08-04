import unittest
from src.vslam.mapping import Mapper

class TestMapper(unittest.TestCase):

    def setUp(self):
        self.mapper = Mapper()

    def test_create_map(self):
        features = [(1, 2), (3, 4), (5, 6)]
        poses = [(0, 0, 0), (1, 1, 0), (2, 2, 0)]
        expected_map = {
            'landmarks': features,
            'poses': poses
        }
        result = self.mapper.create_map(features, poses)
        self.assertEqual(result, expected_map)

    def test_create_map_empty(self):
        features = []
        poses = []
        expected_map = {
            'landmarks': [],
            'poses': []
        }
        result = self.mapper.create_map(features, poses)
        self.assertEqual(result, expected_map)

if __name__ == '__main__':
    unittest.main()