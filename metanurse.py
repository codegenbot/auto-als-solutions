import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state):
    obs = parse_observations(observations)
    
    if obs[38] < 0.65 or obs[39] < 20:
        return 17, 'cpr'  # StartChestCompression

    if state == 'cpr':
        if obs[27] == 0:
            return 28, 'attach_defib'  # AttachDefibPads
        elif obs[28] == 0:
            return 39, 'turn_on_defib'  # TurnOnDefibrillator
        elif obs[29] == 0:
            return 40, 'charge_defib'  # DefibrillatorCharge
        else:
            return 16, 'monitor'  # ViewMonitor

    if state == 'start':
        return 8, 'response'  # ExamineResponse
    elif state == 'response':
        return 3, 'airway'  # ExamineAirway
    elif state == 'airway':
        return 4, 'breathing'  # ExamineBreathing
    elif state == 'breathing':
        return 5, 'circulation'  # ExamineCirculation
    elif state == 'circulation':
        return 27, 'bp_cuff'  # UseBloodPressureCuff
    elif state == 'bp_cuff':
        return 6, 'disability'  # ExamineDisability
    elif state == 'disability':
        return 7, 'exposure'  # ExamineExposure
    elif state == 'exposure':
        return 25, 'sats_probe'  # UseSatsProbe
    elif state == 'sats_probe':
        return 16, 'monitor'  # ViewMonitor

    if obs[7] > 0:  # BreathingNone
        return 29, 'bag_mask'  # UseBagValveMask

    if obs[39] < 60:
        return 15, 'fluids'  # GiveFluids

    if obs[38] < 0.88:
        return 30, 'oxygen'  # UseNonRebreatherMask

    if obs[3] > 0 and obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
        return 48, 'finish'  # Finish if stabilized

    return 16, 'monitor'  # ViewMonitor

state = 'start'
while True:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state)
    print(action)
    sys.stdout.flush()