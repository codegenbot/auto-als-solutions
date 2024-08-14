import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    def has_observations(vital_signs_times):
        return all(t > 0 for t in vital_signs_times)

    def get_unstable_tachyarrhythmia(events):
        tachy_events = [31, 32, 33, 34, 35, 36, 37, 38]
        return any(events[i] > 0 for i in tachy_events)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        if not has_observations(vital_signs_times):
            for i, action in enumerate([25, 27, 16, 3]):
                if action not in actions_taken:
                    take_action(action)
                    break
            continue

        # Vital Sign Values
        RespRate = vital_signs_values[1] if vital_signs_times[1] > 0 else None
        MAP = vital_signs_values[4] if vital_signs_times[4] > 0 else None
        Sats = vital_signs_values[5] if vital_signs_times[5] > 0 else None

        # Check for critical conditions first
        if (MAP is not None and MAP < 20) or (Sats is not None and Sats < 65):
            take_action(23)
            continue

        if MAP is not None and MAP < 60:
            if get_unstable_tachyarrhythmia(events):
                if 24 not in actions_taken:
                    take_action(24)
                else:
                    take_action(40)  # Cardiovert
            else:
                take_action(15)  # Give fluids
            continue

        if Sats is not None and Sats < 88:
            take_action(30)
            continue

        if RespRate is not None and RespRate < 8:
            take_action(29)
            continue

        # Assess and manage airway
        if any(events[e] > 0 for e in [4, 5]):
            take_action(31)  # Use Yankeur Suction Catheter
            continue
        if events[6] > 0:
            take_action(36)  # Perform Head Tilt Chin Lift
            continue

        # Respond to critical breathing issues
        if any(events[e] > 0 for e in [7, 10, 11, 12, 13, 14]):
            take_action(29)  # Use Bag Valve Mask
            continue

        # Assess responsiveness
        if any(events[e] > 0 for e in [1, 2, 3]):
            take_action(8)  # Examine Response
            continue

        # If all checks pass and no critical action needed, finalize
        take_action(48)
        break

if __name__ == "__main__":
    stabilize()