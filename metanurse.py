import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs):
    airway_checked = max(obs[:7])
    breathing_checked = max(obs[7:16])
    circulation_checked = max(obs[16:21])
    disability_checked = max(obs[21:27])
    exposure_checked = max(obs[27:33])
    
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
    
    if obs[46] > 0.5 and obs[-1] < 88:  # If sats measured and < 88%
        return 30  # UseNonRebreatherMask
    
    if obs[45] > 0.5 and obs[-2] < 60:  # If MAP measured and < 60
        return 15  # GiveFluids
    
    if obs[40] > 0.5 and obs[-7] < 8:  # If resp rate measured and < 8
        return 29  # UseBagValveMask
    
    return 48  # Finish

for line in sys.stdin:
    observations = parse_observations(line)
    action = choose_action(observations)
    print(action)
    sys.stdout.flush()