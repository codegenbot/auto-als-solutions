import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, last_action):
    if obs[7] > 0:  # BreathingNone detected
        return 29  # UseBagValveMask
    if obs[0] == 0 and obs[1] == 0 and obs[2] == 0:
        return 8  # ExamineResponse
    if obs[3] == 0 and obs[4] == 0 and obs[5] == 0 and obs[6] == 0:
        return 3  # ExamineAirway
    if obs[7] == 0 and obs[8] == 0 and obs[9] == 0 and obs[10] == 0:
        return 4  # ExamineBreathing
    if obs[16] == 0 and obs[17] == 0:
        return 5  # ExamineCirculation
    if obs[20] == 0 and obs[21] == 0 and obs[22] == 0:
        return 6  # ExamineDisability
    if obs[25] == 0 and obs[26] == 0:
        return 7  # ExamineExposure
    if obs[44] == 0:
        if obs[19] == 0:
            return 19  # OpenBreathingDrawer
        return 25  # UseSatsProbe
    if obs[45] == 0:
        if obs[20] == 0:
            return 20  # OpenCirculationDrawer
        return 27  # UseBloodPressureCuff
    if obs[46] > 0 and obs[52] < 88:
        return 30  # UseNonRebreatherMask
    if obs[45] > 0 and obs[51] < 60:
        return 15  # GiveFluids
    if obs[17] > 0 or (obs[46] > 0 and obs[52] < 65) or (obs[45] > 0 and obs[51] < 20):
        if last_action != 17:
            return 17  # StartChestCompression
        else:
            return 23  # ResumeCPR
    if obs[28] == 0:
        return 2  # CheckRhythm
    if obs[28] > 0 and any(obs[29:39]):
        if obs[32] > 0:  # HeartRhythmVT
            return 11  # GiveAmiodarone
        if obs[38] > 0:  # HeartRhythmVF
            if last_action != 40:
                return 40  # DefibrillatorCharge
            else:
                return 41  # DefibrillatorCurrentUp
    if obs[46] > 0 and obs[52] >= 88 and obs[47] > 0 and obs[53] >= 8 and obs[45] > 0 and obs[51] >= 60:
        return 48  # Finish
    return 16  # ViewMonitor (regularly check vital signs)

step_count = 0
last_action = -1
while True:
    try:
        observations = input()
        obs = parse_observations(observations)
        action = choose_action(obs, last_action)
        print(action)
        sys.stdout.flush()
        if action == 48 or step_count >= 349:
            break
        last_action = action
        step_count += 1
    except EOFError:
        break
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)