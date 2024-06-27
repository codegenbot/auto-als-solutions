import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, state):
    if obs[7] > 0.5:  # BreathingNone
        return 18 if state['airway_drawer'] == False else 29

    if not state['airway']:
        state['airway'] = True
        return 3
    if not state['breathing']:
        state['breathing'] = True
        return 4
    if not state['circulation']:
        state['circulation'] = True
        return 5
    if not state['disability']:
        state['disability'] = True
        return 6
    if not state['exposure']:
        state['exposure'] = True
        return 7

    recent_sats = obs[45] > 0.5
    recent_map = obs[44] > 0.5
    recent_resp = obs[46] > 0.5

    if not recent_sats:
        return 25
    if not recent_map:
        return 27
    if not recent_resp:
        return 38

    sats = obs[52] if recent_sats else 0
    map = obs[51] if recent_map else 0
    resp_rate = obs[53] if recent_resp else 0

    if sats < 88:
        return 30
    if map < 60:
        return 15
    if resp_rate < 8:
        return 29

    if sats >= 88 and map >= 60 and resp_rate >= 8:
        return 48

    if sats < 65 or map < 20:
        return 17

    return 0

def main():
    state = {
        'airway': False, 'breathing': False, 'circulation': False,
        'disability': False, 'exposure': False, 'airway_drawer': False,
        'step_count': 0
    }
    while state['step_count'] < 350:
        observations = input().strip()
        if not observations:
            break
        obs = parse_observations(observations)
        action = choose_action(obs, state)
        print(action)
        sys.stdout.flush()
        state['step_count'] += 1
        if action == 18:
            state['airway_drawer'] = True
        if action == 48:
            break

if __name__ == "__main__":
    main()