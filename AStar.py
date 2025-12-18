import time
import heapq

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

print("Starting A* Search to solve the 0/1 Knapsack problem\n")
print(f"Knapsack capacity: {capacity}")
print(f"Number of items: {len(items)}\n")
print("-" * 70)

start_time = time.time()

def heuristic(index):
    return sum(item["value"] for item in items[index:])

priority_queue = []
heapq.heappush(priority_queue, (0, 0, 0, 0, []))

visited = set()

while priority_queue:
    neg_f, index, current_weight, current_value, selected_items = heapq.heappop(priority_queue)

    state = (index, current_weight)
    if state in visited:
        continue
    visited.add(state)

    if current_value > best_value:
        best_value = current_value
        best_weight = current_weight
        best_combination = selected_items[:]

    if index == len(items):
        continue

    item = items[index]

    print(f"Depth {index} → Exclude: {item['name']} | "
          f"Weight: {current_weight} | Value: {current_value}")

    g = current_value
    h = heuristic(index + 1)
    f = g + h
    heapq.heappush(
        priority_queue,
        (-f, index + 1, current_weight, current_value, selected_items[:])
    )

    if current_weight + item["weight"] <= capacity:
        new_weight = current_weight + item["weight"]
        new_value = current_value + item["value"]

        print(f"Depth {index} → Include: {item['name']} | "
              f"Weight: {new_weight} | Value: {new_value}")

        g = new_value
        h = heuristic(index + 1)
        f = g + h

        new_selected = selected_items[:]
        new_selected.append(item)

        heapq.heappush(
            priority_queue,
            (-f, index + 1, new_weight, new_value, new_selected)
        )
    else:
        print(f"Depth {index} → Cannot include {item['name']} (capacity exceeded!)")

end_time = time.time()

print("-" * 70)
print("\nFinished A* Search!")
print(f"Best possible value = {best_value}")
print(f"Used weight = {best_weight}/{capacity}")
print("Selected items:")
for item in best_combination:
    print(f"   • {item['name']} (Weight: {item['weight']}, Value: {item['value']})")

print(f"\nExecution time: {end_time - start_time:.4f} seconds")
