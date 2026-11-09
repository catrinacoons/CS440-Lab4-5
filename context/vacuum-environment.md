# Vacuum Robot Environment

## Problem
Implement Q-learning for a reinforcement learning vacuum robot,
that uses the environment below.


## Grid (row, col), start at top-left
S   0   0   0
0   X   0   0
0   0   0   0
0  -1   0  10

## Known Information
- Grid size: 4x4
- S = start (0,0); X = wall/obstacle at (1,1) (not enterable)
- -1 at (3,1) = penalty terminal state (the "stairs"/pit)
- 10 at (3,3) = goal terminal state
- Actions: up, down, left, right. Bumping a wall/edge = stay in place.

## Unknown Information
- Transition model T
- Complete reward function R
- Movement probabilities

## Hyperparameters
- Living reward: -0.04
- Discount (gamma): 0.9
- Learning rate (alpha): 0.1
- Epsilon: 0.1
- Invalid action behavior
- Terminal-state rules

## Constraints
- Do not assume missing requirements.
- Separate confirmed facts from assumptions.
