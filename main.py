import numpy as np
import random

# 定义配送点和距离矩阵
distance_matrix = np.array([
    [0, 11.664, 22.0698, 42.9336, 23.6823, 10.0424, 29.231, 61.2049],  # 仓库
    [11.664, 0, 26.3344, 12.186, 35.6682, 3.8953, 30.7112, 71.2565],  # 客户1
    [22.0698, 26.3344, 0, 44.773, 12.8769, 35.7188, 80.7583],          # 客户2
    [42.9336, 12.186, 44.773, 0, 47.0516, 14.0086, 38.5624],          # 客户3
    [23.6823, 35.6682, 12.8769, 47.0516, 0, 35.7555, 64.9765],        # 客户4
    [10.0424, 3.8953, 35.7188, 14.0086, 35.7555, 0, 33.2539],         # 客户5
    [29.231, 30.7112, 80.7583, 38.5624, 64.9765, 33.2539, 0],         # 客户6
    [61.2049, 71.2565, 0, 83.1142, 0, 70.9789, 53.445],               # 客户7
])

# 客户需求量
customer_demand = [50, 60, 20, 50, 40, 100, 60, 80]

# 基本参数
num_vehicles = 5
max_load = 7000

def calculate_fitness(path):
      """计算路径的适应度（总距离）"""
    if len(path) < 2:
        return float('inf')  # 无效路径，返回无穷大
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    return total_distance

def crossover(parent1, parent2):
    """交叉操作"""
    point = random.randint(1, len(parent1) - 2)
    child = parent1[:point] + [x for x in parent2 if x not in parent1[:point]]
    return child

def mutate(path):
    """变异操作"""
    if random.random() < 0.1:  # 10% 变异概率
        i, j = random.sample(range(1, len(path)), 2)
        path[i], path[j] = path[j], path[i]  # 交换两个节点
    return path

def genetic_algorithm(num_generations, population_size):
    """遗传算法主函数"""
    # 初始化种群
    population = [random.sample(range(len(distance_matrix)), len(distance_matrix)) for _ in range(population_size)]
    
    for generation in range(num_generations):
        population.sort(key=calculate_fitness)  # 按适应度排序
        next_population = population[:population_size // 2]  # 选择前一半

        while len(next_population) < population_size:
            parent1, parent2 = random.sample(next_population, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            next_population.append(child)

        population = next_population

    best_path = min(population, key=calculate_fitness)
    return best_path, calculate_fitness(best_path)

# 运行遗传算法
best_path, best_distance = genetic_algorithm(num_generations=100, population_size=50)

# 输出结果
print("最优路径:", best_path)
print("最优距离:", best_distance)
