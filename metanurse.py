import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    # Check for immediate life-threatening conditions
    if obs[7] > 0.5:  # BreathingNone
        return 29  # UseBagValveMask

    # ABCDE assessment
    if state['assessment'] < 5:
        actions = [8, 3, 4, 5, 6, 7]  # ExamineResponse, ExamineAirway, ExamineBreathing, ExamineCirculation, ExamineDisability, ExamineExposure
        action = actions[state['assessment']]
        state['assessment'] += 1
        return action

    # Check vital signs
    if obs[39] <= 0.5:  # MeasuredSats
        return 25  # UseSatsProbe
    if obs[42] <= 0.5:  # MeasuredMAP
        return 27  # UseBloodPressureCuff
    if obs[40] <= 0.5:  # MeasuredRespRate
        return 38  # TakeBloodPressure

    # Get vital signs
    sats = obs[46] if obs[39] > 0.5 else 0
    map = obs[46] if obs[42] > 0.5 else 0
    resp_rate = obs[47] if obs[40] > 0.5 else 0

    # Stabilization actions
    if sats < 88:
        return 30  # UseNonRebreatherMask
    if map < 60:
        return 15  # GiveFluids
    if resp_rate < 8:
        return 29  # UseBagValveMask

    # Check if patient is stabilized
    if sats >= 88 and map >= 60 and resp_rate >= 8:
        return 48  # Finish

    # Timeout mechanism
    if step >= 349:
        return 48  # Finish

    # Default action
    return 16  # ViewMonitor

def main():
    step = 0
    state = {'assessment': 0}
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