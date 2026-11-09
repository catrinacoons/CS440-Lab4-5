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

## Decision Log
Decisions confirmed by the user on 2026-11-08 to resolve the unknowns above.
These are design choices, not facts from the assignment.
- Transition model: stochastic and configurable. With probability p_intended
  the robot moves as chosen; otherwise it slips to one of the two perpendicular
  directions with equal probability. Default p_intended = 0.8 (0.8/0.1/0.1).
- Terminal-state rules: separate EXIT action. Entering (3,1) or (3,3) is an
  ordinary move (living reward, episode continues). In a terminal the only
  legal action is EXIT, which pays -1 / +10 and ends the episode.
- Invalid action behavior: bumping a wall/edge = stay in place, living reward -0.04.
  This also applies when a stochastic slip sends the robot into a wall or
  edge: it stays in place and receives the living reward -0.04.
- Episode step cap: the EXIT action counts toward the 100-step limit. An
  episode that hits the cap is truncated, not terminated, so its final
  Q-update still bootstraps from the next state.
- Training: epsilon fixed at 0.1 (no decay), 5000 episodes, max 100 steps per
  episode, Q initialized to 0, every episode starts at (0,0), fixed seed.
- Hyperparameter values unchanged: -0.04, gamma 0.9, alpha 0.1, epsilon 0.1.
