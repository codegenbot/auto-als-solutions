import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True

    required_measurements = {25, 27, 16, 3}  # SATs Probe, BP Cuff, Monitor, Airway

    def need_measurements():
        return not required_measurements.issubset(actions_taken)

    def need_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    for step in range(max_steps):
        if done: break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        if need_measurements():
            take_action(need_measurement_action())
            continue

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Immediate Life Threatening Actions
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(23)  # Resume CPR
            continue

        # Airway (A)
        if any(events[i] > 0 for i in [4, 5, 6]):  # AirwayVomit, AirwayBlood, AirwayTongue
            take_action(31)  # Use Yankeur Suction Catheter
            continue
        if events[6] > 0:  # AirwayTongue
            take_action(36)  # Perform Head-Tilt Chin-Lift
            continue

        # Breathing (B)
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8: 
            take_action(29)  # Use Bag-Valve Mask
            continue

        # Circulation (C)
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if any(events[i] > 0 for i in range(28, 33)):  # HeartRhythm events indicating arrhythmia
                take_action(24)  # Use Monitor Pads
            else:
                take_action(15)  # Give Fluids
            continue

        # Disability (D)
        if any(events[i] > 0 for i in [19, 20]):  # AVPU_A, AVPU_U
            take_action(6)  # Examine Disability
            continue

        # Exposure (E)
        if any(events[i] > 0 for i in [26, 27]):  # ExposureRash, ExposurePeripherallyShutdown
            take_action(7)  # Examine Exposure
            continue

        take_action(48)  # Finish if stable

if __name__ == "__main__":
    stabilize()