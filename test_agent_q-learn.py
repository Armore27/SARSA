import gym
import gym_mirror
env = gym.make('Mirror-v0')
import numpy as np

state_space = env.observation_space.n
action_space = env.action_space.n
qtable = np.zeros((state_space, action_space))

epsilon = 1.0  # Greed 100%
epsilon_min = 0.005  # Minimum greed 0.05%
epsilon_decay = 0.99993  # Decay multiplied with epsilon after each episode
episodes = 10  # Amount of games
max_steps = 500  # Maximum steps per episode
learning_rate = 0.65
gamma = 0.65

for episode in range(episodes):
# Reset the game state, done and score before every episode/game
    state = env.reset()  # Gets current game state
    done = False  # decides whether the game is over
    score = 0

    for _ in range(max_steps):

        # With the probability of (1 - epsilon) take the best action in our Q-table
        if random.uniform(0, 1) > epsilon:
            action = np.argmax(qtable[state, :])
        # Else take a random action
        else:
            action = env.action_space.sample()

        # Step the game forward
        next_state, reward, done, _ = env.step(action)

        # Add up the score
        score += reward

        # Update our Q-table with our Q-function
        qtable[state, action] = (1 - learning_rate) * qtable[state, action] \
                                + learning_rate * (reward + gamma * np.max(qtable[next_state, :]))

        # Set the next state as the current state
        state = next_state

        if done:
            break

    # Reducing our epsilon each episode (Exploration-Exploitation trade-off)
    if epsilon >= epsilon_min:
        epsilon *= epsilon_decay
