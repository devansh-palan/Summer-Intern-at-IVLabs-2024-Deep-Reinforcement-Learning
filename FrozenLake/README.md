<h1>Frozen Lake DP Agent</h1>
    <p>This project implements a Dynamic Programming (DP) agent to solve the Frozen Lake environment from OpenAI Gym. The agent learns the optimal policy to navigate through the slippery grid world and reach the goal state while avoiding holes.</p>

<h2>Environment Description</h2>
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

<h3>Policy Iteration</h3>
    <p>
    Policy Iteration alternates between policy evaluation and policy improvement steps to converge to the optimal policy. Here's a detailed breakdown of the algorithm:

Initialization:

Initialize a random policy π
Initialize the value function V(s) = 0 for all states s


Policy Evaluation:

Repeat until convergence:

For each state s:

v = V(s)
V(s) = Σ_a π(a|s) * Σ_s' P(s'|s,a) * [R(s,a,s') + γ * V(s')]


If max|v - V(s)| < θ (small threshold), stop



Where:

π(a|s) is the probability of taking action a in state s under policy π
P(s'|s,a) is the transition probability from state s to s' given action a
R(s,a,s') is the reward for transitioning from s to s' with action a
γ (gamma) is the discount factor
θ is a small threshold for determining convergence


Policy Improvement:

policy_stable = True
For each state s:

old_action = π(s)
π(s) = argmax_a Σ_s' P(s'|s,a) * [R(s,a,s') + γ * V(s')]
If old_action ≠ π(s), then policy_stable = False




Convergence Check:

If policy_stable, stop and return π as the optimal policy
Else, go back to step 2 (Policy Evaluation)



Policy Iteration guarantees convergence to the optimal policy. The algorithm terminates when the policy improvement step no longer changes the policy, indicating that we have found the optimal policy.</p>
    <h3>Value Iteration</h3>
    <ol>
        <li>Initialize the value function arbitrarily.</li>
        <li>Update the value function using the Bellman optimality equation.</li>
        <li>Repeat step 2 until convergence.</li>
        <li>Extract the optimal policy from the final value function.</li>
    </ol>

<p>Both algorithms compute the optimal policy for the agent to follow.</p>

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

<h2>Usage</h2>
    <p>Run the main script to train the agent and see its performance:</p>
    <div class="code-block">
        <pre><code>python frozen_lake_dp.py</code></pre>
    </div>

<p>You can modify the following parameters in the script:</p>
    <ul>
        <li><code>env_name</code>: 'FrozenLake-v1' (4x4 grid) or 'FrozenLake8x8-v1' (8x8 grid)</li>
        <li><code>is_slippery</code>: True (default) or False</li>
        <li><code>algorithm</code>: 'policy_iteration' or 'value_iteration'</li>
    </ul>

<h2>File Structure</h2>
    <ul>
        <li><code>frozen_lake_dp.py</code>: Main script containing the DP algorithms and training loop</li>
        <li><code>utils.py</code>: Utility functions for rendering and plotting</li>
        <li><code>requirements.txt</code>: List of required Python packages</li>
    </ul>

<h2>Implementation Details</h2>
    <ul>
        <li><strong>State-Value Function (V)</strong>: Represents the expected return starting from a state.</li>
        <li><strong>Action-Value Function (Q)</strong>: Represents the expected return starting from a state and taking a specific action.</li>
        <li><strong>Policy</strong>: A mapping from states to actions.</li>
        <li><strong>Discount Factor (gamma)</strong>: Balances immediate and future rewards (default: 0.99).</li>
        <li><strong>Convergence Threshold</strong>: Determines when to stop iterating (default: 1e-8).</li>
    </ul>

<p>The implementation uses NumPy for efficient matrix operations and OpenAI Gym for environment interactions.</p>

<h2>Results and Visualization</h2>
    <p>The script outputs:</p>
    <ul>
        <li>Optimal value function as a heatmap</li>
        <li>Optimal policy as arrows on the grid</li>
        <li>Learning curve showing improvement over iterations</li>
        <li>Average reward and success rate over 1000 episodes</li>
    </ul>

 <h2>Troubleshooting</h2>
    <p>Common issues and solutions:</p>
    <ul>
        <li><strong>"Module not found" error</strong>: Ensure all required packages are installed.</li>
        <li><strong>Poor performance</strong>: Try adjusting the discount factor or increasing the number of iterations.</li>
        <li><strong>Slow convergence</strong>: Consider using value iteration instead of policy iteration for faster results.</li>
    </ul>