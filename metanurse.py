import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False
    examination_actions = {3, 4, 5, 6, 7}

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True

    def need_measurements():
        return not all(measured(vital_sign) for vital_sign in [25, 27, 16, 3])

    def measured(vital_sign):
        return vital_sign in actions_taken

    def need_measurement_action():
        for action in [25, 27, 16, 3]:
            if action not in actions_taken:
                return action

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
            take_action(need_measurement_action())
            continue

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(29)  # UseBagValveMask
            continue

        if events[4] > 0 or events[5] > 0:  # Vomit, Blood in Airway
            take_action(31)
            continue

        if events[6] > 0:  # Tongue Obstruction
            take_action(36)
            continue

        if events[7] > 0 or events[10] > 0:  # No Breathing or See-Saw Sign
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if any(events[i] > 0 for i in range(28, 33)):  # Unstable Tachyarrhythmia
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(40)  # DefibrillatorCharge
            continue

        if not any(event > 0 for event in examination_actions):  # Ensure all events are examined
            take_action(3 + step % 4)  # Alternate between ExamineAirway, Breathing, Circulation, Disability
            continue

        if step == max_steps - 1:  # Ensure termination by max steps
            take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()