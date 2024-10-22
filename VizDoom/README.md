<h1>VizDoom Environment - Training with Stable-Baselines3</h1>

<img src="https://media.discordapp.net/attachments/1279373242267602967/1294378020601073786/The-basic-scenario-used.png?ex=670acaf8&is=67097978&hm=74237d5288ed4539f907182ae4e38d5f888e9c11cb2bd5d43179c60b3a02c59d&=&format=webp&quality=lossless&width=753&height=565">

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


<img src="https://media.discordapp.net/attachments/1246168053922791537/1296999911409193010/Screenshot_from_2024-10-19_06-16-49.png?ex=6718494b&is=6716f7cb&hm=ff5fc921e266c151b4e305280c21b30a58a6944708e70d8aed469d1f3cb8f723&=&format=webp&quality=lossless&width=1002&height=565"/>

<img src="https://media.discordapp.net/attachments/1246168053922791537/1296999911044157480/Screenshot_from_2024-10-19_06-17-03.png?ex=6718494b&is=6716f7cb&hm=62be43dace463c9659d8d63817f571ea924f6a80547ab80b763a79d24f2f7d9b&=&format=webp&quality=lossless&width=1096&height=565"/>

<video src="C:\Users\Devansh Palan\Downloads\Screencast from 22-10-24 05_07_57 PM IST.webm" />

