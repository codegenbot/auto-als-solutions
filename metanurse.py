import sys


def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action, break_action=True):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True
        return break_action

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
                if take_action(measurement_action):
                    continue

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if events[4] > 0 or events[5] > 0:  # Vomit, Blood in Airway
            if take_action(31):
                continue  # UseSuction

        if events[6] > 0:  # Tongue Obstruction
            if take_action(36):
                continue  # HeadTiltChinLift

        if events[7] > 0:  # No Breathing
            if 29 not in actions_taken and take_action(29):
                continue  # UseBagValveMask

        if any(events[i] > 0 for i in range(28, 33)):  # Unstable Tachyarrhythmia
            if 28 not in actions_taken and take_action(28):
                continue  # AttachDefibPads
            if take_action(40):  # DefibrillatorCharge
                continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            if take_action(17):
                continue  # StartChestCompression

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            if take_action(22):
                continue  # BagDuringCPR

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if take_action(15):
                continue  # GiveFluids

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if take_action(30):
                continue  # UseNonRebreatherMask

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            if take_action(29):
                continue  # UseBagValveMask

        if actions_taken == {25, 27, 16, 3}:
            if take_action(48, False):  # Finish only when all measurements are taken
                break


if __name__ == "__main__":
    stabilize()