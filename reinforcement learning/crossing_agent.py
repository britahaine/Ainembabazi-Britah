import numpy as np
import random

# Define number of states and actions
# States: 0=(0,0), 1=(0,1), 2=(1,0), 3=(1,1)
num_states = 4
num_actions = 3  # 0=look_left, 1=look_right, 2=cross

# Initialize Q-table
Q = np.zeros((num_states, num_actions))

# Learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.1  # Exploration rate
num_episodes = 10000 # Number of episodes for training

# Step function: Given current state and action, return next state and reward
def step(state, action):
    if state == 0:  # (0,0)
        if action == 0:  # look_left
            return 2, -0.1  # Go to (1,0)
        elif action == 1:  # look_right
            return 1, -0.1  # Go to (0,1)
        elif action == 2:  # cross
            if random.random() < 0.5:
                return 4, 10  # Success
            else:
                return 5, -10  # Hit
    elif state == 1:  # (0,1)
        if action == 0:  # look_left
            return 3, -0.1  # Go to (1,1)
        elif action == 1:  # look_right
            return 1, -0.1  # Stay (0,1)
        elif action == 2:  # cross
            if random.random() < 0.5:
                return 4, 10  # Success
            else:
                return 5, -10  # Hit
    elif state == 2:  # (1,0)
        if action == 0:  # look_left
            return 2, -0.1  # Stay (1,0)
        elif action == 1:  # look_right
            return 3, -0.1  # Go to (1,1)
        elif action == 2:  # cross
            if random.random() < 0.5:
                return 4, 10  # Success
            else:
                return 5, -10  # Hit
    elif state == 3:  # (1,1)
        if action == 0:  # look_left
            return 3, -0.1  # Stay (1,1)
        elif action == 1:  # look_right
            return 3, -0.1  # Stay (1,1)
        elif action == 2:  # cross
            if random.random() < 0.9:
                return 4, 10  # Success
            else:
                return 5, -10  # Hit

# Q-learning training
for episode in range(num_episodes):
    state = 0  # Start from (0,0)
    while True:
        # Choose action using epsilon-greedy
        if random.uniform(0, 1) < epsilon:
            action = random.randint(0, num_actions - 1)
        else:
            action = np.argmax(Q[state])

        # Take action and get next state and reward
        next_state, reward = step(state, action)

        # Update Q-table
        if next_state > 3:  # Terminal state (success or hit)
            target = reward
        else:
            target = reward + gamma * np.max(Q[next_state])
        Q[state, action] += alpha * (target - Q[state, action])

        # Move to next state
        state = next_state

        # Check for terminal state
        if next_state > 3:
            break

# Print learned Q-table
print("Learned Q-table:")
print(Q)

# Extract policy
policy = {}
for state in range(num_states):
    policy[state] = np.argmax(Q[state])
print("\nLearned Policy:")
print(policy)