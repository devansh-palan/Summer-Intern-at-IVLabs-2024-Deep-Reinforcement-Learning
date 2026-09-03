# Deep Reinforcement Learning — Summer Internship @ IVLabs (2024)

Implementations of classical and deep reinforcement learning algorithms, built and trained from scratch during my summer research internship at **IVLabs**. The work progresses from tabular methods on toy environments to policy-gradient deep RL in a 3D game engine — with experiments comparing convergence, stability, and sample efficiency at each stage.

| Environment | Algorithms |
|---|---|
| FrozenLake (Gym) | Value Iteration, Policy Iteration, Monte Carlo, SARSA(λ) |
| MiniGrid | Monte Carlo, SARSA(λ), Q-learning |
| ViZDoom | DQN, PPO |

---

## Task 1 — FrozenLake: Dynamic Programming

<img src="https://camo.githubusercontent.com/2ec3bee2bceafb626a446a0320eefedd658a2b4dae593c82754f087ef5b83795/68747470733a2f2f696d6775722e636f6d2f423575793361492e676966" height="300" width="300" alt="FrozenLake agent">

**Objective:** navigate a slippery frozen grid to the goal while avoiding holes.

- **Value Iteration** — iteratively backs up state values with the Bellman Optimality Equation until convergence, then extracts the greedy policy.
- **Policy Iteration** — alternates policy evaluation (computing the value function under the current policy) with greedy policy improvement.

**Findings:** with access to the full transition model, dynamic programming converged quickly to the optimal policy on the deterministic map. Model-free methods (Monte Carlo, SARSA(λ)) needed far more exploration and hyperparameter tuning to stay competitive on the stochastic version.

<img src="episode_vs_reward_frozen_lake.webp" width="400" alt="Episode vs reward"> <img src="stepsize_vs_episode_frozen_lake.webp" width="400" alt="Step size vs episode">

## Task 2 — MiniGrid: Model-Free Tabular Methods

<img src="https://camo.githubusercontent.com/4c91fc8f5469c3a6bd9fad7c04c2f6297b369cf0db200f26f7e42f31bfd83093/68747470733a2f2f692e696d6775722e636f6d2f346c43774c38672e676966" height="300" width="300" alt="MiniGrid agent">

**Objective:** learn to reach the goal in a partially observable grid world, without a model of the environment.

### Monte Carlo control
Collects full-episode returns, averages them per state–action pair (first-visit), and improves an ε-greedy policy. Worked well on small grids but needed many episodes to converge.

### SARSA(λ)
On-policy TD learning with **eligibility traces**, which propagate credit back through recent state–action pairs. This gave the most stable learning under partial observability — at the cost of careful λ tuning.

### Q-learning
Off-policy TD control that bootstraps directly on the max Q-value. Converged fastest in fully observable regions but struggled where long action sequences mattered.

**Takeaway:** the three methods trade off convergence speed against stability — Q-learning learns fastest when the state is fully visible, while SARSA(λ)'s traces handle partial observability more gracefully.

## Task 3 — ViZDoom: Deep RL (DQN & PPO)

<img src="https://github.com/devansh-palan/Summer-Intern-at-IVLabs-2024-Deep-Reinforcement-Learning/blob/main/clideo_editor_68da857852f4409dafa7d51cf4cb5545%20(1)%20(1).gif?raw=true" width="500" alt="ViZDoom PPO agent">

**Objective:** train agents to navigate a 3D environment, engage enemies, and collect resources directly from raw game frames.

**PPO implementation highlights:**

- **Actor–critic architecture** — CNN-based policy and value networks processing stacked game frames
- **Advantage estimation** — advantages computed from observed returns vs. value estimates to drive policy updates
- **Clipped surrogate objective** — probability ratios are clipped each update, keeping the new policy close to the old one for stable learning

**Findings:** PPO learned robust behaviour noticeably faster than DQN, handling the large visual state space and delivering better sample efficiency across combat and resource-collection scenarios.

---

## Repository Structure

```
├── FrozenLake/   # DP, Monte Carlo, SARSA(λ) notebooks & training curves
├── Minigrid/     # MC, SARSA(λ), Q-learning implementations
└── VizDoom/      # DQN and PPO agents
```
