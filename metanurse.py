import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs):
    airway_checked = max(obs[:7])
    breathing_checked = max(obs[7:16])
    circulation_checked = max(obs[16:21])
    disability_checked = max(obs[21:27])
    exposure_checked = max(obs[27:33])
    
    if obs[7] > 0.5:  # BreathingNone
        return 29  # UseBagValveMask
    
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
    
    if obs[39] < 0.5:  # MeasuredMAP not recent
        return 27  # UseBloodPressureCuff
    if obs[40] < 0.5:  # MeasuredSats not recent
        return 25  # UseSatsProbe
    if obs[41] < 0.5:  # MeasuredResps not recent
        return 16  # ViewMonitor
    
    if obs[46] > 0.5 and obs[-1] < 88:  # If sats measured and < 88%
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
    
    return 16  # ViewMonitor (default action to keep checking vitals)

for line in sys.stdin:
    observations = parse_observations(line)
    action = choose_action(observations)
    print(action)
    sys.stdout.flush()