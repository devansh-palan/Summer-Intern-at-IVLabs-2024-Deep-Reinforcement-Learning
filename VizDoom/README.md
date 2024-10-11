<h1>VizDoom Environment - Training with Stable-Baselines3</h1>

    

<h2>Introduction</h2>
    <p>This project implements a reinforcement learning agent to play various scenarios in the VizDoom environment using Stable-Baselines3. The agent learns to navigate and combat in a 3D environment using state-of-the-art RL algorithms.</p>

<h2>Environment Description</h2>
    <p>VizDoom is a Doom-based AI research platform for reinforcement learning from raw visual information. It allows developing AI bots that play Doom using only the screen buffer. Key features include:</p>
    <ul>
        <li>3D first-person perspective</li>
        <li>Partial observability (agent's view is limited)</li>
        <li>Customizable resolution and rendering options</li>
        <li>Various scenarios with different objectives (e.g., navigation, combat, survival)</li>
        <li>Customizable reward structure and action space</li>
    </ul>
   <h2>Stable-Baselines3 Approach</h2>
    <p>Stable-Baselines3 is a set of reliable implementations of reinforcement learning algorithms in PyTorch. It provides a unified interface for training and deploying agents.</p>

  <h3>Algorithms Overview</h3>

  <h4>Proximal Policy Optimization (PPO)</h4>
    <ul>
        <li>On-policy algorithm</li>
        <li>Good performance across a wide range of tasks</li>
        <li>Relatively simple to tune</li>
    </ul>

  <h4>Advantage Actor Critic (A2C)</h4>
    <ul>
        <li>On-policy algorithm</li>
        <li>Synchronous version of A3C</li>
        <li>Good for environments with short episodes</li>
    </ul>

  <h4>Deep Q Network (DQN)</h4>
    <ul>
        <li>Off-policy algorithm</li>
        <li>Works well for discrete action spaces</li>
        <li>Includes variants like Double DQN and Dueling DQN</li>
    </ul>

   <h4>Soft Actor-Critic (SAC)</h4>
    <ul>
        <li>Off-policy algorithm</li>
        <li>Suitable for continuous action spaces</li>
        <li>Includes entropy regularization for improved exploration</li>
    </ul>

   <h3>Policy Networks</h3>
    <p>Stable-Baselines3 provides various policy network architectures:</p>
    <ul>
        <li><strong>MlpPolicy:</strong> Multi-layer perceptron, suitable for low-dimensional state spaces</li>
        <li><strong>CnnPolicy:</strong> Convolutional Neural Network, ideal for image-based inputs like VizDoom</li>
        <li><strong>MultiInputPolicy:</strong> Handles multiple input types (e.g., image and vector observations)</li>
    </ul>

   <h2>Requirements</h2>
    <ul>
        <li>Python 3.7+</li>
        <li>VizDoom</li>
        <li>Stable-Baselines3</li>
        <li>PyTorch</li>
        <li>OpenAI Gym</li>
        <li>NumPy</li>
        <li>Matplotlib (for visualization)</li>
    </ul>

   <h2>Installation</h2>
    <pre><code>pip install vizdoom stable-baselines3[extra] torch gymnasium numpy matplotlib</code></pre>
