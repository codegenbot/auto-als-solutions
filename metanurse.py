import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

class ABCDEAssessment:
    def __init__(self):
        self.step = 'A'
        self.equipment_used = set()
        self.counter = 0

    def next_step(self):
        steps = 'ABCDE'
        self.step = steps[steps.index(self.step) + 1] if self.step != 'E' else 'E'

def choose_action(obs, assessment):
    assessment.counter += 1
    if assessment.counter > 300:
        return 48  # Finish if too many steps

    if assessment.step == 'A':
        if 3 not in assessment.equipment_used:
            assessment.equipment_used.add(3)
            return 3  # ExamineAirway
        if obs[3] > 0.5:  # AirwayClear
            assessment.next_step()
        else:
            return 35  # PerformAirwayManoeuvres

    elif assessment.step == 'B':
        if 19 not in assessment.equipment_used:
            assessment.equipment_used.add(19)
            return 19  # OpenBreathingDrawer
        if 25 not in assessment.equipment_used:
            assessment.equipment_used.add(25)
            return 25  # UseSatsProbe
        if 4 not in assessment.equipment_used:
            assessment.equipment_used.add(4)
            return 4  # ExamineBreathing
        if obs[46] > 0.5 and obs[-1] < 88:  # If sats measured and < 88%
            return 30  # UseNonRebreatherMask
        if obs[40] > 0.5 and obs[-7] < 8:  # If resp rate measured and < 8
            return 29  # UseBagValveMask
        assessment.next_step()

    elif assessment.step == 'C':
        if 20 not in assessment.equipment_used:
            assessment.equipment_used.add(20)
            return 20  # OpenCirculationDrawer
        if 27 not in assessment.equipment_used:
            assessment.equipment_used.add(27)
            return 27  # UseBloodPressureCuff
        if 5 not in assessment.equipment_used:
            assessment.equipment_used.add(5)
            return 5  # ExamineCirculation
        if obs[17] > 0.5:  # RadialPulseNonPalpable
            return 17  # StartChestCompression
        if obs[45] > 0.5 and obs[-2] < 60:  # If MAP measured and < 60
            return 15  # GiveFluids
        if obs[38] > 0.5 and obs[-8] > 150:  # If heart rate measured and > 150
            return 9  # GiveAdenosine
        assessment.next_step()

    elif assessment.step == 'D':
        if 6 not in assessment.equipment_used:
            assessment.equipment_used.add(6)
            return 6  # ExamineDisability
        assessment.next_step()

    elif assessment.step == 'E':
        if 7 not in assessment.equipment_used:
            assessment.equipment_used.add(7)
            return 7  # ExamineExposure
        if (obs[3] > 0.5 and  # AirwayClear
            obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
            obs[40] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
            obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
            return 48  # Finish

    return 16  # ViewMonitor (default action to keep checking vitals)

assessment = ABCDEAssessment()
for line in sys.stdin:
    observations = parse