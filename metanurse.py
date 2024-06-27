import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    if obs[7] > 0.5 or obs[46] < 65 or obs[44] < 20:  # BreathingNone or low sats or low MAP
        return handle_cardiac_arrest(state)

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

    if state['assessment_step'] == 'measurements':
        return take_measurements(obs, state)

    if state['assessment_step'] == 'stabilization':
        return stabilize_patient(obs, state)

    if step >= 349:
        return 48  # Finish

    return 0  # DoNothing

def handle_cardiac_arrest(state):
    if 'cpr_started' not in state:
        state['cpr_started'] = True
        return 17  # StartChestCompression
    return 23  # ResumeCPR

def take_measurements(obs, state):
    if obs[39] <= 0.5:  # MeasuredSats
        if 'breathing_drawer_opened' not in state:
            state['breathing_drawer_opened'] = True
            return 19  # OpenBreathingDrawer
        return 25  # UseSatsProbe
    if obs[42] <= 0.5:  # MeasuredMAP
        if 'circulation_drawer_opened' not in state:
            state['circulation_drawer_opened'] = True
            return 20  # OpenCirculationDrawer
        return 27  # UseBloodPressureCuff
    if obs[40] <= 0.5:  # MeasuredRespRate
        return 38  # TakeBloodPressure
    state['assessment_step'] = 'stabilization'
    return 16  # ViewMonitor

def stabilize_patient(obs, state):
    sats = obs[46] if obs[39] > 0.5 else 0
    map = obs[44] if obs[42] > 0.5 else 0
    resp_rate = obs[47] if obs[40] > 0.5 else 0

    if sats < 88:
        return 30  # UseNonRebreatherMask
    if map < 60:
        return 15  # GiveFluids
    if resp_rate < 8:
        return 29  # UseBagValveMask

    if sats >= 88 and map >= 60 and resp_rate >= 8:
        return 48  # Finish

    return 16  # ViewMonitor

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
        if action == 48:  # Finish
            break

if __name__ == "__main__":
    main()