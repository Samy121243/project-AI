# Search Algorithms in AI – Project Examples

##  Overview
This repository presents **detailed project examples** for implementing and comparing **Search Algorithms in Artificial Intelligence**.  
Each example includes:
- A clear **problem description**
- The **implementation approach**
- **Expected deliverables**
- Key considerations when applying different **search algorithms**

---

##  Example 1: Knapsack Problem

###  Problem Description
The **Knapsack Problem** is a classic optimization problem in AI and Computer Science.

**Given:**
- A set of items, each with:
  - **Weight**
  - **Value**
- A knapsack with a **maximum weight capacity**

**Objective:**
- Select a subset of items such that:
  - The **total weight** does not exceed the knapsack capacity
  - The **total value** is **maximized**

---

###  Variants of the Knapsack Problem
- **0/1 Knapsack**  
  Each item can either be taken **once or not at all**
- **Fractional Knapsack**  
  Items can be taken partially (usually solved using greedy algorithms)

 *For search algorithms, the **0/1 Knapsack** is the most appropriate variant.*

---

###  Why This Problem?
The Knapsack Problem is ideal for demonstrating search algorithms because:

- ✔ Clearly defined **state space**
- ✔ Naturally forms a **decision tree**
- ✔ Highlights the difference between:
  - **Uninformed search**
  - **Informed (heuristic) search**
- ✔ It is **NP-hard**, making heuristics and optimization strategies essential

This allows teams to analyze:
- Solution quality
- Time complexity
- Memory usage

---

##  Algorithms Used
The project implements and compares multiple search algorithms.  
Each algorithm is implemented by a different team member:

- **Breadth-First Search (BFS)**  
  *Implemented by:* **Omar Elattar**

- **Depth-First Search (DFS)**  
  *Implemented by:* **Samy Ayman**

- **Uniform Cost Search (UCS)**  
  *Implemented by:* **Sobhy Abdelhakeem**

- **Iterative Deepening Search (IDS)**  
  *Implemented by:* **Mostafa Yasser**

- **A\* Search Algorithm**  
  *Implemented by:* **Moaz Mansour**

- **Hill Climbing**  
  *Implemented by:* **Mostafa Elhanfy**

---

##  Project Workflow – Knapsack Problem

### 1️⃣ Define the Problem Inputs
- Specify:
  - Knapsack capacity
  - List of items (weight & value)

### 2️⃣ Initialize the Solution Structure
- Create a data structure (e.g., **Dynamic Programming table**) to store:
  - Maximum achievable value for each capacity

### 3️⃣ Iterate Over the Items
- Process items one by one

### 4️⃣ Check the Weight Constraint
- Ensure the item’s weight does not exceed the current capacity

### 5️⃣ Apply the Knapsack Decision Rule
Compare two cases:
-  Excluding the item
-  Including the item and adding its value to the remaining capacity’s best solution

### 6️⃣ Update the DP Table
- Store the maximum value obtained from the comparison

### 7️⃣ Construct the Optimal Solution
- The final cell of the table contains the **maximum achievable value**

### 8️⃣ Trace Back Selected Items (Optional)
- Determine which items were chosen to reach the optimal value

### 9️⃣ Display the Result
- Output:
  - Maximum total value
  - Selected items (if required)

---

##  Expected Deliverables
- Source code for each search algorithm
- Comparative analysis of algorithm performance
- Output showing:
  - Optimal value
  - Selected items
- Documentation explaining:
  - Algorithm behavior
  - Time and space complexity

---

##  Conclusion
This project demonstrates how different **search algorithms** approach the same optimization problem, highlighting their strengths, weaknesses, and real-world trade-offs in AI problem-solving.

---

✨ *Feel free to contribute, experiment, or extend this project!*  
