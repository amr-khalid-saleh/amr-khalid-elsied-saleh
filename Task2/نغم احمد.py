from itertools import permutations


conflicts = [
    {"sub_id": 100, "Conflict_sub_id": 200, "NumOfIntersection": 30},
    {"sub_id": 100, "Conflict_sub_id": 300, "NumOfIntersection": 15},
    {"sub_id": 200, "Conflict_sub_id": 300, "NumOfIntersection": 20},
]


levels = [
    {"sub_id": 100, "level": 1},
    {"sub_id": 200, "level": 2},
    {"sub_id": 300, "level": 3},
]


level_groups = {1: [], 2: [], 3: []}
for level in levels:
    level_groups[level["level"]].append(level["sub_id"])


patterns = [
    [1, 2, 3],  # مستوى أول ← ثاني ← ثالث
    [3, 2, 1],  # مستوى ثالث ← ثاني ← أول
]


def calculate_cost(order):
    total_cost = 0
    for i in range(len(order) - 1):
        for conflict in conflicts:
            if conflict["sub_id"] in order[i] and conflict["Conflict_sub_id"] in order[i + 1]:
                total_cost += conflict["NumOfIntersection"]
    return total_cost


min_cost = float("inf")
best_order = None

for pattern in patterns:
   
    possible_orders = permutations(
        level_groups[pattern[0]] + level_groups[pattern[1]] + level_groups[pattern[2]]
    )
    for order in possible_orders:
        cost = calculate_cost(order)
        if cost < min_cost:
            min_cost = cost
            best_order = order


print("أفضل ترتيب للمقررات:", best_order)
print("التكلفة النهائية:", min_cost)
