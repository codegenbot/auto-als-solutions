import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

class ABCDEAssessment:
    def __init__(self):
        self.state = 'A'
        self.steps = 0
        self.drawer_opened = {'A': False, 'B': False, 'C': False}
        self.equipment_used = {'sats_probe': False, 'bp_cuff': False}

    def choose_action(self, obs):
        self.steps += 1
        if self.steps > 300:
            return 48  # Finish due to timeout

        if self.state == 'A':
            if not self.drawer_opened['A']:
                self.drawer_opened['A'] = True
                return 18  # OpenAirwayDrawer
            if max(obs[:7]) < 0.5:
                return 3  # ExamineAirway
            self.state = 'B'

        if self.state == 'B':
            if not self.drawer_opened['B']:
                self.drawer_opened['B'] = True
                return 19  # OpenBreathingDrawer
            if not self.equipment_used['sats_probe']:
                self.equipment_used['sats_probe'] = True
                return 25  # UseSatsProbe
            if max(obs[7:16]) < 0.5:
                return 4  # ExamineBreathing
            self.state = 'C'

        if self.state == 'C':
            if not self.drawer_opened['C']:
                self.drawer_opened['C'] = True
                return 20  # OpenCirculationDrawer
            if not self.equipment_used['bp_cuff']:
                self.equipment_used['bp_cuff'] = True
                return 27  # UseBloodPressureCuff
            if max(obs[16:21]) < 0.5:
                return 5  # ExamineCirculation
            self.state = 'D'

        if self.state == 'D':
            if max(obs[21:27]) < 0.5:
                return 6  # ExamineDisability
            self.state = 'E'

        if self.state == 'E':
            if max(obs[27:33]) < 0.5:
                return 7  # ExamineExposure
            self.state = 'Monitor'

        if self.state == 'Monitor':
            return 16  # ViewMonitor

        # Stabilization actions
        if obs[46] > 0.5:  # If sats measured
            if obs[-1] < 65:
                return 17  # StartChestCompression
            elif obs[-1] < 88:
                return 30  # UseNonRebreatherMask

        if obs[45] > 0.5 and obs[-2] < 60:  # If MAP measured and < 60
            return 15  # GiveFluids

        if obs[40] > 0.5 and obs[-7] < 8:  # If resp rate measured and < 8
            return 29  # UseBagValveMask

        # Check if patient is stabilized
        if (obs[46] > 0.5 and obs[-1] >= 88 and
            obs[45] > 0.5 and obs[-2] >= 60 and
            obs[40] > 0.5 and obs[-7] >= 8):
            return 48  # Finish

        return 0  # DoNothing

assessment = ABCDEAssessment()

for line in sys.stdin:
    observations = parse_observations(line)
    action = assessment.choose_action(observations)
    print(action)
    sys.stdout.flush()