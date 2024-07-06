import random

class AIAgent:
    def __init__(self, environment):
        self.environment = environment
        self.q_values = {}

    def learn(self, episodes):
        for episode in range(episodes):
            state = self.environment.reset()
            done = False
            while not done:
                action = self.select_action(state)
                next_state, reward, done, _ = self.environment.step(action)
                self.update_q_value(state, action, next_state, reward)
                state = next_state

    def select_action(self, state):
        if random.random() < 0.1:
            return random.choice(self.environment.actions)
        else:
            return max(self.q_values[state], key=self.q_values[state].get)

    def update_q_value(self, state, action, next_state, reward):
        if state not in self.q_values:
            self.q_values[state] = {}
        if next_state not in self.q_values:
            self.q_values[next_state] = {}
        self.q_values[state][action] = reward + 0.9 * max(self.q_values[next_state].values())

ai_agent = AIAgent(environment)
