data_structure = [

[1, 2, 3],

{'a': 4, 'b': 5},

(6, {'cube': 7, 'drum': 8}),

"Hello",

((), [{(2, 'Urban', ('Urban2', 35))}])

]


def calculate_structure_sum(item):
    total_sum = 0
    if isinstance(item, (int, float)):
        total_sum += item
    elif isinstance(item, str):
        total_sum += len(item)
    elif isinstance(item, (list, tuple, set)):
        for i in item:
            total_sum += calculate_structure_sum(i)
    elif isinstance(item, dict):
        for key, value in item.items():
            total_sum += calculate_structure_sum(key)
            total_sum += calculate_structure_sum(value)
    return total_sum

print(calculate_structure_sum(data_structure))






