import os

import pytest

import q_learning
from q_learning import QLearningAgent, train
from vacuum_env import EXIT, MOVE_ACTIONS, RIGHT, VacuumEnv


def test_hyperparameters_match_spec():
    assert (q_learning.GAMMA, q_learning.ALPHA, q_learning.EPSILON) == (0.9, 0.1, 0.1)
    assert (q_learning.EPISODES, q_learning.MAX_STEPS) == (5000, 100)


def test_update_rule_single_step():
    agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.0)
    agent.q[((0, 1), RIGHT)] = 2.0
    agent.update((0, 0), RIGHT, -0.04, (0, 1), False, MOVE_ACTIONS)
    # 0 + 0.1 * (-0.04 + 0.9 * 2.0 - 0)
    assert agent.q[((0, 0), RIGHT)] == pytest.approx(0.176)


def test_update_rule_terminal_no_bootstrap():
    agent = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.0)
    agent.update((3, 3), EXIT, 10.0, None, True, ())
    assert agent.q[((3, 3), EXIT)] == pytest.approx(1.0)


def test_agent_does_not_read_reward_table():
    path = os.path.join(os.path.dirname(__file__), "..", "q_learning.py")
    with open(path) as f:
        assert "_terminal_rewards" not in f.read()


def _greedy_rollout(env, agent, max_steps=20):
    s, path = env.reset(), []
    for _ in range(max_steps):
        path.append(s)
        if env.is_terminal(s):
            return path
        s, _, _ = env.step(s, agent.greedy_action(s, env.legal_actions(s)))
    return path


def test_learns_shortest_path_deterministic():
    env = VacuumEnv(p_intended=1.0, seed=0)
    agent = QLearningAgent(seed=1)
    train(env, agent)
    path = _greedy_rollout(env, agent)
    assert path[-1] == (3, 3)
    assert len(path) == 7  # 6 moves from (0,0) to (3,3)
    assert agent.q[((3, 3), EXIT)] == pytest.approx(10.0, abs=0.01)


def test_learns_to_reach_goal_stochastic():
    env = VacuumEnv(p_intended=0.8, seed=0)
    agent = QLearningAgent(seed=1)
    train(env, agent)
    deterministic = VacuumEnv(p_intended=1.0)
    assert _greedy_rollout(deterministic, agent)[-1] == (3, 3)
    assert agent.value((0, 0), MOVE_ACTIONS) > 0
