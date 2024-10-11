<h1>MiniGrid Environment - Action Space and Description</h1>

   <img src="https://minigrid.farama.org/_images/EmptyEnv.gif">

<h2>Action Space</h2>
    <p><strong>Type:</strong> Discrete(7)</p>

   <h2>Observation Space</h2>
    <p><strong>Type:</strong> Dict</p>
    <ul>
        <li><strong>direction:</strong> Discrete(4)</li>
        <li><strong>image:</strong> Box(0, 255, (7, 7, 3), uint8)</li>
        <li><strong>mission:</strong> MissionSpace</li>
    </ul>

   <h2>Reward Range</h2>
    <p>(0, 1)</p>

   <h2>Creation</h2>
    <pre><code>gymnasium.make("MiniGrid-Empty-16x16-v0")</code></pre>

   <h2>Description</h2>
    <p>This environment is an empty room, and the goal of the agent is to reach the green goal square, which provides a sparse reward. A small penalty is subtracted for the number of steps to reach the goal. This environment is useful, with small rooms, to validate that your RL algorithm works correctly, and with large rooms to experiment with sparse rewards and exploration. The random variants of the environment have the agent starting at a random position for each episode, while the regular variants have the agent always starting in the corner opposite to the goal.</p>

   <h2>Mission Space</h2>
    <p>“get to the green goal square”</p>

   <h2>Action Space Details</h2>
    <table border="1">
        <tr>
            <th>Num</th>
            <th>Name</th>
            <th>Action</th>
        </tr>
        <tr>
            <td>0</td>
            <td>left</td>
            <td>Turn left</td>
        </tr>
        <tr>
            <td>1</td>
            <td>right</td>
            <td>Turn right</td>
        </tr>
        <tr>
            <td>2</td>
            <td>forward</td>
            <td>Move forward</td>
        </tr>
        <tr>
            <td>3</td>
            <td>pickup</td>
            <td>Unused</td>
        </tr>
        <tr>
            <td>4</td>
            <td>drop</td>
            <td>Unused</td>
        </tr>
        <tr>
            <td>5</td>
            <td>toggle</td>
            <td>Unused</td>
        </tr>
        <tr>
            <td>6</td>
            <td>done</td>
            <td>Unused</td>
        </tr>
    </table>

   <h2>Observation Encoding</h2>
    <p>Each tile is encoded as a 3-dimensional tuple: <code>(OBJECT_IDX, COLOR_IDX, STATE)</code></p>
    <p><strong>OBJECT_TO_IDX</strong> and <strong>COLOR_TO_IDX</strong> mappings can be found in <code>minigrid/core/constants.py</code>.</p>
    <p><strong>STATE</strong> refers to the door state with:</p>
    <ul>
        <li>0 = open</li>
        <li>1 = closed</li>
        <li>2 = locked</li>
    </ul>

   <h2>Rewards</h2>
    <p>A reward of <code>1 - 0.9 * (step_count / max_steps)</code> is given for success, and <code>0</code> for failure.</p>

   <h2>Termination</h2>
    <p>The episode ends if any one of the following conditions is met:</p>
    <ul>
        <li>The agent reaches the goal.</li>
        <li>Timeout (see <strong>max_steps</strong>).</li>
    </ul>