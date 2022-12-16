# n-puzzle

## Available algorithms

### Greedy search:
```
Pros:
    - Can be faster than A* because it requires fewer calculations
    - Simple to implement
Cons:
    - Can get stuck in local minima and find suboptimal solutions
    - May not always find a solution
```

### Uniform cost search:
```
Pros:
    - Guaranteed to find the optimal solution if one exists
    - Simple to implement
Cons:
    - Can be slower than A* because it expands all nodes, even if they are not promising
    - May require a lot of memory to store all nodes
```

### A\* algorithm:
```
Pros:
    - Guaranteed to find the optimal solution if one exists
    - Can be more efficient than greedy search or uniform cost search because it uses a heuristic
      function to guide the search
Cons:
    - More computationally expensive than greedy search or uniform cost search because
      it requires more calculations
```
