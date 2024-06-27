import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    if obs[17] < 0.5:  # RadialPulseNonPalpable
        if state.get('rhythm_checked', False):
            return 17  # StartChestCompression
        else:
            state['rhythm_checked'] = True
            return 2  # CheckRhythm

    if state['assessment'] < 5:
        actions = [8, 3, 4, 5, 6, 7]  # ExamineResponse, ExamineAirway, ExamineBreathing, ExamineCirculation, ExamineDisability, ExamineExposure
        action = actions[state['assessment']]
        state['assessment'] += 1
        return action

    if not state.get('breathing_drawer_opened', False):
        state['breathing_drawer_opened'] = True
        return 19  # OpenBreathingDrawer
    
    if not state.get('circulation_drawer_opened', False):
        state['circulation_drawer_opened'] = True
        return 20  # OpenCirculationDrawer

    if obs[39] <= 0.5:  # MeasuredSats
        return 25  # UseSatsProbe
    if obs[42] <= 0.5:  # MeasuredMAP
        return 27  # UseBloodPressureCuff
    if obs[40] <= 0.5:  # MeasuredRespRate
        return 38  # TakeBloodPressure

    if obs[39] > 0.5 or obs[42] > 0.5 or obs[40] > 0.5:
        return 16  # ViewMonitor

    sats = obs[46] if obs[39] > 0.5 else 0
    map = obs[46] if obs[42] > 0.5 else 0
    resp_rate = obs[47] if obs[40] > 0.5 else 0

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

    if sats >= 88 and map >= 60 and resp_rate >= 8:
        return 48  # Finish

    if step >= 349:
        return 48  # Finish

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