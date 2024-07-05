import sys
from collections import deque

class ResuscitationState:
    INITIAL = 0
    ABCDE = 1
    CPR = 2
    POST_CPR = 3

def parse_observations(observations):
    return list(map(float, observations.split()))

class Resuscitation:
    def __init__(self):
        self.state = ResuscitationState.INITIAL
        self.last_actions = deque(maxlen=5)
        self.timer = 0
        self.cpr_timer = 0
        self.help_called = False

    def choose_action(self, obs):
        self.timer += 1
        if self.state == ResuscitationState.CPR:
            self.cpr_timer += 1

        if not self.help_called:
            self.help_called = True
            return 1  # CheckSignsOfLife (and implicitly call for help)

        if obs[7] > 0.5 or (obs[46] > 0.5 and obs[-1] < 65) or (obs[45] > 0.5 and obs[-2] < 20):
            self.state = ResuscitationState.CPR
            self.cpr_timer = 0

        if self.state == ResuscitationState.CPR:
            if self.cpr_timer % 30 == 0:
                return 10  # GiveAdrenaline
            if self.cpr_timer % 5 == 0:
                return 2  # CheckRhythm
            if 28 not in self.last_actions:
                return 28  # AttachDefibPads
            if 39 not in self.last_actions:
                return 39  # TurnOnDefibrillator
            if 2 in self.last_actions and self.last_actions[-1] != 17:
                rhythm = max(obs[28:39])
                if rhythm == obs[38] or rhythm == obs[32]:  # VF or VT
                    return 40  # DefibrillatorCharge
            if self.last_actions[-1] == 40:
                return 41  # DefibrillatorCurrentUp
            return 17  # StartChestCompression

        if self.state == ResuscitationState.INITIAL or self.state == ResuscitationState.POST_CPR:
            action = self.abcde_assessment(obs)
            if action is not None:
                return action

        self.state = ResuscitationState.POST_CPR
        return self.stabilize_patient(obs)

    def abcde_assessment(self, obs):
        if 3 not in self.last_actions:
            return 3  # ExamineAirway
        if 4 not in self.last_actions:
            return 4  # ExamineBreathing
        if 25 not in self.last_actions:
            return 25  # UseSatsProbe
        if 5 not in self.last_actions:
            return 5  # ExamineCirculation
        if 27 not in self.last_actions:
            return 27  # UseBloodPressureCuff
        if 6 not in self.last_actions:
            return 6  # ExamineDisability
        if 7 not in self.last_actions:
            return 7  # ExamineExposure
        return None

    def stabilize_patient(self, obs):
        if obs[46] > 0.5 and obs[-1] < 88:
            return 30  # UseNonRebreatherMask
        if obs[45] > 0.5 and obs[-2] < 60:
            return 15  # GiveFluids
        if obs[40] > 0.5 and obs[-7] < 8:
            return 29  # UseBagValveMask
        if (obs[46] > 0.5 and obs[-1] >= 88 and
            obs[45] > 0.5 and obs[-2] >= 60 and
            obs[40] > 0.5 and obs[-