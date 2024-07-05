import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs):
    airway_checked = max(obs[:7])
    breathing_checked = max(obs[7:16])
    circulation_checked = max(obs[16:21])
    disability_checked = max(obs[21:27])
    exposure_checked = max(obs[27:33])
    
    if obs[17] > 0.5:  # RadialPulseNonPalpable
        return 17  # StartChestCompression
    
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
    
    if obs[39] < 0.5 or obs[40] < 0.5 or obs[41] < 0.5:
        return 16  # ViewMonitor
    
    if obs[24] < 0.5:  # HeartRhythmNSR not recent
        return 24  # UseMonitorPads
    if obs[25] < 0.5:  # UseSatsProbe not used
        return 25  # UseSatsProbe
    if obs[26] < 0.5:  # UseAline not used
        return 26  # UseAline
    
    if obs[46] > 0.5 and obs[-1] < 88:  # If sats measured and < 88%
        return 30  # UseNonRebreatherMask
    
    if obs[45] > 0.5 and obs[-2] < 60:  # If MAP measured and < 60
        return 15  # GiveFluids
    
    if obs[40] > 0.5 and obs[-7] < 8:  # If resp rate measured and < 8
        return 29  # UseBagValveMask
    
    if obs[38] > 0.5 and obs[-8] > 150:  # If heart rate measured and > 150
        return 9  # GiveAdenosine
    
    if (obs[3] > 0.5 and  # AirwayClear
        obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
        obs[40] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
        obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
        return 48  # Finish
    
    return 16  # ViewMonitor (default action to keep checking vitals)

for line in sys.stdin:
    observations = parse_observations(line)
    action = choose_action(observations)
    print(action)
    sys.stdout.flush()