import gym
from gym import spaces
from vizdoom import *
from stable_baselines3 import PPO
import random

import time 

import numpy as np
import os 
models_dir = "MODELS/PPO"
logdir = "logs"

	
class CustomVizdoom(gym.Env):
	"""Custom Environment that follows gym interface"""

	def __init__(self):
				super(CustomVizdoom, self).__init__()
				self.game=vizdoom.DoomGame()
				self.action_space = spaces.Discrete(3)
				self.observation_space = spaces.Box(low=0, high=255,
													shape=(3,240,320), dtype=np.uint8)
				self.game.load_config('scenarios/basic.cfg')
				self.game.set_window_visible(False)
				self.game.init()
	

	def step(self, action):
			actions = [[1, 0, 0],  # 0
					[0, 1, 0],  #  1
					[0, 0, 1]]  #  2

			# Execute the action and get the reward
			reward = self.game.make_action(actions[action], 4)  # Frame skip parameter

			# Check if the episode is done
			done = self.game.is_episode_finished()

			# Get the new state
			if not done:
				state = self.game.get_state().screen_buffer
			else:
				state = np.zeros(self.observation_space.shape)

			return state, reward, done, {}
			
		
	def reset(self):
				self.game.new_episode()
				return self.game.get_state().screen_buffer
	
	def close(self):
		self.game.close()
	
env=CustomVizdoom()

if not os.path.exists(models_dir):
     os.makedirs(models_dir)


if not os.path.exists(logdir):
     os.makedirs(logdir)

env.reset()

model=PPO("CnnPolicy",env,verbose=1,tensorboard_log=logdir)
timesteps=1000

episodes=50
for step in range(episodes):
	    
 		model.learn(total_timesteps=timesteps,reset_num_timesteps=False,tb_log_name="PPO")
		model.save(f"{models_dir}/{timesteps*step}")


env.close()