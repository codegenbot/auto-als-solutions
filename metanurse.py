import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    # Check for immediate life-threatening conditions
    if obs[7] > 0.5:  # BreathingNone
        return 29  # UseBagValveMask

    # ABCDE assessment state machine
    if state['assessment_step'] == 'response':
        state['assessment_step'] = 'airway'
        return 8  # ExamineResponse
    elif state['assessment_step'] == 'airway':
        state['assessment_step'] = 'breathing'
        return 3  # ExamineAirway
    elif state['assessment_step'] == 'breathing':
        state['assessment_step'] = 'circulation'
        return 4  # ExamineBreathing
    elif state['assessment_step'] == 'circulation':
        state['assessment_step'] = 'disability'
        return 5  # ExamineCirculation
    elif state['assessment_step'] == 'disability':
        state['assessment_step'] = 'exposure'
        return 6  # ExamineDisability
    elif state['assessment_step'] == 'exposure':
        state['assessment_step'] = 'measurements'
        return 7  # ExamineExposure

    # Take vital measurements
    if state['assessment_step'] == 'measurements':
        if obs[39] <= 0.5:  # MeasuredSats
            return 25  # UseSatsProbe
        if obs[42] <= 0.5:  # MeasuredMAP
            return 27  # UseBloodPressureCuff
        if obs[40] <= 0.5:  # MeasuredRespRate
            return 38  # TakeBloodPressure
        state['assessment_step'] = 'stabilization'

    # Stabilization actions
    if state['assessment_step'] == 'stabilization':
        sats = obs[46] if obs[39] > 0.5 else 0
        map = obs[46] if obs[42] > 0.5 else 0
        resp_rate = obs[47] if obs[40] > 0.5 else 0

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
    return 0  # DoNothing

def main():
    step = 0
    state = {'assessment_step': 'response'}
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