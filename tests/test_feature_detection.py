import unittest
from src.vslam.feature_detection import FeatureDetector

class TestFeatureDetection(unittest.TestCase):

    def setUp(self):
        self.detector = FeatureDetector()

    def test_detect_features(self):
        # Test with a sample image
        sample_image = "path/to/sample/image.jpg"  # Replace with actual image path
        features = self.detector.detect_features(sample_image)
        
        # Check if features are detected
        self.assertIsNotNone(features)
        self.assertGreater(len(features), 0, "No features detected")

    def test_detect_features_invalid_input(self):
        # Test with an invalid image path
        with self.assertRaises(FileNotFoundError):
            self.detector.detect_features("invalid/path/to/image.jpg")

if __name__ == '__main__':
    unittest.main()