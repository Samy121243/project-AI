import time
from collections import deque


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

queue = deque()

queue.append((0, 0, 0, [], ""))

print(f"\n  (( Project Ai )) ==> BFS ")

print("Starting BFS to solve the 0/1 Knapsack problem\n")
print(f"Knapsack capacity: {capacity}")
print(f"Number of items: {len(items)}\n")
print("-" * 70)

start_time = time.time()

while queue:
    index, current_weight, current_value, selected_items, path = queue.popleft()

    if index == len(items):
        if current_value > best_value:
            best_value = current_value
            best_weight = current_weight
            best_combination = selected_items[:] 
        continue

    item = items[index]

    exclude_msg = f"Depth {index} → Exclude: {item['name']} | Weight: {current_weight} | Value: {current_value}"
    print(exclude_msg)
    queue.append((index + 1, current_weight, current_value, selected_items[:], path + " ← Exclude"))

    if current_weight + item["weight"] <= capacity:
        include_msg = f"Depth {index} → Include: {item['name']} | Weight: {current_weight + item['weight']} | Value: {current_value + item['value']}"
        print(include_msg)
        new_selected = selected_items[:]
        new_selected.append(item)
        queue.append((index + 1, current_weight + item["weight"], current_value + item["value"], new_selected, path + " → Include"))
    else:
        print(f"Depth {index} → Cannot include {item['name']} (capacity exceeded!)")

end_time = time.time()

print("-" * 70)
print("\nFinished exploring all branches!")
print(f"Best possible value = {best_value}")
print(f"Used weight = {best_weight}/{capacity}")
print("Selected items:")
for item in best_combination:
    print(f"   • {item['name']} (Weight: {item['weight']}, Value: {item['value']})")

print(f"\nExecution time: {end_time - start_time:.4f} seconds")