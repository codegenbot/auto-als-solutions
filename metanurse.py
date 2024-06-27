import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    if obs[7] > 0.5 or obs[46] < 65 or obs[46] < 20:  # BreathingNone or low sats or low MAP
        return start_cpr(state)

    if state['assessment'] < 5:
        return perform_abcde_assessment(state)

    if state['measurement'] < 2:
        return perform_measurements(state)

    sats = obs[46] if obs[39] > 0.5 else 0
    map = obs[46] if obs[42] > 0.5 else 0
    resp_rate = obs[47] if obs[40] > 0.5 else 0

    if sats < 88:
        return 30  # UseNonRebreatherMask
    if map < 60:
        return 15  # GiveFluids
    if resp_rate < 8:
        return 29  # UseBagValveMask

    if sats >= 88 and map >= 60 and resp_rate >= 8:
        return 48  # Finish

    if step >= 349:
        return 48  # Finish

    return 16  # ViewMonitor

def start_cpr(state):
    if state['cpr_step'] == 0:
        state['cpr_step'] = 1
        return 2  # CheckRhythm
    elif state['cpr_step'] == 1:
        state['cpr_step'] = 2
        return 17  # StartChestCompression
    elif state['cpr_step'] == 2:
        state['cpr_step'] = 0
        return 10  # GiveAdrenaline

def perform_abcde_assessment(state):
    actions = [8, 3, 4, 5, 6, 7]
    action = actions[state['assessment']]
    state['assessment'] += 1
    if state['assessment'] == 3:  # After ExamineBreathing
        state['assessment'] -= 1
        return 19  # OpenBreathingDrawer
    elif state['assessment'] == 4:  # After ExamineCirculation
        state['assessment'] -= 1
        return 20  # OpenCirculationDrawer
    return action

def perform_measurements(state):
    if state['measurement'] == 0:
        state['measurement'] += 1
        return 25  # UseSatsProbe
    elif state['measurement'] == 1:
        state['measurement'] += 1
        return 27  # UseBloodPressureCuff
    else:
        return 16  # ViewMonitor

def main():
    step = 0
    state = {'assessment': 0, 'measurement': 0, 'cpr_step': 0}
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