import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    sats = obs[46] if obs[39] > 0.5 else 0
    map_value = obs[47] if obs[42] > 0.5 else 0
    resp_rate = obs[48] if obs[43] > 0.5 else 0
    heart_rate = obs[44] if obs[37] > 0.5 else 0

    # Check for cardiac arrest
    if sats < 65 or map_value < 20:
        return 17, 'CPR'  # StartChestCompression

    if state == 'START':
        return 25, 'A'  # UseSatsProbe
    elif state == 'A':
        return 3, 'B'  # ExamineAirway
    elif state == 'B':
        return 4, 'C'  # ExamineBreathing
    elif state == 'C':
        return 27, 'D'  # UseBloodPressureCuff
    elif state == 'D':
        return 6, 'E'  # ExamineDisability
    elif state == 'E':
        return 7, 'INTERVENE'  # ExamineExposure

    # Interventions based on vital signs
    if state == 'INTERVENE':
        if sats < 88:
            return 30, 'INTERVENE'  # UseNonRebreatherMask
        elif map_value < 60:
            return 15, 'INTERVENE'  # GiveFluids
        elif resp_rate < 8:
            return 29, 'INTERVENE'  # UseBagValveMask
        elif sats >= 88 and map_value >= 60 and resp_rate >= 8:
            return 48, 'FINISH'  # Finish
        else:
            return 16, 'START'  # ViewMonitor

    # Timeout mechanism
    if step > 300:
        return 48, 'FINISH'  # Finish

    return 0, state  # DoNothing

def main():
    step = 0
    state = 'START'
    while True:
        observations = input().strip()
        if not observations:
            break
        obs = parse_observations(observations)
        action, new_state = choose_action(obs, step, state)
        print(action)
        sys.stdout.flush()
        step += 1
        state = new_state

if __name__ == "__main__":
    main()