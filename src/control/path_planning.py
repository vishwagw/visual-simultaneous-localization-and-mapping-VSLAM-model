class PathPlanner:
    def __init__(self, start, goal, obstacles):
        self.start = start
        self.goal = goal
        self.obstacles = obstacles

    def plan_path(self):
        # Implement the RRT* algorithm to generate a path from start to goal
        path = self.rrt_star(self.start, self.goal, self.obstacles)
        return path

    def rrt_star(self, start, goal, obstacles):
        # Placeholder for RRT* algorithm implementation
        # This function should return a list of waypoints representing the path
        pass

    def is_collision_free(self, point):
        # Check if the point collides with any obstacles
        for obstacle in self.obstacles:
            if self.distance(point, obstacle) < obstacle.radius:
                return False
        return True

    def distance(self, point1, point2):
        # Calculate the Euclidean distance between two points
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5