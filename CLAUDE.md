# CS440 Vacuum Robot

## Objective
Investigate and implement the environment for
a 4x4 vacuum robot.

Q-learning is out of scope for this lab.

Read @context/vacuum-environment.md
before investigating the vacuum robot.

Also implement reward-agent

Use isolated subagents for independent
investigations.

Select values for the living reward, discount factor, learning rate, and epsilon. 

Do not implement Q-learning until requested.

## Subagent Rules
- Delegate environment analysis to environment-agent.
- Delegate transition and reward analysis to transition-agent.
- Each agent must investigate independently.
- Do not assume missing transition probabilities.
- Do not implement Q-learning.
- Report assumptions separately from confirmed facts.