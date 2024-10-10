# Summer-Intern-at-IVLabs-2024-Deep-Reinforcement-Learning
# Description

This repository contains the work I completed during my summer internship focused on Deep Reinforcement Learning (DRL). Over the course of the internship, I implemented, trained, and evaluated several reinforcement learning algorithms in various environments.
My goal was to understand how different algorithms performed in various settings, experiment with hyperparameters, and gain hands-on experience in building and training agents in both classical and complex environments.

# TASK 1 -Training an agent in the FrozenLake Environment by Dynamic Programming.

* Algorithm: Dynamic Programming 
* Environment: FrozenLake (from OpenAI Gym)
* Objective: To navigate a slippery frozen grid and reach the goal while avoiding holes in the ice.
* Implementation:
Implemented Value Iteration and Policy Iteration algorithms to solve the FrozenLake environment. These algorithms are based on planning methods using a model of the environment and iterating over state values or policies until convergence.
Value Iteration: Used to iteratively update the value function based on the Bellman Optimality Equation. This algorithm helps find the optimal policy by backing up the state values.
Policy Iteration: Involves two steps: policy evaluation (calculating value function under the current policy) and policy improvement (greedily improving the policy).
* Results: The Dynamic Programming methods converged quickly and provided the optimal solution for the deterministic version of the FrozenLake environment. In contrast, the Monte Carlo and SARSA(λ) methods, while more suitable for model-free scenarios, required more exploration and experimentation with hyperparameters to achieve a competitive solution in the stochastic environment.


# TASK 2-Training an agent in the MiniGrid Envrionment

# 1.MonteCarlo Policy
* Algorithm:  Monte Carlo Policy

* Environment: MiniGrid (a partially observable grid world)

* Objective: To train an agent to navigate a grid world and reach the goal while avoiding obstacles and following optimal policies.

* Implementation:
The agent collects state-action-return triplets for each episode it experiences in MiniGrid.
Returns are averaged over multiple visits (first-visit approach), and the policy is improved gradually using an epsilon-greedy strategy to ensure exploration.
This approach is slower to converge than Q-learning in some cases, but it provides an unbiased estimate of the action-value function, which can be useful in model-free environments like MiniGrid.

* Results: The Monte Carlo policy performed well on smaller grid configurations but required more episodes to converge compared to Q-learning.

# 2.Sarsa Lambda
* Algorithm:  Sarsa Lambda

* Environment: MiniGrid (a partially observable grid world)

* Objective: To train an agent to navigate a grid world and reach the goal while avoiding obstacles and following optimal policies.

* Implementation:
Eligibility Traces: SARSA(λ) combines the benefits of on-policy learning (SARSA) with eligibility traces to assign credit to previous actions, even if they occurred several steps back. This allows the agent to better learn from long sequences of actions.
Exploration Strategy: An epsilon-greedy policy was used to encourage exploration while SARSA(λ) learned the Q-values for each state-action pair.
Trace Decay: The λ parameter controls the decay of eligibility traces over time, balancing between more recent and older state-action pairs.
* Results: SARSA(λ) provided more stable learning compared to Q-learning, especially in partially observable environments like MiniGrid. The eligibility traces helped propagate rewards backward more effectively, enabling faster learning in some scenarios. However, tuning the λ parameter was critical to achieving optimal performance.


# 3.Q-learning








