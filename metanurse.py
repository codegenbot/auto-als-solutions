import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step_count, state):
    recent_sats = obs[39] > 0.5
    recent_map = obs[42] > 0.5
    recent_resp = obs[40] > 0.5
    
    sats = obs[46] if recent_sats else 0
    map = obs[46] if recent_map else 0
    resp_rate = obs[47] if recent_resp else 0

    if obs[7] > 0.5:  # BreathingNone
        return 29 if state['airway_drawer_open'] else 18

    if not state['abcde_complete']:
        if not state['airway_checked']:
            state['airway_checked'] = True
            return 3
        elif not state['breathing_checked']:
            state['breathing_checked'] = True
            return 4
        elif not state['circulation_checked']:
            state['circulation_checked'] = True
            return 5
        elif not state['disability_checked']:
            state['disability_checked'] = True
            return 6
        elif not state['exposure_checked']:
            state['exposure_checked'] = True
            state['abcde_complete'] = True
            return 7

    if step_count % 10 == 0:
        if not recent_sats:
            return 25
        elif not recent_map:
            return 27
        elif not recent_resp:
            return 38

    if sats < 65 or map < 20:
        return 17

    if sats < 88:
        return 30
    if map < 60:
        return 15
    if resp_rate < 8:
        return 29

    if sats >= 88 and map >= 60 and resp_rate >= 8:
        return 48

    return 16  # ViewMonitor as default action

def main():
    step_count = 0
    state = {
        'airway_checked': False,
        'breathing_checked': False,
        'circulation_checked': False,
        'disability_checked': False,
        'exposure_checked': False,
        'abcde_complete': False,
        'airway_drawer_open': False
    }

    while step_count < 350:
        observations = input().strip()
        if not observations:
            break
        obs = parse_observations(observations)
        action = choose_action(obs, step_count, state)
        print(action)
        sys.stdout.flush()
        
        if action == 18:
            state['airway_drawer_open'] = True
        elif action == 48:
            break
        
        step_count += 1

if __name__ == "__main__":
    main()