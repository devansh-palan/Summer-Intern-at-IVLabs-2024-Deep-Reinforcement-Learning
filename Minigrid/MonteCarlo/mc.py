import gym_minigrid
import numpy as np
import gym
import matplotlib.pyplot as plt
import random
env=gym.make('MiniGrid-Empty-6x6-v0')#render_mode="human")
env.reset()

q_value={}
reward=[]
step_taken=[]
for x in range(1,5):
  for y in range(1,5):
    for z in range(4):
      q_value[((x,y),z)]={0:0,1:0,2:0}
policy={}
for x in range(1,5):
  for y in range(1,5):
    for z in range(4):
      policy[((x,y),z)]={0:1/3,1:1/3,2:1/3}
max_steps=100
gamma=.9
alpha=.4
k=1
old_epsilon=1
no_of_episodes=100
def epsilon_decay(old_epsilon,episode_no,min_epsilon=.01):
  new_epsilon=max(min_epsilon,(old_epsilon/episode_no))
  return new_epsilon
def episode_generator(env,max_steps,policy):
  env.reset()
  state=(env.agent_pos,env.agent_dir)
  episode=[]
  t=0
  while(True):
    r=random.random()
    action = None
    cumulative_prob = 0.0
    for a in range(3):
      cumulative_prob += policy[state][a]
      if r < cumulative_prob:
        action = a
        break
    obs,reward,done,truncated,info=env.step(action)
    direction=obs['direction']
    time_step=[state,action,reward]
    episode.append(time_step)
    state=(env.agent_pos,direction)
    t=t+1
    if(t>max_steps or done):
      break
  return episode,t

def q_value_generator(epi,gamma,alpha,q_value):
  G=0
  ts=len(epi)-1
  while(ts>=0):
    G=gamma*G+epi[ts][2]
    q_value[epi[ts][0]][epi[ts][1]]=q_value[epi[ts][0]][epi[ts][1]]+alpha*(G-q_value[epi[ts][0]][epi[ts][1]])
    ts=ts-1
  return q_value
def improve_policy(q,policy,episode_no,old_epsilon):
  E=epsilon_decay(old_epsilon,episode_no,min_epsilon=.01)
  for s in q.keys():
    max_action = max(q[s], key=q[s].get)
    for m in range(3):
      if(m==max_action):
        policy[s][m]=1-E+E/3
      else:
        policy[s][m]=E/3
  return(policy)
episode_no=0
while(episode_no<=no_of_episodes):
  epi,t=episode_generator(env,max_steps,policy)
  step_taken.append(t)
  G1=0
  ts=len(epi)-1
  while(ts>=0):
    G1=gamma*G1+epi[ts][2]
    ts=ts-1
  reward.append(G1)
  q=q_value_generator(epi,gamma,alpha,q_value)
  episode_no=episode_no+1
  older_epsilon=epsilon_decay(old_epsilon,episode_no,min_epsilon=.01)
  policy=improve_policy(q,policy,episode_no,older_epsilon)
print(policy)
print(reward)
print(step_taken)
episodes_list=np.arange(1,len(step_taken)+1)
plt.plot(episodes_list,step_taken)
plt.xlabel('Episodes')
plt.ylabel('steps')
plt.show()

episodes_list=np.arange(1,len(reward)+1)
plt.plot(episodes_list,reward)
plt.xlabel('Episodes')
plt.ylabel('reward')
plt.show()