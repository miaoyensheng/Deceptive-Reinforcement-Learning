# qlearningAgents.py
# ------------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

# import os
from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *
import graphicsDisplay
import graphicsUtils

import random,util,math


class QLearningAgent(ReinforcementAgent):
    """
      Q-Learning Agent
      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update
      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)
      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """

    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.expandedCells = []
        "*** YOUR CODE HERE ***"

        self.values = util.Counter()

        grid_states = util.Counter()
        # Plug in the file that you want to check in grid world here
        grid_data = open("dataRealGoal.txt", "r")

        for line in grid_data:
            str_position, action, value = line.split("|")
            grid_states[(str_position, action)] = float(value)

        grid_data.close()

        data = [grid_states]

        for i in data:
            for key, value in i.items():
                self.values[(str((int(key[0][1])-1, int(key[0][4])-1)), key[1].lower())] += value

        # compare_data = open("dataCurrent.txt", "w")
        #
        # self.find_largest = util.Counter()
        # self.action = util.Counter()
        #
        # for i in data:
        #     for key, value in i.items():
        #         if self.find_largest[(str((int(key[0][1]) - 1, int(key[0][4]) - 1)))] < value:
        #             self.action[(str((int(key[0][1]) - 1, int(key[0][4]) - 1)))] = (value, key[1])
        #             self.find_largest[(str((int(key[0][1]) - 1, int(key[0][4]) - 1)))] = value
        #
        # for key, value in self.action.items():
        #
        #     compare_data.write(str(key)+"|"+(value[1])+"\n")
        #
        # compare_data.close()

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"

        return self.values[(str(state), action)]

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"

        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return 0.0

        return max([self.getQValue(str(state), action) for action in legal_actions])

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"

        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return None

        max_value = self.computeValueFromQValues(state)

        actions = [action for action in legal_actions if self.values[(str(state), action)] == max_value]

        return random.choice(actions)

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.
          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return None

        if util.flipCoin(self.epsilon):
            return random.choice(legal_actions)

        else:
            return self.computeActionFromQValues(state)

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"

        temporal_difference = reward + self.discount * self.computeValueFromQValues(nextState) - self.getQValue(state, action)

        val = self.getQValue(state, action) + self.alpha * temporal_difference

        self.values[(str(state), action)] = val

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)




















