<h1>Frozen Lake Dynamic Programming Agent</h1>
    <p>This project implements a Dynamic Programming (DP) agent to solve the Frozen Lake environment from OpenAI Gym. The agent learns the optimal policy to navigate through the slippery grid world and reach the goal state while avoiding holes.</p>

<img src="https://camo.githubusercontent.com/2ec3bee2bceafb626a446a0320eefedd658a2b4dae593c82754f087ef5b83795/68747470733a2f2f696d6775722e636f6d2f423575793361492e676966" height=300px width=300px>
    

<h2>Environment Description</h2>
    <a href="https://gymnasium.farama.org/environments/toy_text/frozen_lake/#frozen-lake" >FrozenLake Documentation</a>
    

<p><strong>Frozen Lake</strong> is a grid-world environment where:</p>
    <ul>
        <li>The agent starts in the top-left corner (S) and must reach the goal (G) in the bottom-right corner.</li>
        <li>The grid contains frozen tiles (F) and holes (H).</li>
        <li>If the agent falls in a hole, it receives a reward of 0 and the episode ends.</li>
        <li>Reaching the goal provides a reward of 1.</li>
        <li>The environment is slippery, meaning the agent's actions may not always result in the intended movement.</li>
    </ul>

<h3>Example 4x4 Grid:</h3>
    <pre><code>
    SFFF
    FHFH
    FFFH
    HFFG
    </code></pre>

<h2>Dynamic Programming Approach</h2>
    <p>We implement two main DP algorithms to solve this environment:</p>

<h2>Policy Iteration</h2>
    <p>Policy Iteration alternates between policy evaluation and policy improvement steps to converge to the optimal policy. Here's a detailed breakdown of the algorithm:</p>

<h3>Initialization:</h3>
    <ul>
        <li>Initialize a random policy π</li>
        <li>Initialize the value function V(s) = 0 for all states s</li>
    </ul>

<h3>Policy Evaluation:</h3>
    <p>Repeat until convergence:</p>
    <ul>
        <li>For each state s:</li>
        <pre><code>v = V(s)
        V(s) = Σ_a π(a|s) * Σ_s' P(s'|s,a) * [R(s,a,s') + γ * V(s')]</code></pre>
        <li>If max|v - V(s)| &lt; θ (small threshold), stop</li>
    </ul>

<p>Where:</p>
    <ul>
        <li>π(a|s) is the probability of taking action a in state s under policy π</li>
        <li>P(s'|s,a) is the transition probability from state s to s' given action a</li>
        <li>R(s,a,s') is the reward for transitioning from s to s' with action a</li>
        <li>γ (gamma) is the discount factor</li>
        <li>θ is a small threshold for determining convergence</li>
    </ul>

 <h3>Policy Improvement:</h3>
    <pre><code>policy_stable = True
For each state s:
    old_action = π(s)
    π(s) = argmax_a Σ_s' P(s'|s,a) * [R(s,a,s') + γ * V(s')]
    If old_action ≠ π(s), then policy_stable = False</code></pre>
    <h3>Convergence Check:</h3>
    <ul>
        <li>If policy_stable, stop and return π as the optimal policy</li>
        <li>Else, go back to step 2 (Policy Evaluation)</li>
    </ul>
    <p>Policy Iteration guarantees convergence to the optimal policy. The algorithm terminates when the policy improvement step no longer changes the policy, indicating that we have found the optimal policy.</p>

<h2>Value Iteration</h2>
    <p>Value Iteration combines policy evaluation and improvement into a single step, iteratively computing the optimal value function. Here's a detailed explanation of the algorithm:</p>
    <h3>Initialization:</h3>
    <ul>
        <li>Initialize V(s) = 0 for all states s</li>
        <li>Choose a small threshold θ > 0</li>
    </ul>
    <h3>Value Iteration:</h3>
    <p>Repeat until convergence:</p>
    <pre><code>Δ = 0
For each state s:
    v = V(s)
    V(s) = max_a Σ_s' P(s'|s,a) * [R(s,a,s') + γ * V(s')]
    Δ = max(Δ, |v - V(s)|)

If Δ &lt; θ, stop iteration</code></pre>
    <h3>Policy Extraction:</h3>
    <pre><code>For each state s:
    π(s) = argmax_a Σ_s' P(s'|s,a) * [R(s,a,s') + γ * V(s')]</code></pre>
    <p>Where:</p>
    <ul>
        <li>max_a denotes the maximum over all actions a</li>
        <li>Other symbols have the same meaning as in Policy Iteration</li>
    </ul>
    <p>Value Iteration converges to the optimal value function V*, from which we can extract the optimal policy. The algorithm is generally faster than Policy Iteration as it combines the policy evaluation and improvement steps.</p>



<h2>Requirements</h2>
    <ul>
        <li>Python 3.7+</li>
        <li>OpenAI Gym</li>
        <li>NumPy</li>
        <li>Matplotlib (for visualization)</li>
    </ul>

<h2>Installation</h2>
    <div class="code-block">
        <pre><code>pip install gym numpy matplotlib</code></pre>
    </div>


<p>You can modify the following parameters in the script:</p>
    <ul>
        <li><code>env_name</code>: 'FrozenLake-v1' (4x4 grid) or 'FrozenLake8x8-v1' (8x8 grid)</li>
        <li><code>is_slippery</code>: True (default) or False</li>
        <li><code>algorithm</code>: 'policy_iteration' or 'value_iteration'</li>
    </ul>

<img src="https://raw.githubusercontent.com/devansh-palan/Summer-Intern-at-IVLabs-2024-Deep-Reinforcement-Learning/refs/heads/main/episode_vs_reward_frozen_lake.webp">

<img src="https://raw.githubusercontent.com/devansh-palan/Summer-Intern-at-IVLabs-2024-Deep-Reinforcement-Learning/refs/heads/main/stepsize_vs_episode_frozen_lake.webp" width="600px">

