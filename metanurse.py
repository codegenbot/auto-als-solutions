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
        return 25, 'sats_probe'  # UseSatsProbe
    elif state == 'sats_probe':
        return 27, 'bp_cuff'  # UseBloodPressureCuff
    elif state == 'bp_cuff':
        return 16, 'monitor'  # ViewMonitor
    elif state == 'monitor':
        if obs[38] < 0.65 or obs[39] < 20 or obs[35] == 0:
            return 17, 'cpr'  # StartChestCompression
        elif obs[39] < 60:
            return 15, 'fluids'  # GiveFluids
        elif obs[38] < 0.88:
            return 30, 'oxygen'  # UseNonRebreatherMask
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
        if obs[28] > 0:  # NSR
            return 16, 'monitor'
        elif obs[29] > 0:  # SVT
            return 9, 'give_adenosine'
        elif obs[30] > 0 or obs[31] > 0:  # AF or Atrial Flutter
            return 11, 'give_amiodarone'
        elif obs[32] > 0:  # VT
            return 40, 'charge_defib'
        elif obs[38] > 0:  # VF
            return 40, 'charge_defib'
        else:
            return 16, 'monitor'
    elif state == 'fluids':
        return 16, 'monitor'
    elif state == 'oxygen':
        return 16, 'monitor'
    elif state == 'give_adenosine':
        return 16, 'monitor'
    elif state == 'give_amiodarone':
        return 16, 'monitor'
    elif state == 'charge_defib':
        return 41, 'shock'
    elif state == 'shock':
        return 16, 'monitor'
    
    return 16, 'monitor'  # Default to monitoring

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