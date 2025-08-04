# main.py

import time
from vslam.feature_detection import FeatureDetector
from vslam.feature_matching import FeatureMatcher
from vslam.pose_estimation import PoseEstimator
from vslam.mapping import Mapper
from vslam.loop_closure import LoopClosureDetector
from vslam.sensor_fusion import SensorFusion
from control.path_planning import PathPlanner
from control.mpc_controller import MPCController

class VSLAMSystem:
    def __init__(self):
        self.feature_detector = FeatureDetector()
        self.feature_matcher = FeatureMatcher()
        self.pose_estimator = PoseEstimator()
        self.mapper = Mapper()
        self.loop_closure_detector = LoopClosureDetector()
        self.sensor_fusion = SensorFusion()
        self.path_planner = PathPlanner()
        self.mpc_controller = MPCController()

    def run(self):
        while True:
            # Simulate data acquisition from sensors
            sensor_data = self.sensor_fusion.fuse_data()
            
            # Feature detection
            features = self.feature_detector.detect_features(sensor_data['image'])
            
            # Feature matching
            matches = self.feature_matcher.match_features(features)
            
            # Pose estimation
            pose = self.pose_estimator.estimate_pose(matches)
            
            # Mapping
            self.mapper.create_map(features, pose)
            
            # Loop closure detection
            self.loop_closure_detector.detect_loop_closure(pose)
            
            # Path planning and control
            path = self.path_planner.plan_path(pose)
            self.mpc_controller.control_drone(path)
            
            # Sleep to simulate processing time
            time.sleep(0.1)

if __name__ == "__main__":
    vslam_system = VSLAMSystem()
    vslam_system.run()