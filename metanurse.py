import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    sats = obs[46] if obs[39] > 0.5 else 0
    map_value = obs[46] if obs[42] > 0.5 else 0
    resp_rate = obs[47] if obs[43] > 0.5 else 0
    heart_rate = obs[44] if obs[37] > 0.5 else 0

    if sats < 65 or map_value < 20:
        return 17, "CPR"  # StartChestCompression

    if state == "A":
        if obs[3] < 0.5:
            return 3, "A"  # ExamineAirway
        return 29, "B"  # UseBagValveMask
    elif state == "B":
        if obs[39] < 0.5:
            return 25, "B"  # UseSatsProbe
        if sats < 88:
            return 30, "B"  # UseNonRebreatherMask
        return 4, "C"  # ExamineBreathing
    elif state == "C":
        if obs[42] < 0.5:
            return 27, "C"  # UseBloodPressureCuff
        if map_value < 60:
            return 15, "C"  # GiveFluids
        return 5, "D"  # ExamineCirculation
    elif state == "D":
        return 6, "E"  # ExamineDisability
    elif state == "E":
        return 7, "Stabilize"  # ExamineExposure
    elif state == "Stabilize":
        if sats >= 88 and map_value >= 60 and resp_rate >= 8:
            return 48, "Finish"  # Finish
        return 16, "Stabilize"  # ViewMonitor

    if step > 300:
        return 48, "Finish"  # Finish

    return 0, state  # DoNothing

def main():
    step = 0
    state = "A"
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