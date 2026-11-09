# CS440 Vacuum Robot

## Objective
Investigate and implement the 4 x 4 environment for
a vacuum robot, and implement Q-learning for the reinforcement learning of the vacuum robot.


Read @context/vacuum-environment.md
before investigating the vacuum robot.

Use isolated subagents for independent
investigations.

## Subagent Rules
- Delegate environment analysis to environment-agent.
- Delegate transition and reward analysis to transition-agent.
- Delegate validation to validation-agent.
- Each agent must investigate independently.
- Do not assume missing transition probabilities.
- Report assumptions separately from confirmed facts.
