<h1>MiniGrid Environment - Action Space and Description</h1>

   <img src="https://camo.githubusercontent.com/4c91fc8f5469c3a6bd9fad7c04c2f6297b369cf0db200f26f7e42f31bfd83093/68747470733a2f2f692e696d6775722e636f6d2f346c43774c38672e676966" height=300px width=300px>

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

<img src="https://camo.githubusercontent.com/58565c007abc6833ce67aef88ca8f16f4a1f001049e37a6864debb74f2cf1750/68747470733a2f2f692e696d6775722e636f6d2f7370516a6d4f622e706e67 " height="500px" >

<img src="https://camo.githubusercontent.com/d8d56d1bc76b1f947d193d169179d1ae6b49c8cadc79fdc4338c6e036fc1a579/68747470733a2f2f692e696d6775722e636f6d2f6b58614f5464352e706e67" height="500px">