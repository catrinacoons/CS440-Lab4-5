"""Grid and transition tests (grid-validation + transition-testing skills).

Deviation from the transition-testing skill, confirmed by the user:
terminal rewards use a separate EXIT action, so entering a terminal pays the
living reward with done=False, and EXIT pays +10 / -1 with done=True.
"""

from collections import Counter
from collections import deque

import pytest

from vacuum_env import DOWN, EXIT, LEFT, MOVE_ACTIONS, RIGHT, UP, VacuumEnv

LIVING = -0.04


@pytest.fixture
def env():
    return VacuumEnv(p_intended=1.0, seed=0)  # deterministic for exact checks


# ---- grid validation ----------------------------------------------------

def test_grid_size_and_start(env):
    assert (env.ROWS, env.COLS) == (4, 4)
    assert env.reset() == (0, 0)


def test_wall_and_terminals(env):
    assert env.WALLS == {(1, 1)}
    assert (1, 1) not in env.states()
    assert len(env.states()) == 15
    terminals = [s for s in env.states() if env.is_terminal(s)]
    assert sorted(terminals) == [(3, 1), (3, 3)]


def test_terminals_only_allow_exit(env):
    for s in [(3, 1), (3, 3)]:
        assert env.legal_actions(s) == (EXIT,)
        with pytest.raises(ValueError):
            env.step(s, UP)


def test_path_from_start_to_goal(env):
    seen, queue = {env.START}, deque([env.START])
    while queue:
        s = queue.popleft()
        if env.is_terminal(s):
            continue
        for a in MOVE_ACTIONS:
            nxt, _, _ = env.step(s, a)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    assert (3, 3) in seen


# ---- transitions --------------------------------------------------------

@pytest.mark.parametrize("action, expected", [(RIGHT, (0, 1)), (DOWN, (1, 0))])
def test_normal_moves(env, action, expected):
    assert env.step((0, 0), action) == (expected, LIVING, False)


@pytest.mark.parametrize("state, action", [
    ((0, 0), UP), ((0, 0), LEFT), ((0, 3), UP), ((0, 3), RIGHT),
    ((2, 0), LEFT), ((3, 0), DOWN), ((3, 2), DOWN), ((2, 3), RIGHT),
])
def test_edge_bumps_stay(env, state, action):
    assert env.step(state, action) == (state, LIVING, False)


@pytest.mark.parametrize("state, action", [
    ((0, 1), DOWN), ((1, 0), RIGHT), ((1, 2), LEFT), ((2, 1), UP),
])
def test_wall_bumps_stay(env, state, action):
    assert env.step(state, action) == (state, LIVING, False)


def test_wall_never_entered_under_noise():
    env = VacuumEnv(p_intended=0.8, seed=1)
    for _ in range(2000):
        for s in [(0, 1), (1, 0), (1, 2), (2, 1)]:
            for a in MOVE_ACTIONS:
                assert env.step(s, a)[0] != (1, 1)


def test_entering_terminal_is_ordinary_move(env):
    assert env.step((2, 3), DOWN) == ((3, 3), LIVING, False)
    assert env.step((2, 1), DOWN) == ((3, 1), LIVING, False)


def test_exit_rewards(env):
    assert env.step((3, 3), EXIT) == (None, 10.0, True)
    assert env.step((3, 1), EXIT) == (None, -1.0, True)


def test_interface_returns_three_values(env):
    result = env.step((0, 0), RIGHT)
    assert isinstance(result, tuple) and len(result) == 3


def test_deterministic_when_p_intended_is_one(env):
    outcomes = {env.step((2, 2), RIGHT) for _ in range(200)}
    assert outcomes == {((2, 3), LIVING, False)}


def test_stochastic_slip_distribution():
    env = VacuumEnv(p_intended=0.8, seed=42)
    n = 20000
    counts = Counter(env.step((2, 2), UP)[0] for _ in range(n))
    # up -> (1,2) 0.8; slip left -> (2,1) 0.1; slip right -> (2,3) 0.1
    assert set(counts) == {(1, 2), (2, 1), (2, 3)}
    assert counts[(1, 2)] / n == pytest.approx(0.8, abs=0.02)
    assert counts[(2, 1)] / n == pytest.approx(0.1, abs=0.02)
    assert counts[(2, 3)] / n == pytest.approx(0.1, abs=0.02)


def test_invalid_p_intended_rejected():
    with pytest.raises(ValueError):
        VacuumEnv(p_intended=1.5)
