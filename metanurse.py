import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state):
    if state['step'] == 0:
        return 2, {'step': 1}  # CheckRhythm
    elif state['step'] == 1:
        return 24, {'step': 2}  # UseMonitorPads
    elif state['step'] == 2:
        return 19, {'step': 3}  # OpenBreathingDrawer
    elif obs[7] > 0:  # BreathingNone detected
        return 17, {'step': 4}  # StartChestCompression
    elif state['step'] == 3:
        return 27, {'step': 4}  # UseBloodPressureCuff
    elif state['step'] == 4:
        return 30, {'step': 5}  # UseNonRebreatherMask
    elif obs[0] == 0 and obs[1] == 0 and obs[2] == 0:
        return 8, state  # ExamineResponse
    elif obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
        return 3, state  # ExamineAirway
    elif obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
        return 4, state  # ExamineBreathing
    elif obs[16] == 0 and obs[17] == 0:
        return 5, state  # ExamineCirculation
    elif obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
        return 6, state  # ExamineDisability
    elif obs[25] == 0 and obs[26] == 0:
        return 7, state  # ExamineExposure
    elif obs[45] > 0 and obs[51] < 60:
        return 15, state  # GiveFluids
    elif obs[46] > 0 and obs[52] < 65 or (obs[45] > 0 and obs[51] < 20):
        return 10, state  # GiveAdrenaline
    elif obs[28] > 0 and any(obs[29:39]):
        if obs[32] > 0:  # HeartRhythmVT
            return 11, state  # GiveAmiodarone
        if obs[38] > 0:  # HeartRhythmVF
            return 40, state  # DefibrillatorCharge
    elif obs[46] > 0 and obs[52] >= 88 and obs[47] > 0 and obs[53] >= 8 and obs[45] > 0 and obs[51] >= 60:
        return 48, state  # Finish
    return 16, state  # ViewMonitor

step_count = 0
state = {'step': 0}
while True:
    observations = input()
    obs = parse_observations(observations)
    action, state = choose_action(obs, state)
    print(action)
    sys.stdout.flush()
    if action == 48 or step_count >= 349:
        break
    step_count += 1