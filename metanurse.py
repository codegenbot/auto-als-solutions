import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    if 'drawers_opened' not in state:
        state['drawers_opened'] = False
        state['abcde_step'] = 0
        state['breathing_none_count'] = 0
        state['last_vitals_check'] = -10

    if not state['drawers_opened']:
        state['drawers_opened'] = True
        return 18  # OpenAirwayDrawer

    if obs[7] > 0.5:  # BreathingNone
        state['breathing_none_count'] += 1
        if state['breathing_none_count'] > 2:
            return 17  # StartChestCompression
        return 29  # UseBagValveMask

    state['breathing_none_count'] = 0

    if step - state['last_vitals_check'] >= 10:
        state['last_vitals_check'] = step
        return 25 if step % 3 == 0 else 27 if step % 3 == 1 else 38

    sats = obs[46] if obs[39] > 0.5 else 0
    map = obs[46] if obs[42] > 0.5 else 0
    resp_rate = obs[47] if obs[40] > 0.5 else 0

    if sats < 88:
        return 30  # UseNonRebreatherMask
    if map < 60:
        return 15  # GiveFluids
    if resp_rate < 8:
        return 29  # UseBagValveMask

    abcde_actions = [3, 4, 5, 6, 7]
    if state['abcde_step'] < len(abcde_actions):
        action = abcde_actions[state['abcde_step']]
        state['abcde_step'] += 1
        return action

    if sats >= 88 and map >= 60 and resp_rate >= 8:
        return 48  # Finish

    if step >= 340:
        return 48  # Finish

    return 0  # DoNothing

def main():
    step = 0
    state = {}
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