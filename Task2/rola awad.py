from itertools import permutations

# المدخلات
conflict_table=[
    {
        "sub_id":100,
        "conflict_sub_id":200,
        "num_of_intersection":30
    },
    {
        "sub_id":200,
        "conflict_sub_id":300,
         "num_of_intersection":15
    },
]
level_table=[
    {"sub_id":100,"level":1},
    {"sub_id":200,"level":2},
    {"sub_id":300,"level":3},
]

#عدد المقررات لكل مستوى
courses_per_level={
    1:[100],
    2:[200],
    3:[300],
}

#انشاء جميع الانماط الممكنه لترتيب المستوبات
level_patterns=list(permutations([1,2,3]))

#داله لحساب تكلفه التعارض
def calculate_cost(pattern,conflict_table,courses_per_level):
    total_cost=0
    schedule=[]

#بناء الجدول حسب النمط
    for level in pattern:
        schedule.extend(courses_per_level[level])

#نحسب تكلفه التعارض
    for day in range(len(schedule)-1):
        course1=schedule[day]
        course2=schedule[day+1]
        for conflict in conflict_table:
            if(conflict["sub_id"]==course1 and 
         conflict["conflict_sub_id"]==course2) or\
                (conflict["sub_id"]==course2 and 
        conflict["conflict_sub_id"]==course1):
                 total_cost+=conflict["num_of_intersection"]
        return total_cost

#نبحث عن الترتيب الافضل 
optimal_pattern=None
min_cost=float("inf")
for pattern in level_patterns:
    cost=calculate_cost(pattern,conflict_table,courses_per_level)
    if cost<min_cost:
        min_cost=cost
        optimal_pattern=pattern

#طباعه الناتج
print("Best level arrangement",optimal_pattern)
print("Less cost to conflict",min_cost)

            

