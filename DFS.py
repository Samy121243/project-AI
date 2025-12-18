items = [
    {"id": 1, "name": "Book",      "weight": 1, "value": 1},
    {"id": 2, "name": "Laptop",    "weight": 4, "value": 30},
    {"id": 3, "name": "Camera",    "weight": 3, "value": 20},
    {"id": 4, "name": "Headphones","weight": 2, "value": 15},
    {"id": 5, "name": "Phone",     "weight": 3, "value": 25}
]

capacity = 6

best_value = 0
best_combination = []
best_weight = 0

def dfs_knapsack(index, current_weight, current_value, selected_items, path):
    global best_value, best_combination, best_weight

    if index == len(items):
        if current_value > best_value:
            best_value = current_value
            best_weight = current_weight
            best_combination = selected_items.copy()
        return

    item = items[index]

    print(f"Depth {index} → Exclude: {item['name']} | Weight: {current_weight} | Value: {current_value}")
    dfs_knapsack(index + 1, current_weight, current_value, selected_items, path + " ← Exclude")

    if current_weight + item["weight"] <= capacity:
        selected_items.append(item)
        print(f"Depth {index} → Include: {item['name']} | Weight: {current_weight + item['weight']} | Value: {current_value + item['value']}")
        dfs_knapsack(
            index + 1,
            current_weight + item["weight"],
            current_value + item["value"],
            selected_items,
            path + " → Include"
        )
        selected_items.pop()
    else:
        print(f"Depth {index} → Cannot include {item['name']} (capacity exceeded!)")

print("Starting DFS to solve the 0/1 Knapsack problem\n")
print(f"Knapsack capacity: {capacity}")
print(f"Number of items: {len(items)}\n")
print("-" * 70)

import time
start_time = time.time()

dfs_knapsack(0, 0, 0, [], "")

end_time = time.time()

print("-" * 70)
print("\nFinished exploring all branches!")
print(f"Best possible value = {best_value}")
print(f"Used weight = {best_weight}/{capacity}")
print("Selected items:")
for item in best_combination:
    print(f"   • {item['name']} (Weight: {item['weight']}, Value: {item['value']})")

print(f"\nExecution time: {end_time - start_time:.4f} seconds")
