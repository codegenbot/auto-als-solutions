import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state, step_count):
    obs = parse_observations(observations)
    
    if step_count > 350:
        return 48, 'finish'  # Finish if timeout

    if state == 'start':
        return 8, 'response'  # ExamineResponse
    elif state == 'response':
        return 3, 'airway'  # ExamineAirway
    elif state == 'airway':
        return 4, 'breathing'  # ExamineBreathing
    elif state == 'breathing':
        return 29, 'bag_mask'  # UseBagValveMask
    elif state == 'bag_mask':
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
    elif state == 'monitor':
        if obs[38] < 0.65 or obs[39] < 20:
            return 17, 'cpr'  # StartChestCompression
        elif obs[35] == 0:  # No breathing
            return 29, 'monitor'  # UseBagValveMask
        elif obs[39] < 60:
            return 15, 'monitor'  # GiveFluids
        elif obs[38] < 0.88:
            return 30, 'monitor'  # UseNonRebreatherMask
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60 and obs[3] > 0:
            return 48, 'finish'  # Finish
        else:
            return 2, 'check_rhythm'  # CheckRhythm
    elif state == 'cpr':
        if step_count % 5 == 0:
            return 28, 'attach_defib'  # AttachDefibPads
        elif step_count % 5 == 1:
            return 39, 'turn_on_defib'  # TurnOnDefibrillator
        elif step_count % 5 == 2:
            return 40, 'charge_defib'  # DefibrillatorCharge
        elif step_count % 5 == 3:
            return 10, 'give_adrenaline'  # GiveAdrenaline
        else:
            return 16, 'monitor'  # ViewMonitor
    elif state == 'check_rhythm':
        return 16, 'monitor'  # ViewMonitor
    
    return 0, state  # DoNothing

state = 'start'
step_count = 0
while True:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state, step_count)
    print(action)
    sys.stdout.flush()
    step_count += 1