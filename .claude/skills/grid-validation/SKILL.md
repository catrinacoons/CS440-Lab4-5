---
name: grid-validation
description: Validate that the grid environment with valid states, boundaries, and obstacles in the vacuum robot environment.
---

# Grid Validation Skill

## Grid
S  0  0  0
0  X  0  0
0  0  0  0
0 -1  0 10

##Validation Steps
1. Verify the grid is a 4x4.
2. Verify the start state is (0,0).
3. Verify the obstacle is (1,1).
4. Verify the goal is (3,3).
5. Check that the coordinates are within bounds.
6. Ensure obstacle states are not valid states.

## Expected Output
- Valid state list
- Obstacle locations
- Grid validation results
- Any detected errors
