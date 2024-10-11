<h1>MiniGrid Environment - SARSA(λ) Agent</h1>
    
    

<h2>Introduction</h2>
    <p>This project implements a SARSA(λ) agent to solve various environments in MiniGrid, a minimalistic gridworld package for OpenAI Gym. The agent learns the optimal policy through repeated interactions with the environment using the SARSA(λ) algorithm, which combines temporal-difference learning with eligibility traces.</p>
    <h2>Environment Description</h2>

<a href="https://minigrid.farama.org/environments/minigrid/EmptyEnv/">Documentation</a>
    <p>MiniGrid is a simple, lightweight environment for fast prototyping of reinforcement learning algorithms. It features:</p>
    <ul>
        <li>A grid-world environment with various tasks</li>
        <li>Partially observable states (agent's view is limited)</li>
        <li>Simple action space: turn left, turn right, move forward, pick up, drop, toggle, done</li>
        <li>Customizable grid size and task complexity</li>
    </ul>
    <p>Example environments include:</p>
    <ul>
        <li>Empty: Navigate to a goal in an empty room</li>
        <li>FourRooms: Navigate through four connected rooms to reach a goal</li>
        <li>DoorKey: Collect a key to unlock a door and reach the goal</li>
    </ul>
    <h2>SARSA(λ) Approach</h2>
    <p>SARSA(λ) is an on-policy temporal-difference learning algorithm that uses eligibility traces to propagate reward information more efficiently through the state-action space.</p>
    <h3>Algorithm Overview</h3>
    <h4>Initialize:</h4>
    <ul>
        <li>Q(s,a) arbitrarily for all states s and actions a</li>
        <li>e(s,a) = 0 for all states s and actions a (eligibility traces)</li>
    </ul>
    <h4>For each episode:</h4>
    <ol>
        <li>Initialize S</li>
        <li>Choose A from S using policy derived from Q (e.g., ε-greedy)</li>
        <li>For each step of episode:</li>
        <ol>
            <li>Take action A, observe R, S'</li>
            <li>Choose A' from S' using policy derived from Q</li>
            <li>δ = R + γQ(S',A') - Q(S,A)  # TD-error</li>
            <li>e(S,A) = e(S,A) + 1  # Accumulating traces</li>
            <li>For all s, a:</li>
            <pre><code>Q(s,a) = Q(s,a) + αδe(s,a)
e(s,a) = γλe(s,a)</code></pre>
            <li>S = S'; A = A'</li>
        </ol>
        <li>Until S is terminal</li>
    </ol>
    <p>Where:</p>
    <ul>
        <li>α: Learning rate</li>
        <li>γ: Discount factor</li>
        <li>λ: Trace decay parameter</li>
        <li>ε: Exploration rate (for ε-greedy policy)</li>
    </ul>
    <h3>Eligibility Traces</h3>
    <p>Eligibility traces provide a mechanism for temporal credit assignment. They help to:</p>
    <ul>
        <li>Speed up learning by updating multiple state-action pairs per step</li>
        <li>Bridge delays between actions and resulting rewards</li>
        <li>Provide a continuous spectrum between Monte Carlo and TD(0) methods</li>
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


<img src="https://media.discordapp.net/attachments/1279373242267602967/1294274992007282709/Copy_of_SARSA_stepVs_Episode2.png?ex=670a6b04&is=67091984&hm=d2ad98d8cc5632b3722e3ab2f750526d1906f62d3bc718640b8f9f56e357694b&=&format=webp&quality=lossless&width=713&height=540">
<img src="https://media.discordapp.net/attachments/1279373242267602967/1294274991721812031/Copy_of_SARSA_reward_Vs_episode2.png?ex=670a6b04&is=67091984&hm=6bad108246726684f774a44ec8db22a162731d61ae7d109710c598706fe368e8&=&format=webp&quality=lossless&width=722&height=540">