<h1>MiniGrid Environment - Monte Carlo Agent</h1>


<h2 id="introduction">Introduction</h2>
    <p>This project implements a Monte Carlo agent to solve various environments in <strong>MiniGrid</strong>, a minimalistic gridworld package for OpenAI Gym. The agent learns the optimal policy through repeated interactions with the environment using Monte Carlo methods.</p>

<h2 id="environment-description">Environment Description</h2>

   <a href="https://minigrid.farama.org/environments/minigrid/EmptyEnv/">Documentation</a>
    <p>MiniGrid is a simple, lightweight environment for fast prototyping of reinforcement learning algorithms. It features:</p>
    <ul>
        <li>A grid-world environment with various tasks</li>
        <li>Partially observable states (agent's view is limited)</li>
        <li>Simple action space: turn left, turn right, move forward, pick up, drop, toggle, done</li>
        <li>Customizable grid size and task complexity</li>
    </ul>
    

 <h2 id="monte-carlo-approach">Monte Carlo Approach</h2>
    <p>We implement Monte Carlo methods for both prediction and control to solve MiniGrid environments:</p>

<h3 id="monte-carlo-prediction">Monte Carlo Prediction</h3>
    <p>Monte Carlo prediction is used to estimate the value function for a given policy:</p>
    <h4>Initialization:</h4>
    <ul>
        <li>Initialize V(s) arbitrarily for all states s</li>
        <li>Initialize Returns(s) as an empty list for all states s</li>
    </ul>

<h4>Episode Generation:</h4>
<p>Generate an episode following policy π: S₀, A₀, R₁, S₁, A₁, R₂, ..., Sₜ</p>

<h4>Value Estimation:</h4>
    <ul>
        <li>For each state Sₜ visited in the episode:</li>
        <pre><code>G ← Return from time step t
    Append G to Returns(Sₜ)
    V(Sₜ) ← average(Returns(Sₜ))</code></pre>
    </ul>

<h4>Repeat:</h4>
    <ul>
        <li>Go to step 2 and generate more episodes until convergence or a set number of episodes</li>
    </ul>

<h3 id="monte-carlo-control">Monte Carlo Control</h3>
    <p>Monte Carlo control aims to find the optimal policy through iterative improvement:</p>

<h4>Initialization:</h4>
    <ul>
        <li>Initialize Q(s,a) arbitrarily for all state-action pairs</li>
        <li>Initialize policy π arbitrarily</li>
        <li>Initialize Returns(s,a) as an empty list for all state-action pairs</li>
    </ul>
    <h4>Episode Generation:</h4>
    <p>Generate an episode following policy π: S₀, A₀, R₁, S₁, A₁, R₂, ..., Sₜ</p>

<h4>Policy Evaluation:</h4>
    <ul>
        <li>For each state-action pair (Sₜ, Aₜ) in the episode:</li>
        <pre><code>G ← Return from time step t
Append G to Returns(Sₜ, Aₜ)
Q(Sₜ, Aₜ) ← average(Returns(Sₜ, Aₜ))</code></pre>
    </ul>

 <h4>Policy Improvement:</h4>
    <ul>
        <li>For each state S in the episode:</li>
        <pre><code>π(S) ← argmax_a Q(S,a)</code></pre>
    </ul>

 <h4>Repeat:</h4>
    <ul>
        <li>Go to step 2 and generate more episodes until convergence or a set number of episodes</li>
    </ul>

<p>We implement two variants of Monte Carlo Control:</p>
    <h1>Monte Carlo Control Variants</h1>

<h2>1. On-policy Monte Carlo Control</h2>
    <p>On-policy Monte Carlo Control learns the optimal policy by improving the same policy that it uses to make decisions. It uses an ε-greedy policy for both action selection and improvement.</p>
    <h3>Algorithm:</h3>
    <h4>Initialization:</h4>
    <ul>
        <li>Initialize Q(s,a) arbitrarily for all state-action pairs</li>
        <li>Initialize π to an ε-greedy policy with respect to Q</li>
        <li>Initialize Returns(s,a) as an empty list for all state-action pairs</li>
    </ul>
    <h4>Episode Generation:</h4>
    <p>Generate an episode using π: S₀, A₀, R₁, S₁, A₁, R₂, ..., Sₜ</p>
    <h4>Policy Evaluation:</h4>
    <pre><code>G ← 0
For each step t = T-1, T-2, ..., 0:
    G ← γG + Rₜ₊₁
    Unless the pair Sₜ, Aₜ appears in S₀, A₀, S₁, A₁, ..., Sₜ₋₁, Aₜ₋₁:
        Append G to Returns(Sₜ, Aₜ)
        Q(Sₜ, Aₜ) ← average(Returns(Sₜ, Aₜ))</code></pre>

    <h4>Policy Improvement:</h4>
    <pre><code>For each S in the episode:
    A* ← argmax_a Q(S,a)
    For all a ∈ A(S):
        π(a|S) ← 1 - ε + ε/|A(S)| if a = A*
        π(a|S) ← ε/|A(S)| if a ≠ A*</code></pre>
<h4>Repeat:</h4>
    <p>Go to step 2 and generate more episodes until convergence or a set number of episodes.</p>

   <h4>Key Points:</h4>
    <ul>
        <li>Uses first-visit MC method: only the first occurrence of each state-action pair in an episode is used for updates.</li>
        <li>ε-greedy policy balances exploration and exploitation.</li>
        <li>Converges to an ε-soft policy (a policy that has a probability of at least ε/|A(S)| of selecting any action).</li>
    </ul>

   <h2>2. Off-policy Monte Carlo Control</h2>
    <p>Off-policy Monte Carlo Control learns the optimal policy while following a different behavior policy. It uses importance sampling to correct for the difference between the target and behavior policies.</p>

   <h3>Algorithm:</h3>

   <h4>Initialization:</h4>
    <ul>
        <li>Initialize Q(s,a) arbitrarily for all state-action pairs</li>
        <li>Initialize π(s) ← argmax_a Q(s,a) for all states (target policy)</li>
        <li>Initialize C(s,a) ← 0 for all state-action pairs (cumulative weights)</li>
    </ul>

   <h4>Episode Generation:</h4>
    <p>Generate an episode using behavior policy b: S₀, A₀, R₁, S₁, A₁, R₂, ..., Sₜ</p>

   <h4>Policy Evaluation and Improvement:</h4>
    <pre><code>G ← 0
W ← 1
For each step t = T-1, T-2, ..., 0:
    G ← γG + Rₜ₊₁
    C(Sₜ, Aₜ) ← C(Sₜ, Aₜ) + W
    Q(Sₜ, Aₜ) ← Q(Sₜ, Aₜ) + (W / C(Sₜ, Aₜ)) * (G - Q(Sₜ, Aₜ))
    π(Sₜ) ← argmax_a Q(Sₜ, a)
    If Aₜ ≠ π(Sₜ), then break
    W ← W * (1 / b(Aₜ|Sₜ))</code></pre>

   <h4>Repeat:</h4>
    <p>Go to step 2 and generate more episodes until convergence or a set number of episodes.</p>

   <h4>Key Points:</h4>
    <ul>
        <li>Uses a behavior policy b (often ε-greedy) for exploration.</li>
        <li>Target policy π is greedy with respect to Q.</li>
        <li>Importance sampling ratio W corrects for the difference between target and behavior policies.</li>
        <li>Can potentially learn from a wider range of experiences, as the behavior policy can be more exploratory.</li>
    </ul>

  <h2 id="requirements">Requirements</h2>
    <ul>
        <li>Python 3.7+</li>
        <li>OpenAI Gym</li>
        <li>MiniGrid</li>
        <li>NumPy</li>
        <li>Matplotlib (for visualization)</li>
    </ul>

 <h2 id="installation">Installation</h2>
 <pre><code>pip install gym minigrid numpy matplotlib</code></pre>

<img src=https://media.discordapp.net/attachments/1279373242267602967/1294270765742690356/MC_steps_Vs_episode.png?ex=670a6714&is=67091594&hm=618dc66cff39e028c736df920a14eb2cccde5b3535841b0b3d11865c0b02643d&=&format=webp&quality=lossless&width=713&height=540">
 <img src="https://media.discordapp.net/attachments/1279373242267602967/1294270766036025404/MC_Reward_Vs_Episode.png?ex=670a6715&is=67091595&hm=6484cbbec3d2edff5637f4028638f9cf5ad57bcd1235ca95d2fe8a179c619bd7&=&format=webp&quality=lossless&width=720&height=540">