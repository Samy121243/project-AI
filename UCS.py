import time
import heapq

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

priority_queue = []

heapq.heappush(priority_queue, (0, 0, 0, [], ""))  

print("Starting Uniform Cost Search (UCS) to solve the 0/1 Knapsack problem\n")
print(f"Knapsack capacity: {capacity}")
print(f"Number of items: {len(items)}\n")
print("-" * 70)

start_time = time.time()

visited = {}  

while priority_queue:
    neg_value, current_weight, index, selected_items, path = heapq.heappop(priority_queue)
    current_value = -neg_value

    state_key = (index, current_weight)

    if state_key in visited and visited[state_key] <= neg_value:
        continue

 
    visited[state_key] = neg_value

    if index == len(items):
       
        if current_value > best_value:
            best_value = current_value
            best_weight = current_weight
            best_combination = selected_items[:]  
        continue

    item = items[index]


    print(f"Depth {index} → Exclude: {item['name']} | Weight: {current_weight} | Value: {current_value}")
    heapq.heappush(priority_queue, (-current_value, current_weight, index + 1, selected_items[:], path + " ← Exclude"))

  
    if current_weight + item["weight"] <= capacity:
        new_weight = current_weight + item["weight"]
        new_value = current_value + item["value"]
        print(f"Depth {index} → Include: {item['name']} | Weight: {new_weight} | Value: {new_value}")
        new_selected = selected_items[:]
        new_selected.append(item)
        heapq.heappush(priority_queue, (-new_value, new_weight, index + 1, new_selected, path + " → Include"))
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