import cv2
class FeatureDetector:
    def __init__(self, n_features=500):
        self.n_features = n_features
        self.orb = cv2.ORB_create(n_features)

    def detect_features(self, image):
        keypoints, descriptors = self.orb.detectAndCompute(image, None)
        return keypoints, descriptors

    def draw_keypoints(self, image, keypoints):
        return cv2.drawKeypoints(image, keypoints, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)