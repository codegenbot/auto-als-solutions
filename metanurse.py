import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    sats = obs[46] if obs[39] > 0.5 else 0
    map_value = obs[46] if obs[42] > 0.5 else 0
    resp_rate = obs[47] if obs[43] > 0.5 else 0

    if sats < 65 or map_value < 20:
        return 17  # StartChestCompression

    if state == 'A':
        state = 'B'
        return 3  # ExamineAirway
    elif state == 'B':
        state = 'C'
        return 4  # ExamineBreathing
    elif state == 'C':
        state = 'D'
        return 5  # ExamineCirculation
    elif state == 'D':
        state = 'E'
        return 6  # ExamineDisability
    elif state == 'E':
        state = 'Equipment'
        return 7  # ExamineExposure
    elif state == 'Equipment':
        if obs[18] < 0.5:
            return 18  # OpenAirwayDrawer
        elif obs[19] < 0.5:
            return 19  # OpenBreathingDrawer
        elif obs[20] < 0.5:
            return 20  # OpenCirculationDrawer
        else:
            state = 'Vitals'
    elif state == 'Vitals':
        if obs[39] < 0.5:
            return 25  # UseSatsProbe
        elif obs[42] < 0.5:
            return 27  # UseBloodPressureCuff
        elif obs[43] < 0.5:
            return 38  # TakeBloodPressure
        else:
            state = 'Stabilize'
    elif state == 'Stabilize':
        if sats < 88:
            return 30  # UseNonRebreatherMask
        elif map_value < 60:
            return 15  # GiveFluids
        elif resp_rate < 8:
            return 29  # UseBagValveMask
        elif sats >= 88 and map_value >= 60 and resp_rate >= 8:
            return 48  # Finish
        else:
            state = 'A'

    if step > 300:
        return 48  # Finish

    return 0  # DoNothing

def main():
    step = 0
    state = 'A'
    while True:
        observations = input().strip()
        if not observations:
            break
        obs = parse_observations(observations)
        action = choose_action(obs, step, state)
        print(action)
        sys.stdout.flush()
        step += 1

if __name__ == "__main__":
    main()