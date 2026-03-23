from itertools import combinations

items = {1:[12, 4], 2:[2, 2], 3:[1, 2], 4:[1, 1], 5:[4, 10]} #ключ:[вага, ціна]
max_capacity = 15 #максимальна вага рюкзака

#1. генеруємо всі можливі комбінації
all_combinations = []
for size in range(len(items) + 1):
    for comb in combinations(items.keys(), size):
        all_combinations.append(comb)

print(f"Усі можливі комбінації: {all_combinations}")
print("-"*20)

#2. та 3. - визначаємо вагу та відбираємо задовільні варіанти
valid_comb = []
for current_comb in all_combinations:
    current_weight = sum(items[item][0] for item in current_comb)
    if current_weight <= max_capacity:
        valid_comb.append(current_comb)

print(f"Комбінації, що не перевищують дозволену вагу рюкзака: {valid_comb}")
print("-"*20)

#4. визначаємо ціну кожної підмножини
comb_val = []
for current_comb in valid_comb:
    current_val = sum(items[item][1] for item in current_comb)
    comb_val.append(current_val)

print(f"Ціна кожної з цих комбінацій:{comb_val}")
print("-"*20)

#5. обираємо максимальне значення
max_val = max(comb_val)
index = comb_val.index(max_val)
best_comb = valid_comb[index]

print(f"Найкраща комбінація: предмети {best_comb} та їх ціна {max_val}")