<h1>VizDoom Environment - Training with Stable-Baselines3</h1>

<img src="https://www.dropbox.com/scl/fi/0te9k0z68fqegd5znu5ea/clideo_editor_68da857852f4409dafa7d51cf4cb5545-1-1.gif?rlkey=galbl43qq913vf0n5ctk7gdh6&st=3prl6r0y&raw=1
" width="500px">

<h1>Doom RL Environment using PPO</h1>
    <p>
        This project demonstrates how to train a reinforcement learning (RL) agent using 
        Proximal Policy Optimization (PPO) on a custom environment built for the game <em>Doom</em> 
        using the <code>vizdoom</code> library. The RL agent is trained to interact with the game 
        environment and learn optimal policies for navigating and surviving in the game.
    </p>

<h2>Environment Description</h2>

<p>VizDoom is a Doom-based AI research platform for reinforcement learning from raw visual information. It allows developing AI bots that play Doom using only the screen buffer. Key features include:</p>
    <ul>
        <li>3D first-person perspective</li>
        <li>Partial observability (agent's view is limited)</li>
        <li>Customizable resolution and rendering options</li>
        <li>Various scenarios with different objectives (e.g., navigation, combat, survival)</li>
        <li>Customizable reward structure and action space</li>
    </ul>
<h2 id="references">References</h2>
    <ul>
        <li><a href="https://vizdoom.cs.put.edu.pl/">VizDoom Documentation</a></li>
        <li><a href="https://stable-baselines3.readthedocs.io/">Stable Baselines3 Documentation</a></li>
    </ul>
   
<h2 id="usage">Usage</h2>
    <ol>
        <li><strong>Run the training script:</strong>
            <pre><code>python doom.py</code></pre>
            <p>This will initialize the <em>Doom</em> environment, set up the PPO model, and begin training.</p>
        </li>
        <li><strong>Training Options:</strong>
            <ul>
                <li>Modify <code>timesteps</code> and <code>episodes</code> in the script to change the number of steps and episodes for training.</li>
                <li>Models are saved in the <code>MODELS/PPO</code> directory and logs are saved in the <code>logs</code> directory for TensorBoard.</li>
            </ul>
        </li>
        <li><strong>Visualize Training (TensorBoard):</strong>
            <p>After training starts, you can visualize the learning progress using TensorBoard:</p>
            <pre><code>tensorboard --logdir=logs</code></pre>
        </li>
    </ol>

   <h2>Requirements</h2>
    <ul>
        <li>Python 3.7+</li>
        <li>VizDoom</li>
        <li>Stable-Baselines3</li>
        <li>PyTorch</li>
        <li>OpenAI Gym</li>
        <li>NumPy</li>
        <li>Tensorboard (for visualization)</li>
    </ul>

   <h2>Installation</h2>
    <pre><code>pip install vizdoom stable-baselines3[extra] torch gym[box2d] numpy matplotlib</code></pre>


<img src="https://www.dropbox.com/scl/fi/1zeeue8p6e8f0gs5rltwg/Screenshot_from_2024-10-19_06-16-49.webp?rlkey=jmiepphzb9ydmja24qzipiuam&st=eebwr3zi&raw=1"/>

<img src="https://www.dropbox.com/scl/fi/7juklh0fpky3qjnrv1bga/Screenshot_from_2024-10-19_06-17-03.webp?rlkey=9bcp0ntkjltkcx722i6k5eckm&st=c4d8cf6i&raw=1"/>