class FQLearningAgent(ReinforcementAgent):  # run to create dataFakeGoal.txt using real goal map
    """
      Q-Learning Agent
      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update
      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)
      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """

    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.expandedCells = []
        "*** YOUR CODE HERE ***"

        self.values = util.Counter()  # Creating(or update by complete replacing) new real goal data
        f = open("dataFakeGoal.txt", "w")
        f.close()

        # reading the saved data in text file
        fake_goal1_values = util.Counter()
        real_goal_values = util.Counter()

        fake_goal1_data = open("dataFakeGoal1.txt", "r")
        real_goal_data = open("dataRealGoal.txt", "r")

        for line in fake_goal1_data:
            str_position, action, value = line.split("|")
            fake_goal1_values[(str_position, action)] = float(value)

        for line in real_goal_data:
            str_position, action, value = line.split("|")
            real_goal_values[(str_position, action)] = float(value)

        fake_goal1_data.close()
        real_goal_data.close()

        data = [fake_goal1_values, real_goal_values]

        for i in data:
            for key, value in i.items():
                self.values[(key[0], key[1])] += value

        self.find_largest = util.Counter()
        self.action = util.Counter()



















    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        return self.values[(str(position), action)]

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"

        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return 0.0

        return max([self.getQValue(state, action) for action in legal_actions])

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return None

        max_value = self.computeValueFromQValues(state)

        actions = [action for action in legal_actions if self.values[(str(position), action)] == max_value]

        return random.choice(actions)

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.
          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return None

        if util.flipCoin(self.epsilon):
            return random.choice(legal_actions)

        else:
            return self.computeActionFromQValues(state)

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        temporal_difference = reward + self.discount * self.computeValueFromQValues(nextState) - self.getQValue(state, action)

        val = self.getQValue(state, action) + self.alpha * temporal_difference

        self.values[(str(position), action)] = val

        with open("dataFakeGoal.txt", "a+") as f:
            f.write(str(position) + "|" + action + "|" + str(val) + "\n")

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class FPacmanQAgent(FQLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.6, alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1
        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        FQLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = FQLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action























class F1QLearningAgent(ReinforcementAgent):  # run to create dataFakeGoal.txt using real goal map
    """
      Q-Learning Agent
      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update
      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)
      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """

    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.expandedCells = []
        "*** YOUR CODE HERE ***"

        self.values = util.Counter()  # Creating(or update by complete replacing) new real goal data
        f = open("dataFakeGoal1.txt", "w")
        f.close()

        # reading the saved data in text file
        fake_goal_values = util.Counter()
        real_goal_values = util.Counter()

        fake_goal_data = open("dataFakeGoal.txt", "r")
        real_goal_data = open("dataRealGoal.txt", "r")

        for line in fake_goal_data:
            str_position, action, value = line.split("|")
            fake_goal_values[(str_position, action)] = float(value)

        for line in real_goal_data:
            str_position, action, value = line.split("|")
            real_goal_values[(str_position, action)] = float(value)

        fake_goal_data.close()
        real_goal_data.close()

        data = [fake_goal_values, real_goal_values]

        for i in data:
            for key, value in i.items():
                self.values[(key[0], key[1])] += value

        self.find_largest = util.Counter()
        self.action = util.Counter()























    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        return self.values[(str(position), action)]

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"

        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return 0.0

        return max([self.getQValue(state, action) for action in legal_actions])

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return None

        max_value = self.computeValueFromQValues(state)

        actions = [action for action in legal_actions if self.values[(str(position), action)] == max_value]

        return random.choice(actions)

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.
          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return None

        if util.flipCoin(self.epsilon):
            return random.choice(legal_actions)

        else:
            return self.computeActionFromQValues(state)

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        temporal_difference = reward + self.discount * self.computeValueFromQValues(nextState) - self.getQValue(state, action)

        val = self.getQValue(state, action) + self.alpha * temporal_difference

        self.values[(str(position), action)] = val

        with open("dataFakeGoal1.txt", "a+") as f:
            f.write(str(position) + "|" + action + "|" + str(val) + "\n")

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class F1PacmanQAgent(F1QLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05,gamma=0.6, alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1
        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        F1QLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = F1QLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action




























class RQLearningAgent(ReinforcementAgent):  # run to create dataRealGoal.txt using real goal map
    """
      Q-Learning Agent
      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update
      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)
      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """

    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.expandedCells = []
        "*** YOUR CODE HERE ***"

        self.values = util.Counter()  # Creating(or update by complete replacing) new real goal data
        f = open("dataRealGoal.txt", "w")
        f.close()

        penalty_values = util.Counter()
        fake_goal_values = util.Counter()
        fake_goal1_values = util.Counter()

        fake_goal_data = open("dataFakeGoal.txt", "r")
        fake_goal1_data = open("dataFakeGoal1.txt", "r")
        penalty_data = open("penalty.txt", "r")

        for line in fake_goal_data:
            str_position, action, value = line.split("|")
            fake_goal_values[(str_position, action)] = float(value)

        for line in fake_goal1_data:
            str_position, action, value = line.split("|")
            fake_goal1_values[(str_position, action)] = float(value)

        for line in penalty_data:
            str_position, action, value = line.split("|")
            penalty_values[(str_position, action)] = -float(value)

        fake_goal_data.close()
        fake_goal1_data.close()
        penalty_data.close()

        data = [fake_goal_values, fake_goal1_values, penalty_values]

        for i in data:
            for key, value in i.items():
                self.values[(key[0], key[1])] += value










    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        return self.values[(str(position), action)]

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"

        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return 0.0

        return max([self.getQValue(state, action) for action in legal_actions])

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return None

        max_value = self.computeValueFromQValues(state)

        actions = [action for action in legal_actions if self.values[(str(position), action)] == max_value]

        return random.choice(actions)

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.
          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return None

        if util.flipCoin(self.epsilon):
            return random.choice(legal_actions)

        else:
            return self.computeActionFromQValues(state)

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        temporal_difference = reward + self.discount * self.computeValueFromQValues(nextState) - self.getQValue(state, action)

        val = self.getQValue(state, action) + self.alpha * temporal_difference

        self.values[(str(position), action)] = val

        with open("dataRealGoal.txt", "a+") as f:
            f.write(str(position) + "|" + action + "|" + str(val) + "\n")

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class RPacmanQAgent(RQLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05, gamma=0.9, alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1
        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        RQLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = RQLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action



















































class PQLearningAgent(ReinforcementAgent):  # run to create dataRealGoal.txt using real goal map
    """
      Q-Learning Agent
      Functions you should fill in:
        - computeValueFromQValues
        - computeActionFromQValues
        - getQValue
        - getAction
        - update
      Instance variables you have access to
        - self.epsilon (exploration prob)
        - self.alpha (learning rate)
        - self.discount (discount rate)
      Functions you should use
        - self.getLegalActions(state)
          which returns legal actions for a state
    """

    def __init__(self, **args):
        "You can initialize Q-values here..."
        ReinforcementAgent.__init__(self, **args)
        self.expandedCells = []
        "*** YOUR CODE HERE ***"

        self.values = util.Counter()  # Creating(or update by complete replacing) new real goal data
        f = open("penalty.txt", "w")
        f.close()

    def getQValue(self, state, action):
        """
          Returns Q(state,action)
          Should return 0.0 if we have never seen a state
          or the Q node value otherwise
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        return self.values[(str(position), action)]

    def computeValueFromQValues(self, state):
        """
          Returns max_action Q(state,action)
          where the max is over legal actions.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return a value of 0.0.
        """
        "*** YOUR CODE HERE ***"

        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return 0.0

        return max([self.getQValue(state, action) for action in legal_actions])

    def computeActionFromQValues(self, state):
        """
          Compute the best action to take in a state.  Note that if there
          are no legal actions, which is the case at the terminal state,
          you should return None.
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return None

        max_value = self.computeValueFromQValues(state)

        actions = [action for action in legal_actions if self.values[(str(position), action)] == max_value]

        return random.choice(actions)

    def getAction(self, state):
        """
          Compute the action to take in the current state.  With
          probability self.epsilon, we should take a random action and
          take the best policy action otherwise.  Note that if there are
          no legal actions, which is the case at the terminal state, you
          should choose None as the action.
          HINT: You might want to use util.flipCoin(prob)
          HINT: To pick randomly from a list, use random.choice(list)
        """
        legal_actions = self.getLegalActions(state)

        if len(legal_actions) == 0:
            return None

        if util.flipCoin(self.epsilon):
            return random.choice(legal_actions)

        else:
            return self.computeActionFromQValues(state)

    def update(self, state, action, nextState, reward):
        """
          The parent class calls this to observe a
          state = action => nextState and reward transition.
          You should do your Q-Value update here
          NOTE: You should never call this function,
          it will be called on your behalf
        """
        "*** YOUR CODE HERE ***"

        position = state.getPacmanPosition()

        temporal_difference = reward + self.discount * self.computeValueFromQValues(nextState) - self.getQValue(state, action)

        val = self.getQValue(state, action) + self.alpha * temporal_difference

        self.values[(str(position), action)] = val

        with open("penalty.txt", "a+") as f:
            f.write(str(position) + "|" + action + "|" + str(val) + "\n")

    def getPolicy(self, state):
        return self.computeActionFromQValues(state)

    def getValue(self, state):
        return self.computeValueFromQValues(state)


class PPacmanQAgent(PQLearningAgent):
    "Exactly the same as QLearningAgent, but with different default parameters"

    def __init__(self, epsilon=0.05, gamma=0.95, alpha=0.2, numTraining=0, **args):
        """
        These default parameters can be changed from the pacman.py command line.
        For example, to change the exploration rate, try:
            python pacman.py -p PacmanQLearningAgent -a epsilon=0.1
        alpha    - learning rate
        epsilon  - exploration rate
        gamma    - discount factor
        numTraining - number of training episodes, i.e. no learning after these many episodes
        """
        args['epsilon'] = epsilon
        args['gamma'] = gamma
        args['alpha'] = alpha
        args['numTraining'] = numTraining
        self.index = 0  # This is always Pacman
        PQLearningAgent.__init__(self, **args)

    def getAction(self, state):
        """
        Simply calls the getAction method of QLearningAgent and then
        informs parent of action for Pacman.  Do not change or remove this
        method.
        """
        action = PQLearningAgent.getAction(self,state)
        self.doAction(state,action)
        return action



















