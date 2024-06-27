import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    if obs[7] > 0.5:  # BreathingNone
        return 29  # UseBagValveMask

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
        if not state.get('breathing_drawer_opened'):
            state['breathing_drawer_opened'] = True
            return 19  # OpenBreathingDrawer
        if obs[39] <= 0.5:  # MeasuredSats
            return 25  # UseSatsProbe
        if not state.get('circulation_drawer_opened'):
            state['circulation_drawer_opened'] = True
            return 20  # OpenCirculationDrawer
        if obs[42] <= 0.5:  # MeasuredMAP
            return 27  # UseBloodPressureCuff
        if obs[40] <= 0.5:  # MeasuredRespRate
            return 38  # TakeBloodPressure
        if not state.get('monitor_viewed'):
            state['monitor_viewed'] = True
            return 16  # ViewMonitor
        state['assessment_step'] = 'stabilization'

    if state['assessment_step'] == 'stabilization':
        sats = obs[52] if obs[39] > 0.5 else 0
        map = obs[50] if obs[42] > 0.5 else 0
        resp_rate = obs[48] if obs[40] > 0.5 else 0

        if sats < 65 or map < 20:
            state['assessment_step'] = 'cardiac_arrest'
            return 2  # CheckRhythm

        if sats < 88:
            return 30  # UseNonRebreatherMask
        if map < 60:
            return 15  # GiveFluids
        if resp_rate < 8:
            return 29  # UseBagValveMask

        if sats >= 88 and map >= 60 and resp_rate >= 8:
            return 48  # Finish

    if state['assessment_step'] == 'cardiac_arrest':
        if not state.get('chest_compression_started'):
            state['chest_compression_started'] = True
            return 17  # StartChestCompression
        return 23  # ResumeCPR

    if step >= 349:
        return 48  # Finish

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