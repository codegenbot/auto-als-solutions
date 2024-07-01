import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

class ABCDEAssessment:
    def __init__(self):
        self.step = 'A'
        self.timeout = 0
        self.drawer_opened = {'A': False, 'B': False, 'C': False}
        self.last_check = {'signs': 0, 'rhythm': 0}

    def next_step(self):
        self.step = 'BCDEF'['ABCDE'.index(self.step)]
        self.timeout = 0

def choose_action(observations, assessment):
    obs = parse_observations(observations)
    
    assessment.timeout += 1
    if assessment.timeout > 5:
        assessment.next_step()

    if assessment.last_check['signs'] > 10:
        assessment.last_check['signs'] = 0
        return 1  # CheckSignsOfLife

    if assessment.last_check['rhythm'] > 20:
        assessment.last_check['rhythm'] = 0
        return 2  # CheckRhythm

    if obs[24] == 0:
        return 25  # UseSatsProbe
    if obs[26] == 0:
        return 27  # UseBloodPressureCuff

    if assessment.step == 'A':
        if not assessment.drawer_opened['A']:
            assessment.drawer_opened['A'] = True
            return 18  # OpenAirwayDrawer
        if obs[7] == 0:
            return 8  # ExamineResponse
        if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
            return 3  # ExamineAirway
        assessment.next_step()

    if assessment.step == 'B':
        if not assessment.drawer_opened['B']:
            assessment.drawer_opened['B'] = True
            return 19  # OpenBreathingDrawer
        if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
            return 4  # ExamineBreathing
        if obs[7] > 0:  # BreathingNone detected
            return 29  # UseBagValveMask
        if obs[24] > 0 and obs[31] < 0.88:
            return 30  # UseNonRebreatherMask
        assessment.next_step()

    if assessment.step == 'C':
        if not assessment.drawer_opened['C']:
            assessment.drawer_opened['C'] = True
            return 20  # OpenCirculationDrawer
        if obs[16] == 0 and obs[17] == 0:
            return 5  # ExamineCirculation
        if obs[17] > 0:  # RadialPulseNonPalpable
            return 17  # StartChestCompression
        if obs[13] == 0:
            return 14  # UseVenflonIVCatheter
        if obs[26] > 0 and obs[33] < 60:
            return 15  # GiveFluids
        assessment.next_step()

    if assessment.step == 'D':
        if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
            return 6  # ExamineDisability
        assessment.next_step()

    if assessment.step == 'E':
        if obs[25] == 0 and obs[26] == 0:
            return 7  # ExamineExposure
        assessment.next_step()

    if (obs[24] > 0 and obs[31] >= 0.88 and
        obs[27] > 0 and obs[34] >= 8 and
        obs[26] > 0 and obs[33] >= 60):
        return 48  # Finish

    return 16  # ViewMonitor

assessment = ABCDEAssessment()
for line in sys