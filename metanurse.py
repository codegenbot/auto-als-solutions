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

    def need_measurements():
        return (
            25 not in actions_taken
            or 27 not in actions_taken
            or 16 not in actions_taken
            or 3 not in actions_taken
        )

    def need_measurement_action():
        if 25 not in actions_taken:
            return 25  # UseSatsProbe
        if 27 not in actions_taken:
            return 27  # UseBloodPressureCuff
        if 16 not in actions_taken:
            return 16  # ViewMonitor
        if 3 not in actions_taken:
            return 3  # ExamineAirway
        return None

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        if need_measurements():
            measurement_action = need_measurement_action()
            if measurement_action is not None:
                take_action(measurement_action)
                continue

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if events[4] > 0 or events[5] > 0:
            take_action(31)  # Use suction for vomit or blood
            continue

        if events[6] > 0:
            take_action(36)  # Perform head tilt chin lift for tongue obstruction
            continue

        if events[7] > 0:
            take_action(35)  # Perform airway manoeuvres for no breathing
            continue

        unstable_tachyarrhythmia = any(events[i] > 0 for i in range(29, 36))
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)  # Attach defib pads
                continue
            take_action(40)  # Defibrillator charge
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # Start chest compression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # Bag during CPR
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use nonrebreather mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use bag-valve mask
            continue

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()