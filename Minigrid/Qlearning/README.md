<h1>MiniGrid Environment - Q-learning Agent</h1>


<h2>Introduction</h2>
    <p>This project implements a Q-learning agent to solve various environments in MiniGrid, a minimalistic gridworld package for OpenAI Gym. The agent learns the optimal policy through repeated interactions with the environment using the Q-learning algorithm, an off-policy temporal-difference learning method.</p>

<h2>Environment Description</h2>
    <p>MiniGrid is a simple, lightweight environment for fast prototyping of reinforcement learning algorithms. It features:</p>
    <ul>
        <li>A grid-world environment with various tasks</li>
        <li>Partially observable states (agent's view is limited)</li>
        <li>Simple action space: turn left, turn right, move forward, pick up, drop, toggle, done</li>
        <li>Customizable grid size and task complexity</li>
    </ul>

 <p>Example environments include:</p>
    <ul>
        <li><strong>Empty:</strong> Navigate to a goal in an empty room</li>
        <li><strong>FourRooms:</strong> Navigate through four connected rooms to reach a goal</li>
        <li><strong>DoorKey:</strong> Collect a key to unlock a door and reach the goal</li>
    </ul>

 <h2>Q-learning Approach</h2>
    <p>Q-learning is an off-policy reinforcement learning algorithm that learns the optimal action-value function regardless of the policy being followed.</p>

 <h3>Algorithm Overview</h3>
    <pre><code>
Initialize Q(s,a) arbitrarily for all states s and actions a
For each episode:
    Initialize S
    For each step of episode:
        Choose A from S using policy derived from Q (e.g., ε-greedy)
        Take action A, observe R, S'
        Q(S,A) ← Q(S,A) + α[R + γ max_a Q(S',a) - Q(S,A)]
        S ← S'
    Until S is terminal
    </code></pre>

   <p>Where:</p>
    <ul>
        <li><strong>α:</strong> Learning rate</li>
        <li><strong>γ:</strong> Discount factor</li>
        <li><strong>ε:</strong> Exploration rate (for ε-greedy policy)</li>
    </ul>

   <h3>Exploration Strategies</h3>

   <h4>ε-greedy</h4>
    <ul>
        <li>With probability ε, choose a random action</li>
        <li>With probability 1-ε, choose the action with the highest Q-value</li>
    </ul>

  <h4>Softmax Exploration</h4>
    <p>Choose actions based on their relative Q-values. The probability of choosing action <em>a</em> in state <em>s</em> is:</p>
    <pre><code>P(a|s) = exp(Q(s,a)/τ) / Σ_b exp(Q(s,b)/τ)</code></pre>
    <p>Where τ is the temperature parameter controlling exploration.</p>

   <h4>Upper Confidence Bound (UCB)</h4>
    <p>Choose the action that maximizes:</p>
    <pre><code>Q(s,a) + c * sqrt(log(t) / N(s,a))</code></pre>
    <ul>
        <li><strong>N(s,a):</strong> The number of times action <em>a</em> has been taken in state <em>s</em></li>
        <li><strong>t:</strong> The total number of time steps</li>
        <li><strong>c:</strong> An exploration parameter</li>
    </ul>

   <h2>Requirements</h2>
    <ul>
        <li>Python 3.7+</li>
        <li>OpenAI Gym</li>
        <li>MiniGrid</li>
        <li>NumPy</li>
        <li>Matplotlib (for visualization)</li>
    </ul>

<h2>Installation</h2>
    <pre><code>pip install gym minigrid numpy matplotlib</code></pre>
