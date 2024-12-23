import heapq
from collections import defaultdict

###### البيانات: جدول التقاطعات وجداول المستويات
conflict_table = [
    {'sub_id': 1, 'conflict_sub_id': 2, 'NumOfIntersection': 3},
    {'sub_id': 1, 'conflict_sub_id': 3, 'NumOfIntersection': 2},
    {'sub_id': 2, 'conflict_sub_id': 3, 'NumOfIntersection': 1},
    # ... إضافة باقي البيانات
]

level_table = [
    {'sub_id': 1, 'level': 'First'},
    {'sub_id': 2, 'level': 'Second'},
    {'sub_id': 3, 'level': 'Third'},
    # ... إضافة باقي البيانات
]

subjects_per_level = 6

######## بناء التمثيل البياني
graph = defaultdict(list)
for conflict in conflict_table:
    u, v, weight = conflict['sub_id'], conflict['conflict_sub_id'], conflict['NumOfIntersection']
    graph[u].append((v, weight))
    graph[v].append((u, weight))

######### ترتيب المقررات حسب الأولوية باستخدام Heap Sort
def sort_subjects_by_priority(conflict_table):
    priority_queue = []
    for conflict in conflict_table:
        heapq.heappush(priority_queue, (conflict['NumOfIntersection'], conflict['sub_id']))
    sorted_subjects = []
    while priority_queue:
        sorted_subjects.append(heapq.heappop(priority_queue))
    return [sub_id for _, sub_id in sorted_subjects]

sorted_subjects = sort_subjects_by_priority(conflict_table)

##### توزيع المقررات على المستويات
def distribute_subjects(sorted_subjects, level_table, subjects_per_level):
    levels = {'First': [], 'Second': [], 'Third': []}
    level_order = ['First', 'Second', 'Third']
    level_index = 0

    for sub_id in sorted_subjects:
        level_name = level_order[level_index]
        if len(levels[level_name]) < subjects_per_level:
            levels[level_name].append(sub_id)
        else:
            level_index = (level_index + 1) % len(level_order)
            levels[level_order[level_index]].append(sub_id)

    return levels

levels_distribution = distribute_subjects(sorted_subjects, level_table, subjects_per_level)

# ###### حساب التكلفة النهائية
def calculate_final_cost(levels_distribution, graph):
    cost = 0
    for level, subjects in levels_distribution.items():
        for i in range(len(subjects)):
            for j in range(i + 1, len(subjects)):
                u, v = subjects[i], subjects[j]
                for neighbor, weight in graph[u]:
                    if neighbor == v:
                        cost += weight
    return cost

final_cost = calculate_final_cost(levels_distribution, graph)

######## عرض النتائج
print("ترتيب المقررات حسب المستويات:")
for level, subjects in levels_distribution.items():
    print(f"{level}: {subjects}")

print("\nالتكلفة النهائية:", final_cost)
