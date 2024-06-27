import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    # Check for cardiac arrest
    if obs[17] > 0.5:  # RadialPulseNonPalpable
        if not state.get('chest_compressions'):
            state['chest_compressions'] = True
            return 17  # StartChestCompression
        return 23  # ResumeCPR

    # ABCDE assessment
    if state['assessment'] < 5:
        actions = [8, 3, 4, 5, 6, 7]  # ExamineResponse, ExamineAirway, ExamineBreathing, ExamineCirculation, ExamineDisability, ExamineExposure
        action = actions[state['assessment']]
        state['assessment'] += 1
        return action

    # Open drawers and attach monitoring devices
    if not state.get('breathing_drawer'):
        state['breathing_drawer'] = True
        return 19  # OpenBreathingDrawer
    if not state.get('sats_probe') and obs[39] <= 0.5:
        state['sats_probe'] = True
        return 25  # UseSatsProbe
    if not state.get('circulation_drawer'):
        state['circulation_drawer'] = True
        return 20  # OpenCirculationDrawer
    if not state.get('bp_cuff') and obs[42] <= 0.5:
        state['bp_cuff'] = True
        return 27  # UseBloodPressureCuff

    # Check rhythm
    if not state.get('rhythm_checked'):
        state['rhythm_checked'] = True
        return 2  # CheckRhythm

    # View monitor to get updated vital signs
    if not state.get('monitor_viewed'):
        state['monitor_viewed'] = True
        return 16  # ViewMonitor

    # Get vital signs
    sats = obs[46] if obs[39] > 0.5 else 0
    map = obs[46] if obs[42] > 0.5 else 0
    resp_rate = obs[47] if obs[40] > 0.5 else 0

    # Interventions based on vital signs
    if sats < 88:
        if sats < 65:
            return 29  # UseBagValveMask
        return 30  # UseNonRebreatherMask
    if map < 60:
        if map < 20:
            return 10  # GiveAdrenaline
        return 15  # GiveFluids
    if resp_rate < 8:
        return 29  # UseBagValveMask

    # Check if patient is stabilized
    if sats >= 88 and map >= 60 and resp_rate >= 8:
        return 48  # Finish

    # Reset monitor view state
    state['monitor_viewed'] = False

    # Timeout mechanism
    if step >= 349:
        return 48  # Finish

    # Default action
    return 0  # DoNothing

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