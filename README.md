# Visual SLAM Drone Agent

This project implements a Visual SLAM (Simultaneous Localization and Mapping) system designed for autonomous drone navigation. The system utilizes various algorithms and techniques to enable the drone to perceive its environment, estimate its position, and create a map of the surroundings.

## Project Structure

```
vslam-drone-agent
├── src
│   ├── main.py                # Entry point of the application
│   ├── vslam                  # VSLAM algorithms and modules
│   │   ├── __init__.py
│   │   ├── feature_detection.py
│   │   ├── feature_matching.py
│   │   ├── pose_estimation.py
│   │   ├── mapping.py
│   │   ├── loop_closure.py
│   │   └── sensor_fusion.py
│   ├── control                # Control algorithms for drone navigation
│   │   ├── __init__.py
│   │   ├── path_planning.py
│   │   └── mpc_controller.py
│   ├── utils                  # Utility functions for visualization and processing
│   │   ├── __init__.py
│   │   └── visualization.py
│   └── config                 # Configuration settings
│       └── settings.yaml
├── tests                      # Unit tests for the project
│   ├── test_feature_detection.py
│   ├── test_pose_estimation.py
│   └── test_mapping.py
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Files to ignore in version control
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd vslam-drone-agent
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the Visual SLAM system, execute the following command:
```
python src/main.py
```

## Features

- **Feature Detection**: Utilizes ORB (Oriented FAST and Rotated BRIEF) for detecting key features in images.
- **Feature Matching**: Matches detected features using descriptors for robust tracking.
- **Pose Estimation**: Estimates the drone's pose using visual-inertial odometry.
- **Mapping**: Constructs a 3D map from detected features and poses.
- **Loop Closure Detection**: Identifies previously visited locations to correct drift.
- **Sensor Fusion**: Combines data from various sensors (camera, IMU) for improved accuracy.
- **Path Planning**: Generates a path for the drone to follow using algorithms like RRT*.
- **Model Predictive Control**: Implements control strategies for drone navigation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.