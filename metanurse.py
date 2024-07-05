import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state):
    if state == "start":
        return 24, "monitor_pads"  # UseMonitorPads
    elif state == "monitor_pads":
        return 25, "sats_probe"  # UseSatsProbe
    elif state == "sats_probe":
        return 27, "bp_cuff"  # UseBloodPressureCuff
    elif state == "bp_cuff":
        return 3, "airway"  # ExamineAirway
    elif state == "airway":
        return 4, "breathing"  # ExamineBreathing
    elif state == "breathing":
        return 5, "circulation"  # ExamineCirculation
    elif state == "circulation":
        return 6, "disability"  # ExamineDisability
    elif state == "disability":
        return 7, "exposure"  # ExamineExposure
    elif state == "exposure":
        return 16, "assess"  # ViewMonitor

    # Assess vitals and treat
    if state == "assess":
        if obs[39] > 0.5 and obs[-7] < 8:  # RespRate measured and < 8
            return 29, "assess"  # UseBagValveMask
        elif obs[46] > 0.5 and obs[-1] < 88:  # Sats measured and < 88%
            return 30, "assess"  # UseNonRebreatherMask
        elif obs[45] > 0.5 and obs[-2] < 60:  # MAP measured and < 60
            return 15, "assess"  # GiveFluids
        elif obs[38] > 0.5 and obs[-8] > 150:  # HeartRate measured and > 150
            return 9, "assess"  # GiveAdenosine
        elif (obs[3] > 0.5 and  # AirwayClear
              obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
              obs[39] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
              obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
            return 48, "finish"  # Finish
        else:
            return 16, "assess"  # ViewMonitor

    return 0, state  # DoNothing

state = "start"
for line in sys.stdin:
    observations = parse_observations(line)
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()