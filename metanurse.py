import sys

def parse_observations(obs):
    return list(map(float, obs.split()))

def choose_action(observations, state, step_count, last_adrenaline):
    obs = parse_observations(observations)
    
    if step_count > 350:
        return 48, state, last_adrenaline  # Finish if timeout

    if state == 'start':
        return 8, 'response', last_adrenaline  # ExamineResponse
    elif state == 'response':
        return 3, 'airway', last_adrenaline  # ExamineAirway
    elif state == 'airway':
        return 4, 'breathing', last_adrenaline  # ExamineBreathing
    elif state == 'breathing':
        return 25, 'sats_probe', last_adrenaline  # UseSatsProbe
    elif state == 'sats_probe':
        return 27, 'bp_cuff', last_adrenaline  # UseBloodPressureCuff
    elif state == 'bp_cuff':
        return 28, 'attach_defib', last_adrenaline  # AttachDefibPads
    elif state == 'attach_defib':
        return 39, 'turn_on_defib', last_adrenaline  # TurnOnDefibrillator
    elif state == 'turn_on_defib':
        return 16, 'monitor', last_adrenaline  # ViewMonitor
    elif state == 'monitor':
        if obs[39] == 0 or obs[38] < 0.65:
            return 17, 'cpr', last_adrenaline  # StartChestCompression
        elif obs[39] < 60 and obs[39] > 20:
            return 15, 'fluids', last_adrenaline  # GiveFluids
        elif obs[38] < 0.88 and obs[38] >= 0.65:
            return 30, 'oxygen', last_adrenaline  # UseNonRebreatherMask
        elif obs[38] >= 0.88 and obs[35] >= 8 and obs[39] >= 60 and obs[3] > 0:
            return 48, 'finish', last_adrenaline  # Finish
        else:
            return 2, 'check_rhythm', last_adrenaline  # CheckRhythm
    elif state == 'cpr':
        if step_count % 32 == 0:
            return 2, 'check_rhythm', last_adrenaline  # CheckRhythm
        elif step_count % 32 == 31:
            return 22, 'cpr', last_adrenaline  # BagDuringCPR
        elif step_count - last_adrenaline >= 60:  # Give Adrenaline every 3-5 minutes (assuming 1 step = 3 seconds)
            return 10, 'cpr', step_count  # GiveAdrenaline
        else:
            return 17, 'cpr', last_adrenaline  # StartChestCompression
    elif state == 'check_rhythm':
        if obs[28] > 0:  # NSR
            return 16, 'monitor', last_adrenaline
        elif obs[29] > 0:  # SVT
            return 9, 'give_adenosine', last_adrenaline
        elif obs[30] > 0 or obs[31] > 0:  # AF or Atrial Flutter
            return 11, 'give_amiodarone', last_adrenaline
        elif obs[32] > 0 or obs[38] > 0:  # VT or VF
            return 40, 'charge_defib', last_adrenaline
        else:
            return 17, 'cpr', last_adrenaline  # StartChestCompression
    elif state == 'fluids':
        return 16, 'monitor', last_adr