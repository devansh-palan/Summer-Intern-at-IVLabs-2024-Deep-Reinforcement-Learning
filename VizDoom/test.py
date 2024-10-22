
from stable_baselines3 import PPO
import time
 
from doom import CustomVizdoom

model = PPO.load("/home/devansh/Desktop/ivlabs/ViZDoom/MODELS/PPO/49000.zip") #set  the window visible to false and comment out the learning loop
env=CustomVizdoom()
total_reward = 0 
for eps in range(10):
    obs = env.reset()
    done =False
    while not done:
        action,_ = model.predict(obs)
        obs,reward,done,info = env.step(action)
        time.sleep(0.05)
        total_reward += reward
    print("Rewward",reward)
    time.sleep(1)