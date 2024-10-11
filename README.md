 <h1>Summer Intern at IVLabs 2024 - Deep Reinforcement Learning</h1>

<h2>Description</h2>
<p>This repository contains the work I completed during my summer internship focused on Deep Reinforcement Learning (DRL). Over the course of the internship, I implemented, trained, and evaluated several reinforcement learning algorithms in various environments. My goal was to understand how different algorithms performed in various settings, experiment with hyperparameters, and gain hands-on experience in building and training agents in both classical and complex environments.</p>

<h2>Task 1 - Training an agent in the FrozenLake Environment by Dynamic Programming</h2>
                     <img src="https://gymnasium.farama.org/_images/frozen_lake.gif" height=300px width=300px>
   <ul>
        <li><strong>Algorithm:</strong> Dynamic Programming</li>
        <li><strong>Environment:</strong> FrozenLake (from OpenAI Gym)</li>
        <li><strong>Objective:</strong> To navigate a slippery frozen grid and reach the goal while avoiding holes in the ice.</li>
        <li><strong>Implementation:</strong>
            <ul>
                <li><strong>Value Iteration:</strong> Used to iteratively update the value function based on the Bellman Optimality Equation. This algorithm helps find the optimal policy by backing up the state values.</li>
                <li><strong>Policy Iteration:</strong> Involves two steps: policy evaluation (calculating the value function under the current policy) and policy improvement (greedily improving the policy).</li>
            </ul>
        </li>
        <li><strong>Results:</strong> The Dynamic Programming methods converged quickly and provided the optimal solution for the deterministic version of the FrozenLake environment. In contrast, the Monte Carlo and SARSA(λ) methods, while more suitable for model-free scenarios, required more exploration and experimentation with hyperparameters to achieve a competitive solution in the stochastic environment.</li>
    </ul>

   <h2>Task 2 - Training an agent in the MiniGrid Environment</h2>

<img src="https://minigrid.farama.org/_images/EmptyEnv.gif" height=300px width=300px>
  <h3>1. Monte Carlo Policy</h3>
    <ul>
        <li><strong>Algorithm:</strong> Monte Carlo Policy</li>
        <li><strong>Environment:</strong> MiniGrid (a partially observable grid world)</li>
        <li><strong>Objective:</strong> To train an agent to navigate a grid world and reach the goal while avoiding obstacles and following optimal policies.</li>
        <li><strong>Implementation:</strong> 
            <ul>
                <li>The agent collects state-action-return triplets for each episode it experiences in MiniGrid.</li>
                <li>Returns are averaged over multiple visits (first-visit approach), and the policy is improved gradually using an epsilon-greedy strategy to ensure exploration.</li>
            </ul>
        </li>
        <li><strong>Results:</strong> The Monte Carlo policy performed well on smaller grid configurations but required more episodes to converge compared to Q-learning.</li>
    </ul>

   <h3>2. Sarsa Lambda</h3>
    <ul>
        <li><strong>Algorithm:</strong> Sarsa Lambda</li>
        <li><strong>Environment:</strong> MiniGrid (a partially observable grid world)</li>
        <li><strong>Objective:</strong> To train an agent to navigate a grid world and reach the goal while avoiding obstacles and following optimal policies.</li>
        <li><strong>Implementation:</strong>
            <ul>
                <li><strong>Eligibility Traces:</strong> SARSA(λ) combines the benefits of on-policy learning (SARSA) with eligibility traces to assign credit to previous actions, even if they occurred several steps back. This allows the agent to better learn from long sequences of actions.</li>
                <li><strong>Exploration Strategy:</strong> An epsilon-greedy policy was used to encourage exploration while SARSA(λ) learned the Q-values for each state-action pair.</li>
                <li><strong>Trace Decay:</strong> The λ parameter controls the decay of eligibility traces over time, balancing between more recent and older state-action pairs.</li>
            </ul>
        </li>
        <li><strong>Results:</strong> SARSA(λ) provided more stable learning compared to Q-learning, especially in partially observable environments like MiniGrid. The eligibility traces helped propagate rewards backward more effectively, enabling faster learning in some scenarios. However, tuning the λ parameter was critical to achieving optimal performance.</li>
    </ul>

  <h3>3. Q-learning</h3>
    <ul>
        <li><strong>Algorithm:</strong> Q-learning</li>
        <li><strong>Environment:</strong> MiniGrid (a partially observable grid world)</li>
        <li><strong>Objective:</strong> To train an agent to navigate a grid world and reach the goal while avoiding obstacles by learning an optimal policy.</li>
        <li><strong>Implementation:</strong>
            <ul>
                <li><strong>Q-Value Updates:</strong> Q-learning is an off-policy algorithm that updates the Q-values for each state-action pair using the Bellman equation. It directly learns the optimal action-value function by maximizing the expected future reward.</li>
                <li><strong>Exploration Strategy:</strong> An epsilon-greedy policy was used to balance exploration and exploitation. During training, the agent initially takes random actions (exploration), but gradually shifts to taking actions that maximize the learned Q-values (exploitation).</li>
            </ul>
        </li>
        <li><strong>Results:</strong> Q-learning was effective in training an agent to solve tasks in the MiniGrid environment. The agent successfully learned to navigate towards the goal while avoiding obstacles, even in complex grid environments. Compared to SARSA(λ), Q-learning showed more rapid convergence in fully observable areas but faced challenges in partially observable environments where it couldn't rely on long sequences of actions to learn.</li>
    </ul>

   <h2>Task 3 - Training an agent in the ViZDoom Environment</h2>

   <img src="https://raw.githubusercontent.com/Farama-Foundation/ViZDoom/master/docs/_static/img/vizdoom-demo.gif" >
    <ul>
        <li><strong>Algorithm:</strong> Deep Q-Network (DQN)</li>
        <li><strong>Environment:</strong> ViZDoom (a 3D first-person shooter environment)</li>
        <li><strong>Objective:</strong> To train agents to navigate a complex 3D environment, eliminate enemies, collect resources, and survive using two popular reinforcement learning algorithms: DQN and PPO.</li>
        <li><strong>Implementation:</strong>
            <ul>
                <li><strong>Neural Network Architecture:</strong> DQN uses a CNN to process game frames and predict Q-values for each possible action.</li>
                <li><strong>Advantage Function:</strong> PPO uses a combination of the reward and the value function to compute the advantage for updating the policy.</li>
                <li><strong>Clipping:</strong> The policy update is clipped to ensure that the new policy does not deviate too much from the old policy.</li>
                <li><strong>Training:</strong> The agent collects experiences by interacting with the environment, then updates the policy and value networks based on the collected data.</li>
            </ul>
        </li>
        <li><strong>Results:</strong>
            <ul>
                <li><strong>DQN:</strong> Typically, DQN performs well in discrete action spaces and learns stable policies after sufficient training. It may take longer to converge due to the high-dimensional state space but tends to perform well when trained on simpler tasks (e.g., enemy elimination or navigation).</li>
            </ul>
        </li>
    </ul>
