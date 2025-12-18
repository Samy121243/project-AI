import time

items = [
    {"id": 1, "name": "Book",       "weight": 1, "value": 1},
    {"id": 2, "name": "Laptop",     "weight": 4, "value": 30},
    {"id": 3, "name": "Camera",     "weight": 3, "value": 20},
    {"id": 4, "name": "Headphones", "weight": 2, "value": 15},
    {"id": 5, "name": "Phone",      "weight": 3, "value": 25}
]

capacity = 6

best_value = 0
best_weight = 0
best_combination = []

print("Starting Iterative Deepening Search (IDS) to solve the 0/1 Knapsack problem\n")
print(f"Knapsack capacity: {capacity}")
print(f"Number of items: {len(items)}\n")
print("-" * 70)

start_time = time.time()

def depth_limited_search(index, depth, current_weight, current_value, selected_items):
    global best_value, best_weight, best_combination


    if current_weight > capacity:
        return

  
    if depth == 0 or index == len(items):
        if current_value > best_value:
            best_value = current_value
            best_weight = current_weight
            best_combination = selected_items[:]
        return

    item = items[index]


    print(f"Depth {index} → Exclude: {item['name']} | Weight: {current_weight} | Value: {current_value}")
    depth_limited_search(
        index + 1,
        depth - 1,
        current_weight,
        current_value,
        selected_items
    )


    if current_weight + item["weight"] <= capacity:
        print(f"Depth {index} → Include: {item['name']} | "
              f"Weight: {current_weight + item['weight']} | "
              f"Value: {current_value + item['value']}")
        selected_items.append(item)
        depth_limited_search(
            index + 1,
            depth - 1,
            current_weight + item["weight"],
            current_value + item["value"],
            selected_items
        )
        selected_items.pop()
    else:
        print(f"Depth {index} → Cannot include {item['name']} (capacity exceeded!)")


for depth_limit in range(len(items) + 1):
    print(f"\n--- Iteration with Depth Limit = {depth_limit} ---")
    depth_limited_search(0, depth_limit, 0, 0, [])

end_time = time.time()

print("-" * 70)
print("\nFinished exploring all depths!")
print(f"Best possible value = {best_value}")
print(f"Used weight = {best_weight}/{capacity}")
print("Selected items:")
for item in best_combination:
    print(f"   • {item['name']} (Weight: {item['weight']}, Value: {item['value']})")

print(f"\nExecution time: {end_time - start_time:.4f} seconds")
