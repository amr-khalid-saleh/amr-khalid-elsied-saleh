import itertools

conflicts = [
    {"sub_id": 100, "conflict_sub_id": 300, "num_of_intersections": 15},
    {"sub_id": 200, "conflict_sub_id": 100, "num_of_intersections": 10},
    {"sub_id": 300, "conflict_sub_id": 200, "num_of_intersections": 20},
]

levels = {
    1: [100, 200, 300],
    2: [400, 500, 600],
    3: [700, 800, 900]
}

def calculate_cost(schedule, conflicts):
    cost = 0
    for i in range(len(schedule) - 1):
        for conflict in conflicts:
            if (conflict["sub_id"] in schedule[i] and conflict["conflict_sub_id"] in schedule[i + 1]) or \
               (conflict["conflict_sub_id"] in schedule[i] and conflict["sub_id"] in schedule[i + 1]):
                cost += conflict["num_of_intersections"]
    return cost

level_orders = list(itertools.permutations(levels.keys()))
best_schedule = None
min_cost = float('inf')

for order in level_orders:
    schedule = []
    for i in range(courses_per_level):
        for level in order:
            if len(levels[level]) > i:
                schedule.append(levels[level][i:i + 1])
    cost = calculate_cost(schedule, conflicts)
    if cost < min_cost:
        min_cost = cost
        best_schedule = schedule

print("أفضل ترتيب:", best_schedule)
print("التكلفة:", min_cost)