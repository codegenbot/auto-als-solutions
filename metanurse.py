import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

class ABCDEAssessment:
    def __init__(self):
        self.step = 'A'
        self.last_action = None
        self.action_count = 0
        self.drawer_opened = {'A': False, 'B': False, 'C': False}

    def next_step(self):
        self.step = 'ABCDE'['ABCDE'.index(self.step) + 1]
        self.action_count = 0

    def choose_action(self, obs):
        self.action_count += 1
        
        if self.action_count > 5:
            self.next_step()
        
        if self.step == 'A':
            if not self.drawer_opened['A']:
                self.drawer_opened['A'] = True
                return 18  # OpenAirwayDrawer
            if obs[7] == 0:
                return 8  # ExamineResponse
            if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
                return 3  # ExamineAirway
            if obs[7] > 0 or obs[8] > 0:
                return 35  # PerformAirwayManoeuvres
        elif self.step == 'B':
            if not self.drawer_opened['B']:
                self.drawer_opened['B'] = True
                return 19  # OpenBreathingDrawer
            if obs[25] == 0:
                return 25  # UseSatsProbe
            if obs[7] > 0 and obs[8] > 0 and obs[9] > 0 and obs[10] == 0:
                return 4  # ExamineBreathing
            if obs[7] > 0 and obs[40] < 0.88:
                return 30  # UseNonRebreatherMask
            if obs[8] > 0:
                return 29  # UseBagValveMask
        elif self.step == 'C':
            if not self.drawer_opened['C']:
                self.drawer_opened['C'] = True
                return 20  # OpenCirculationDrawer
            if obs[27] == 0:
                return 27  # UseBloodPressureCuff
            if obs[16] == 0 and obs[17] == 0:
                return 5  # ExamineCirculation
            if obs[17] > 0:
                return 17  # StartChestCompression
            if obs[34] > 0 and obs[41] < 60:
                if obs[13] == 0:
                    return 14  # UseVenflonIVCatheter
                return 15  # GiveFluids
        elif self.step == 'D':
            if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
                return 6  # ExamineDisability
        elif self.step == 'E':
            if obs[25] == 0 and obs[26] == 0:
                return 7  # ExamineExposure

        if self.last_action != 1 and self.action_count % 10 == 0:
            return 1  # CheckSignsOfLife
        if self.last_action != 2 and self.action_count % 15 == 0:
            return 2  # CheckRhythm

        if obs[33] > 0 and obs[40] >= 0.88 and obs[35] > 0 and obs[42] >= 8 and obs[34] > 0 and obs[41] >= 60:
            return 48  # Finish

        return 16  # ViewMonitor

assessment = ABCDEAssessment()

for line in sys.stdin:
    obs = parse_observations(line.strip())
    action = assessment.choose_action(obs)
    assessment.last_action = action
