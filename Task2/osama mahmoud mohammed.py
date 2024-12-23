from itertools import permutations
import pandas as pd

conflict_table = [
    {"sub_id": 100, "Conflict_sub_id": 200, "NumOfIntercetion": 30},
    {"sub_id": 100, "Conflict_sub_id": 300, "NumOfIntercetion": 15},
    {"sub_id": 200, "Conflict_sub_id": 300, "NumOfIntercetion": 10},
]

level_table = [
    {"sub_id": 100, "level": 1},
    {"sub_id": 200, "level": 2},
    {"sub_id": 300, "level": 3},
]

def calculate_cost(order, conflicts):
    return sum(
        row['NumOfIntercetion']
        for _, row in conflicts.iterrows()
        if order.index(row['sub_id']) < order.index(row['Conflict_sub_id'])
    )

def generate_orders(levels):
    return [l1 + l2 + l3 for l1 in permutations(levels[1]) for l2 in permutations(levels[2]) for l3 in permutations(levels[3])]

def find_best_order(levels, conflicts):
    orders = generate_orders(levels)
    return min(((order, calculate_cost(order, conflicts)) for order in orders), key=lambda x: x[1])

levels = pd.DataFrame(level_table).groupby('level')['sub_id'].apply(list).to_dict()
conflicts = pd.DataFrame(conflict_table)
best_order, min_cost = find_best_order(levels, conflicts)

print("Best Order:", best_order)
print("Minimum Cost:", min_cost)
