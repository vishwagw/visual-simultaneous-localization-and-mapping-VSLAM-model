class Mapper:
    def __init__(self):
        self.map = []

    def create_map(self, features, poses):
        # Construct a 3D map from detected features and poses
        for pose in poses:
            mapped_features = self.project_features_to_map(features, pose)
            self.map.append(mapped_features)
        return self.map

    def project_features_to_map(self, features, pose):
        # Project features into the 3D map based on the current pose
        projected_features = []
        for feature in features:
            # Example projection logic (to be implemented)
            projected_feature = {
                'x': feature['x'] + pose['x'],
                'y': feature['y'] + pose['y'],
                'z': feature['z'] + pose['z']
            }
            projected_features.append(projected_feature)
        return projected_features

    def get_map(self):
        return self.map