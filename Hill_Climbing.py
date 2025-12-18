import time
import random

items = [
    {"id": 1, "name": "Book",       "weight": 1, "value": 1},
    {"id": 2, "name": "Laptop",     "weight": 4, "value": 30},
    {"id": 3, "name": "Camera",     "weight": 3, "value": 20},
    {"id": 4, "name": "Headphones", "weight": 2, "value": 15},
    {"id": 5, "name": "Phone",      "weight": 3, "value": 25}
]

capacity = 6

print("Starting Hill Climbing to solve the 0/1 Knapsack problem\n")
print(f"Knapsack capacity: {capacity}")
print(f"Number of items: {len(items)}\n")
print("-" * 70)

start_time = time.time()


def evaluate(solution):
    total_weight = sum(item["weight"] for item in solution)
    total_value = sum(item["value"] for item in solution)
    if total_weight > capacity:
        return -1 
    return total_value


current_solution = []
current_value = evaluate(current_solution)

print(f"Initial state → Weight: 0 | Value: 0")

improved = True
while improved:
    improved = False
    best_neighbor = current_solution
    best_value = current_value


    for item in items:
        neighbor = current_solution[:]

        if item in neighbor:
            neighbor.remove(item)   
            action = f"Remove {item['name']}"
        else:
            neighbor.append(item)   
            action = f"Add {item['name']}"

        value = evaluate(neighbor)
        weight = sum(i["weight"] for i in neighbor)

        print(f"Try → {action} | Weight: {weight} | Value: {value}")

        if value > best_value:
            best_neighbor = neighbor
            best_value = value
            improved = True

    current_solution = best_neighbor
    current_value = best_value

    if improved:
        print(f"✔ Move to better state → Weight: "
              f"{sum(i['weight'] for i in current_solution)} | "
              f"Value: {current_value}")
        print("-" * 50)

end_time = time.time()

print("-" * 70)
print("\nFinished Hill Climbing!")
print(f"Final value = {current_value}")
print(f"Used weight = {sum(i['weight'] for i in current_solution)}/{capacity}")
print("Selected items:")
for item in current_solution:
    print(f"   • {item['name']} (Weight: {item['weight']}, Value: {item['value']})")

print(f"\nExecution time: {end_time - start_time:.4f} seconds")
