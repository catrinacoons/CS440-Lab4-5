# CS440-Lab4-Group-11
Student Repository for configuring the Context Engineering Strategies for AI for the CS440-Lab 4 assignment


## Write (Persistent Memory Architecture) Overview:
Context Information is saved outside the window, in files, so the context persists. The AI forgets everything when a session ends, so this ensures that the AI will re-read the context files each time the session is started anew, so it is re-given the necessary information.   
There are 3 memory types: 
1. User memory - Saved Personal preferences of the user; is not shared
2. Project Memory - Overall Architecture, code standards, set rules for the project, shared with all collaborators
3. Dynamic Imports - Extra files loaded as needed, shared depending on import location

## Sub-Agent Overview:
The problem is separated by roles, in which the sub-agents handle them based on their function, with a managerial agent handling their delegation.
The sub-agents are:
1. environment-agent: identifies valid states, robot actions, and boundaries.
2. reward-agent: identifies reward values, terminal conditions, etc.
3. transition-agent: identifies transition rules, reward values, and asks questions.

## Skills Overview:
The skills and subagents are working together with each skill matching to a sub-agent, ie the grid-validation skill is matched to the environment-agent. Sub-agents handle the separate responsibilities, while the skills provide reusable instructions the agents can follow. 
It will be connected by the manager agent, which delegates the tasks.

## Directory Structure
```
CLAUDE.md  
README.md  
.claude/
├──agents/
  ├──environment-agent.md
  ├──reward-agent.md
  ├──transition-agent.md
├──skills/
  ├──grid-validation
    ├──SKILL.md
  ├──reward-design
    ├──SKILL.md
  ├──transition-testing
    ├──SKILL.md
├──settings.json  
context/  
├──api-context.md  
├──auth-system.md  
├──database-context.md  
├──frontend-context.md  
├──payment-flow.md  
├──production-hotfix.md  
├──vacuum-environment.md
scripts/  
├──context-switcher.sh   
```
