import itertools

# تعريف جدول التداخلات بين المقررات
conflicts = [
    {"sub_id": 100, "conflict_sub_id": 200, "NumOfInteraction": 30},
    {"sub_id": 100, "conflict_sub_id": 300, "NumOfInteraction": 15},
]


levels = [
    {"sub_id": 100, "level": 1},
    {"sub_id": 200, "level": 2},
    {"sub_id": 300, "level": 3},
]

# تصنيف المقررات حسب المستوى
levels_dict = {}
for level in levels:
    lvl = level["level"]
    if lvl not in levels_dict:
        levels_dict[lvl] = []
    levels_dict[lvl].append(level["sub_id"])

# استخراج جميع الترتيبات الممكنة للمقررات
level_permutations = [
    list(itertools.permutations(levels_dict[level])) for level in levels_dict
]

# دمج الترتيبات
all_combinations = list(itertools.product(*level_permutations))

# دالة لحساب تكلفة التداخلات لترتيب معين
def calculate_cost(order):
    cost = 0
    for conflict in conflicts:
        try:
            index1 = order.index(conflict["sub_id"])
            index2 = order.index(conflict["conflict_sub_id"])
            # إذا كانت المقررات في أيام متتالية نحسب التكلفة
            if abs(index1 - index2) == 1:
                cost += conflict["NumOfInteraction"]
        except ValueError:
            pass
    return cost

# إيجاد الترتيب بأقل تكلفة
best_order = None
min_cost = float("inf")

for combination in all_combinations:
    # تحويل الترتيب من tuple إلى قائمة
    flattened_order = [item for sublist in combination for item in sublist]
    cost = calculate_cost(flattened_order)
    if cost < min_cost:
        min_cost = cost
        best_order = flattened_order

# طباعة النتيجة
print("أفضل ترتيب للمقررات:", best_order)
print("التكلفة الإجمالية:", min_cost)
