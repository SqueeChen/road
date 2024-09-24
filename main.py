import numpy as np

# 完整距离矩阵，包括所有客户和配送中心
distance_matrix = np.array([
    [0, 11.664, 22.0698, 23.6823, 20.0, 15.0, 30.0, 35.0],  # 从仓库中心到其他客户
    [11.664, 0, 26.3344, 12.186, 17.0, 22.0, 33.0, 27.0],
    [22.0698, 26.3344, 0, 45.8764, 30.0, 25.0, 20.0, 40.0],
    [23.6823, 12.186, 45.8764, 0, 12.0, 15.0, 10.0, 22.0],
    [20.0, 17.0, 30.0, 12.0, 0, 35.0, 20.0, 25.0],
    [15.0, 22.0, 25.0, 15.0, 35.0, 0, 18.0, 30.0],
    [30.0, 33.0, 20.0, 10.0, 20.0, 18.0, 0, 15.0],
    [35.0, 27.0, 40.0, 22.0, 25.0, 30.0, 15.0, 0]
])

# 客户需求量（每个客户的需求量）
customer_demand = [50, 60, 20, 50, 40, 100, 60, 80]  # 各客户的需求量

# 车辆信息
vehicle_count = 5  # 车辆数量
max_load = 7000  # 每辆车的最大载重（kg）

# 人工鱼群算法的实现
class Fish:
    def __init__(self, path):
        self.path = path
        self.distance = self.calculate_distance(path)

    def calculate_distance(self, path):
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += distance_matrix[path[i]][path[i + 1]]
        return total_distance

def artificial_fish_school_algorithm(distance_matrix, customer_demand, vehicle_count, max_load):
    num_customers = len(customer_demand)
    fish_school = [Fish(np.random.permutation(num_customers)) for _ in range(30)]

    for iteration in range(100):
        for fish in fish_school:
            new_path = np.random.permutation(num_customers)
            new_fish = Fish(new_path)
            if new_fish.distance < fish.distance:
                fish = new_fish
            
            best_fish = min(fish_school, key=lambda f: f.distance)
            if best_fish.distance < fish.distance:
                fish = best_fish
        
    best_fish = min(fish_school, key=lambda f: f.distance)
    return best_fish.path, best_fish.distance

# 执行算法
best_path, best_distance = artificial_fish_school_algorithm(distance_matrix, customer_demand, vehicle_count, max_load)
print(f"最佳路径: {best_path}, 最短距离: {best_distance:.2f} km")
