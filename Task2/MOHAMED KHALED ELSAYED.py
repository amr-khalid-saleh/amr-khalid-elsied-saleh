import itertools

#MOHAMED KHALED ELSAYED

# Input data
data = {
    "conflicts": [
        {"subject_id": 100, "conflict_subject_id": 200, "intersection_count": 30},
        {"subject_id": 100, "conflict_subject_id": 300, "intersection_count": 15},
        {"subject_id": 200, "conflict_subject_id": 300, "intersection_count": 20},
    ],
    "levels": [
        {"subject_id": 100, "level": 1},
        {"subject_id": 200, "level": 2},
        {"subject_id": 300, "level": 3},
    ],
    "level_patterns": [
        [1, 2, 3],
        [3, 2, 1],
    ]
}

# Create a mapping from levels to subject IDs
level_to_subjects = {}
for item in data["levels"]:
    level_to_subjects.setdefault(item["level"], []).append(item["subject_id"])

def calculate_total_cost(order, conflicts):
    """Calculate the cost of a given order based on conflicts."""
    total_cost = 0
    for conflict in conflicts:
        if conflict["subject_id"] in order and conflict["conflict_subject_id"] in order:
            index1 = order.index(conflict["subject_id"])
            index2 = order.index(conflict["conflict_subject_id"])
            if abs(index1 - index2) == 1:  # Only consider adjacent subjects
                total_cost += conflict["intersection_count"]
    return total_cost

# Find the optimal order
optimal_order = None
minimum_cost = float('inf')

for pattern in data["level_patterns"]:
    # Collect subjects based on the level pattern
    subjects_in_pattern = [
        subject_id
        for level in pattern
        for subject_id in level_to_subjects.get(level, [])
    ]

    # Generate all permutations of the subjects
    for perm in itertools.permutations(subjects_in_pattern):
        cost = calculate_total_cost(perm, data["conflicts"])
        if cost < minimum_cost:
            minimum_cost = cost
            optimal_order = perm

# Output results
print("Optimal order:", optimal_order)
print("Minimum cost:", minimum_cost)
