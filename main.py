import numpy as np

class Fish:
    def __init__(self, path):
        self.path = path
        self.distance = self.calculate_distance(path)

    def calculate_distance(self, path):
        # 假设距离矩阵为全局变量
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += distance_matrix[path[i]][path[i + 1]]
        return total_distance

def artificial_fish_school_algorithm(distance_matrix, customer_demand, vehicle_count, max_load):
    num_customers = len(customer_demand)
    # 初始化鱼群
    fish_school = [Fish(np.random.permutation(num_customers)) for _ in range(30)]
    
    # 主循环
    for iteration in range(100):
        for fish in fish_school:
            # 觅食行为
            new_path = np.random.permutation(num_customers)
            new_fish = Fish(new_path)
            if new_fish.distance < fish.distance:
                fish = new_fish
            
            # 追尾行为（追随最佳个体）
            best_fish = min(fish_school, key=lambda f: f.distance)
            if best_fish.distance < fish.distance:
                fish = best_fish
        
    # 返回最佳路径
    best_fish = min(fish_school, key=lambda f: f.distance)
    return best_fish.path, best_fish.distance

# 示例数据
distance_matrix = np.array([
    # 距离矩阵
    [0, 11.664, 22.0698, 23.6823],
    [11.664, 0, 26.3344, 12.186],
    [22.0698, 26.3344, 0, 45.8764],
    [23.6823, 12.186, 45.8764, 0]
])

customer_demand = [50, 60, 20, 50]  # 客户需求量

# 执行算法
best_path, best_distance = artificial_fish_school_algorithm(distance_matrix, customer_demand, vehicle_count=5, max_load=7000)
print(f"最佳路径: {best_path}, 最短距离: {best_distance}")
