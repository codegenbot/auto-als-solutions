import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state, steps):
    obs = parse_observations(observations)
    
    if steps >= 349:
        return 48, 'finish'  # Finish if approaching step limit

    if obs[38] < 0.65 or obs[39] < 20:
        return 1, 'cardiac_arrest'  # CheckSignsOfLife

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
        if obs[35] == 0:  # No breathing
            return 29, 'monitor'  # UseBagValveMask
        elif 20 <= obs[39] < 60:
            return 15, 'monitor'  # GiveFluids
        elif 0.65 <= obs[38] < 0.88:
            return 30, 'monitor'  # UseNonRebreatherMask
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60:
            return 48, 'finish'  # Finish
        else:
            return 16, 'monitor'  # ViewMonitor again
    elif state == 'cardiac_arrest':
        return 17, 'cpr'  # StartChestCompression
    elif state == 'cpr':
        return 2, 'check_rhythm'  # CheckRhythm
    elif state == 'check_rhythm':
        if obs[32] > 0 or obs[38] > 0:  # VF or VT
            return 28, 'attach_pads'  # AttachDefibPads
        else:
            return 10, 'give_adrenaline'  # GiveAdrenaline
    elif state == 'attach_pads':
        return 39, 'charge_defib'  # TurnOnDefibrillator
    elif state == 'charge_defib':
        return 40, 'shock'  # DefibrillatorCharge
    elif state == 'shock':
        return 23, 'resume_cpr'  # ResumeCPR
    elif state == 'resume_cpr' or state == 'give_adrenaline':
        return 16, 'monitor'  # ViewMonitor after CPR
    
    return 0, state  # DoNothing

state = 'start'
steps = 0
while True:
    observations = input().strip()
    if not observations:
        break
    action, state = choose_action(observations, state, steps)
    print(action)
    sys.stdout.flush()
    steps += 1