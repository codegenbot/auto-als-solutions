import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step_counter):
    if step_counter >= 350:
        return 48  # Finish if 350 steps reached

    airway_checked = max(obs[:7])
    breathing_checked = max(obs[7:16])
    circulation_checked = max(obs[16:21])
    disability_checked = max(obs[21:27])
    exposure_checked = max(obs[27:33])
    
    # Check for cardiac arrest conditions
    if (obs[46] > 0.5 and obs[-1] < 65) or (obs[45] > 0.5 and obs[-2] < 20):
        return 17  # StartChestCompression
    
    if obs[7] > 0.5:  # BreathingNone
        return 29  # UseBagValveMask
    
    # ABCDE assessment
    if airway_checked < 0.5:
        return 3  # ExamineAirway
    elif breathing_checked < 0.5:
        return 4  # ExamineBreathing
    elif circulation_checked < 0.5:
        return 5  # ExamineCirculation
    elif disability_checked < 0.5:
        return 6  # ExamineDisability
    elif exposure_checked < 0.5:
        return 7  # ExamineExposure
    
    # Use equipment
    if obs[25] < 0.5:  # UseSatsProbe not used
        return 19  # OpenBreathingDrawer
    elif obs[25] > 0.5 and obs[46] < 0.5:  # SatsProbe used but not measured
        return 25  # UseSatsProbe
    
    if obs[27] < 0.5:  # UseBloodPressureCuff not used
        return 20  # OpenCirculationDrawer
    elif obs[27] > 0.5 and obs[45] < 0.5:  # BloodPressureCuff used but not measured
        return 27  # UseBloodPressureCuff
    
    if obs[39] < 0.5 or obs[40] < 0.5 or obs[41] < 0.5 or obs[45] < 0.5 or obs[46] < 0.5:
        return 16  # ViewMonitor
    
    # Interventions based on vital signs
    if obs[46] > 0.5 and obs[-1] < 88:  # If sats measured and < 88%
        return 30  # UseNonRebreatherMask
    
    if obs[45] > 0.5 and obs[-2] < 60:  # If MAP measured and < 60
        return 15  # GiveFluids
    
    if obs[40] > 0.5 and obs[-7] < 8:  # If resp rate measured and < 8
        return 29  # UseBagValveMask
    
    if obs[39] > 0.5 and obs[-8] > 150:  # If heart rate measured and > 150
        return 9  # GiveAdenosine
    
    # Check if patient is stabilized
    if (obs[3] > 0.5 and  # AirwayClear
        obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
        obs[40] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
        obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
        return 48  # Finish
    
    return 16  # ViewMonitor (default action to keep checking vitals)

step_counter = 0
for line in sys.stdin:
    observations = parse_observations(line)
    action = choose_action(observations, step_counter)
    print(action)
    sys.stdout.flush()
    step_counter