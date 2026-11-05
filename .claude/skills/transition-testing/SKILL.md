--- 
name: transition-testing
description: Implement and validate state transitions for the 4x4 vacuum robot environment. Use when handling invalid actions or observing transitions for Q-learning.
---

# Transition Testing Skill

## Objective 
Provide reuable instructions for implmenting the robot movement between states.

The transition component must produce observable next states for Q-learning.

## Environment

S   0   0   0
0   X   0   0
0   0   0   0
0  -1   0  10

- Start state: (0,0)
- Obstacle: (1,1)
- Penalty cell: (3,1)
- Goal: (3,3)

## Available Actions

- UP: (-1, 0)
- DOWN: (1, 0)
- LEFT: (0, -1)
- RIGHT: (0, 1)

## Transition Rules
Use deterministic movement as an initial simulation assumption.

1. Recieve the current state and selected action.
2. Calculate the next possible state.
3. Check if it is inside the grid.
4. Check whether it contains an obstacle.
5. If valid, move to the next state.
6. If invalid, remain in current state.
7. Return the resulting state.

These are not a learned transition model.

## Implementation Instructions
1. Create transition function that accepts the current state and action.
2. Use environment validation to check the possible next state.
3. Return the observed next state.
4. Keep transition logic separate from rewards.
5. Do not implement Q-learning in this skill.
6. Make movement behavior independently testable.

## Constraints

- Do not modify reward values.
- Do not modify the grid layout.
- Do not allow movement outside the grid.
- Do not allow movement into obstacle (1,1).

## Expected Output

Provide:
- Transition function implementation
- Movement validation tests
- Invalid movement handling
- Explanation of transition assumptions