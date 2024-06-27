import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state, step_count):
    obs = parse_observations(observations)
    
    if step_count >= 349:
        return 48, 'finish'  # Finish action if reaching step limit
    
    # Check for cardiac arrest conditions
    if obs[38] < 0.65 or obs[39] < 20:
        return 1, 'cardiac_arrest'  # CheckSignsOfLife
    
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
    elif state == 'monitor':
        if obs[35] == 0:  # No breathing
            return 29, 'monitor'  # UseBagValveMask
        elif obs[39] < 60 and obs[39] >= 20:
            return 15, 'monitor'  # GiveFluids
        elif obs[38] < 0.88 and obs[38] >= 0.65:
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
        if obs[32] > 0 or obs[33] > 0:  # VF or VT
            return 28, 'attach_defib'  # AttachDefibPads
        else:
            return 23, 'resume_cpr'  # ResumeCPR
    elif state == 'attach_defib':
        return 39, 'turn_on_defib'  # TurnOnDefibrillator
    elif state == 'turn_on_defib':
        return 40, 'charge_defib'  # DefibrillatorCharge
    elif state == 'charge_defib':
        return 10, 'give_adrenaline'  # GiveAdrenaline
    elif state == 'give_adrenaline':
        return 23, 'resume_cpr'  # ResumeCPR
    elif state == 'resume_cpr':
        return 16, 'monitor'  # ViewMonitor after CPR
    
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