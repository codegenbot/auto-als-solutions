import sys

def stabilize():
    max_steps = 350
    steps_taken = 0

    def take_action(action):
        print(action)
        sys.stdout.flush()

    def needs_measurements(actions_taken):
        return not {25, 27, 16, 3}.issubset(actions_taken)

    def next_measurement_action(actions_taken):
        for action in [25, 27, 16, 3]:
            if action not in actions_taken:
                return action

    def has_unstable_tachyarrhythmia(events):
        arrhythmia_events = [31, 32, 33, 34, 35, 36, 37, 38]
        return any(events[i] > 0 for i in arrhythmia_events)
    
    actions_taken = set()

    while steps_taken < max_steps:
        steps_taken += 1
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vhr, vrr, vglucose, vtemp, vmap, vsats, vresps = vital_signs_values
        t_hr, t_rr, t_glucose, t_temp, t_map, t_sats, t_resps = vital_signs_times

        vitals = {
            "RespRate": vrr if t_rr > 0 else None,
            "MAP": vmap if t_map > 0 else None,
            "Sats": vsats if t_sats > 0 else None,
        }

        if needs_measurements(actions_taken):
            take_action(next_measurement_action(actions_taken))
            actions_taken.add(next_measurement_action(actions_taken))
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(23)  # Resume CPR
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if has_unstable_tachyarrhythmia(events):
                if 24 not in actions_taken:
                    take_action(24)  # Use Monitor Pads
                    actions_taken.add(24)
                else:
                    take_action(40)  # Defibrillator Charge
            else:
                take_action(15)  # Give Fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if any(events[i] > 0 for i in [4, 5]):
            take_action(31)  # Use Yankeur Suction Catheter
            continue

        if events[6] > 0:
            take_action(36)  # Perform Head-Tilt Chin-Lift
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(29)  # Use Bag-Valve Mask
            continue

        if any(events[i] > 0 for i in range(1, 4)):
            take_action(8)  # Examine Response
            continue

        take_action(48)  # Finish if stable
        break

if __name__ == "__main__":
    stabilize()