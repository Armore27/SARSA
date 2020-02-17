import gym
import matlab.engine
import numpy as np
import scipy.io

class MirrorEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, state, num_states = 0, num_actions = 45, sg1 = 0, sv1 = 0, z1 = 0, g1 = 0, v1 = 0):
        self.num_states = num_states
        self.num_actions = num_actions
        self.state = state
        self.sg1 = sg1
        self.sv1 = sv1
        self.z1 = z1
        self.g1 = g1
        self.v1 = v1
        
    def step(self, action = 0):
        """
        This function determines possible actions.
        """
        self.action = action
        a = 10
        b = 1
        eng = matlab.engine.start_matlab()

        for self.action in range(self.num_actions):
            """
            Useful actions, reward = -1.
            """
            if self.action == 0:
               self.sg1 = eng.sdg1(a)

            if self.action == 1:
                self.sv1 = eng.sdv1(a)

            if self.action == 2:
                self.z1 = eng.os1(a)

            if self.action == 3:
                self.g1 = eng.gora1(b)

            if self.action == 4:
                self.v1 = eng.vera1(b)

            if self.action == 5:
                self.sg1 = eng.sdg1(a)

            if self.action == 6:
                self.sv1 = eng.sdv1(a)
            
            if self.action == 7:
                self.z1 = eng.os1(a)

            if self.action == 8:
                self.g1 = eng.gora1(b)

            if self.action == 9:
                self.v1 = eng.vera1(b)

            if self.action == 10:
                self.g1 = eng.gora1(b)
                self.sg1 = eng.sdg1(a)

            if self.action == 11:
                self.v1 = eng.vera1(b)
                self.sv1 = eng.sdv1(a)

            if self.action == 12:
                self.z1 = eng.os1(a)
                self.sg1 = eng.sdg1(a)

            if self.action == 13:
                self.z1 = eng.os1(a)
                self.sv1 = eng.sdv1(a)

            if self.action == 14:
                self.g1 = eng.gora1(b)
                self.sg1 = eng.sdg1(a)

            if self.action == 15:
                self.v1 = eng.vera1(b)
                self.sv1 = eng.sdv1(a)

            if self.action == 16:
                self.z1 = eng.os1(a)
                self.sg1 = eng.sdg1(a)

            if self.action == 17:
                self.z1 = eng.os1(a)
                self.sv1 = eng.sdv1(a)

            if self.action == 18:
                self.g1 = eng.gora1(b)
                self.sg1 = eng.sdg1(a)

            if self.action == 19:
                self.v1 = eng.vera1(b)
                self.sv1 = eng.sdv1(a)

            if self.action == 20:
                self.z1 = eng.os1(a)
                self.sg1 = eng.sdg1(a)

            if self.action == 21:
                self.z1 = eng.os1(a)
                self.sv1 = eng.sdv1(a)

            if self.action == 22:
                self.g1 = eng.gora1(b)
                self.sg1 = eng.sdg1(a)

            if self.action == 23:
                self.v1 = eng.era1(b)
                self.sv1 = eng.sdv1(a)

            if self.action == 24:
                self.z1 = eng.os1(a)
                self.sg1 = eng.sdg1(a)

            if self.action == 25:
                self.z1 = eng.os1(a)
                self.sv1 = eng.sdv1(a)

            if self.action == 26:
                self.sg1 = eng.sdg1(a)
                self.sv1 = eng.sdv1(a)

            if self.action == 27:
                self.sg1 = eng.sdg1(a)
                self.sv1 = eng.sdv1(a)

            if self.action == 28:
                self.sg1 = eng.sdg1(a)
                self.sv1 = eng.sdv1(a)

            if self.action == 29:
                self.sv1 = eng.sdv1(a)
                self.sg1 = eng.sdg1(a)

            """
            Unuseful actions, reward = -10.
            """
            if self.action == 30:
                self.g1 = eng.gora1(b)
                self.sv1 = eng.sdv1(a)

            if self.action == 31:
                self.v1 = eng.vera1(b)
                self.sg1 = eng.sdg1(a)

            if self.action == 32:
                self.z1 = eng.os1(a)
                self.g1 = eng.gora1(b)

            if self.action == 33:
                self.z1 = eng.os1(a)
                self.v1 = eng.vera1(b)

            if self.action == 34:
                self.g1 = eng.gora1(b)
                self.sv1 = eng.sdv1(a)

            if self.action == 35:
                self.v1 = eng.vera1(b)
                self.sg1 = eng.sdg1(a)

            if self.action == 36:
                self.z1 = eng.os1(a)
                self.g1 = eng.gora1(b)

            if self.action == 37:
                self.z1 = eng.os1(a)
                self.v1 = eng.vera1(b)

            if self.action == 38:
                self.g1 = eng.gora1(b)
                self.sv1 = eng.sdv1(a)

            if self.action == 39:
                self.v1 = eng.vera1(b)
                self.sg1 = eng.sdg1(a)

            if self.action == 40:
                self.z1 = eng.os1(a)
                self.g1 = eng.gora1(b)

            if self.action == 41:
                self.z1 = eng.os1(a)
                self.v1 = eng.vera1(b)

            if self.action == 42:
                self.g1 = eng.gora1(b)
                self.sv1 = eng.sdv1(a)

            if self.action == 43:
                self.v1 = eng.vera1(b)
                self.sg1 = eng.sdg1(a)

            if self.action == 44:
                self.z1 = eng.os1(a)
                self.g1 = eng.gora1(b)

            if self.action == 45:
                self.z1 = eng.os1(a)
                self.v1 = eng.vera1(b)

        state = self._get_state()
        reward = self._get_reward()
        return self.state, reward, self.z1, self.sg1, self.sv1, self.g1, self.v1

    def _get_state(self):
        """
        This function returns the current state.
        """
        self.num_states = +1
        eng = matlab.engine.start_matlab()
        self.state = eng.Obrabotka()
        return self.state, self.num_states

    def reset(self, a_z1 = 0, a_sg1 = 0, a_sv1 = 0, b_g1 = 0, b_v1 = 0):
        """
        This function resets the environment into the initial state.
        """
        eng = matlab.engine.start_matlab()

        self.a_z1 = a_z1
        self.a_sg1 = a_sg1
        self.a_sv1 = a_sv1
        self.b_g1 = b_g1
        self.b_v1 = b_v1

        self.a_z1 = (-1)*self.z1
        self.a_sg1 = (-1)*self.sg1
        self.a_sv1 = (-1)*self.sv1
        self.b_g1 = (-1)*self.g1
        self.b_v1 = (-1)*self.v1

        self.z1 = eng.os1(self.a_z1)
        self.sg1 = eng.sdg1(self.a_sg1)
        self.sv1 = eng.sdv1(self.a_sv1)
        self.g1 = eng.gora1(self.b_g1)
        self.g1 = eng.vera1(self.b_v1)

        return self._get_state()

    def end(self):
        if self.num_states == 500:
            return self.reset 

    def _get_reward(self):
        """
        This function calculates the reward.
        """
        zernike = scipy.io.loadmat('koef.mat')
        koef_hands = np.array(zernike)

        rewards = {"useful": -1,
                   "unuseful": -10,
                   "complited": 200}
        for i in self.state:
            for j in koef_hands:
                if self.state[i] <= koef_hands[j]:
                    return rewards["complited"]
        for self.action in range(0, 30):
            return rewards["useful"]
        for self.actions in range(30, 46):
            return rewards["unuseful"]
