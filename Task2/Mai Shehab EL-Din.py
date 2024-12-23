import pandas as pd

# Input data
conflict_table = pd.DataFrame({
    'sub_id': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Conflict_sub_id': ['B', 'C', 'D', 'E', 'F', 'A'],
    'NumOfIntercetion': [3, 2, 4, 5, 1, 2]
})

level_table = pd.DataFrame({
    'sub_id': ['A', 'B', 'C', 'D', 'E', 'F'],
    'level': ['First', 'Second', 'Third', 'First', 'Second', 'Third']
})

# Distribute courses by levels
levels = {
    "First": level_table[level_table['level'] == 'First']['sub_id'].tolist(),
    "Second": level_table[level_table['level'] == 'Second']['sub_id'].tolist(),
    "Third": level_table[level_table['level'] == 'Third']['sub_id'].tolist()
}

# Create a dictionary to store conflicts and their costs
conflict_dict = {}
for _, row in conflict_table.iterrows():
    if row['sub_id'] not in conflict_dict:
        conflict_dict[row['sub_id']] = {}
    conflict_dict[row['sub_id']][row['Conflict_sub_id']] = row['NumOfIntercetion']

# Patterns
patterns = [
    ["First", "Second", "Third"],
    ["Third", "Second", "First"]
]

# Cost calculation function using the conflict_dict
def calculate_cost(order, conflict_dict, levels):
    cost = 0
    for i in range(len(order) - 1):
        current_level = levels[order[i]]
        next_level = levels[order[i + 1]]
        for sub_id in current_level:
            for conflict_sub_id in next_level:
                if conflict_sub_id in conflict_dict.get(sub_id, {}):
                    cost += conflict_dict[sub_id][conflict_sub_id]
    return cost

# Find the optimal order
best_order = None
min_cost = float('inf')

for pattern in patterns:
    cost = calculate_cost(pattern, conflict_dict, levels)
    if cost < min_cost:
        min_cost = cost
        best_order = pattern

# Output
print(f"Best course order: {best_order}")
print(f"Final cost: {min_cost}")
