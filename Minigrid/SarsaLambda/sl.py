import minigrid
import numpy as np
import gym
import matplotlib.pyplot as plt
import random
env=gym.make('MiniGrid-Empty-6x6-v0')#render_mode="human")
env.reset()

q_values={}
for x in range(1,5):
  for y in range(1,5):
    for z in range(4):
      q_values[((x,y),z)]={0:0,1:0,2:0}
epsilon=1
alpha=.2
gamma=.7
epsiodes=400
time_step=[]
reward_episode=[]
def qvalues_generator(env,q_values,epsilon,alpha,gamma):
  env.reset()
  state=(env.agent_pos,env.agent_dir)
  q_values[(4,4),]=0
  t=0
  G=0
  while(state[0]!=(4,4)):
    action=action_generator(epsilon,q_values[state])
    obs,reward,done,truncated,info=env.step(action)
    G=reward+(gamma)**(t)*(G)
    next_state=(env.agent_pos,env.agent_dir)
    action2=action_generator(epsilon,q_values[next_state])
    q_values[state][action]=q_values[state][action]+alpha*(reward+gamma*(q_values[next_state][action2])- q_values[state][action])
    state=next_state
    t=t+1
  return q_values,t,G
def action_generator(epsilon,q):
  if(random.random()<epsilon):
    act=random.randint(0,2)
  else:
    act=max(q, key=q.get)
  return act
def epsilon_decay(old_epsilon,decay_rate,min_epsilon):
  epi=old_epsilon*decay_rate
  return max(min_epsilon,epi)
episode_no=0
while(episode_no<=epsiodes):
  q_values,t,G=qvalues_generator(env,q_values,epsilon,alpha,gamma)
  time_step.append(t)
  reward_episode.append(G)
  epsilon=epsilon_decay(epsilon,decay_rate=.95,min_epsilon=0.01)
  episode_no=episode_no+1
print(q_values)
print(time_step)
print(reward_episode)
episod=np.arange(1,len(time_step)+1)
plt.plot(episod,time_step)
plt.xlabel('Episodes')
plt.ylabel('steps')

episod=np.arange(1,len(reward_episode)+1)
plt.plot(episod,reward_episode)
plt.xlabel('Episodes')
plt.ylabel('reward')

