import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    # Check for cardiac arrest conditions
    if obs[46] < 65 or obs[44] < 20:
        return 17  # StartChestCompression

    # ABCDE assessment
    if state['assessment'] < 5:
        actions = [8, 3, 4, 5, 6, 7]  # ExamineResponse, ExamineAirway, ExamineBreathing, ExamineCirculation, ExamineDisability, ExamineExposure
        action = actions[state['assessment']]
        state['assessment'] += 1
        if action == 4:  # After ExamineBreathing
            state['next_action'] = 19  # OpenBreathingDrawer
        elif action == 5:  # After ExamineCirculation
            state['next_action'] = 20  # OpenCirculationDrawer
        return action

    if 'next_action' in state:
        action = state['next_action']
        if action == 19:
            state['next_action'] = 25  # UseSatsProbe
        elif action == 20:
            state['next_action'] = 27  # UseBloodPressureCuff
        elif action in [25, 27]:
            state['next_action'] = 16  # ViewMonitor
        else:
            del state['next_action']
        return action

    # Check vital signs
    sats = obs[46] if obs[39] > 0.5 else 0
    map = obs[44] if obs[42] > 0.5 else 0
    resp_rate = obs[47] if obs[40] > 0.5 else 0

    # Respond to critical conditions
    if obs[7] > 0.5:  # BreathingNone
        if state.get('cpr_cycle', 0) == 0:
            state['cpr_cycle'] = 1
            return 2  # CheckRhythm
        elif state['cpr_cycle'] == 1:
            state['cpr_cycle'] = 2
            return 17  # StartChestCompression
        elif state['cpr_cycle'] == 2:
            state['cpr_cycle'] = 0
            return 10  # GiveAdrenaline

    # Interventions based on vital signs
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