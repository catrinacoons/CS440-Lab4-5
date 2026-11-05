---
name: reward-design 
description: Design, calculate, and validate rewards for the vacuum robot reinforcement learning environment. Use when implementing reward functions, evaluating state rewards, or tuning the living reward.

---

# Reward Design Skill

## Objective
Provide consistent instructions for calculating rewards in the 4x4 vacuum robot environment.

The reward function will support Q-learning by providing feedback after each robot action.

## Environment

S   0   0   0
0   X   0   0
0   0   0   0
0  -1   0  10

Special cells:
- Start: (0,0)
- Obstacle: (1,1)
- Penalty: (3,1)
- Goal: (3,3)

## Reward Configuration

Use the following values:

- Living reward: -0.1
- Penalty cell: -1
- Goal: +10

## Reward Calculation
Calculate rewards based on the state the robot enters after an action.

1. If the robot reaches the goal:
    return +10

2. If the robot enters the penalty cell:
    return -1

3. For all valid transitions:
    return living reward (-0.1)

The special-cell rewards replace the living reward instead of being added to it.

## Implementation Steps
1. Create reward function that accepts the resulting      state as input.
2. Check whether the state is the goal.
3. Check whether the state is the penalty cell.
4. Otherwise return living cell.
5. Keep reward logic separate from movement logic.
6. Make reward values configurable.

## Constraints
- Do not implement Q-learning in this skill.
- Do not modify the environment layout.
- Do not calculate transition probabilities.
- Do not assign rewards to invalid states.
- Do not modify the transition agent's logic.

## Expected Output

Provide:
- Reward function implementation
- Reward configuration
- Unit tests for reward values
- Explanation of reward design decisions