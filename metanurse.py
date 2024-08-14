import sys


def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        return action in [25, 27, 16, 3, 28, 40, 48]

    def need_measurements():
        return 0 in observations[33:40]

    def measure_vitals():
        if 25 not in actions_taken:
            return 25  # UseSatsProbe
        if 27 not in actions_taken:
            return 27  # UseBloodPressureCuff
        if 16 not in actions_taken:
            return 16  # ViewMonitor
        if 3 not in actions_taken:
            return 3  # ExamineAirway
        return None

    def get_vitals():
        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] else None,
        }
        return vitals

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        if take_action(need_measurements()):
            continue

        vitals = get_vitals()

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            if take_action(17):
                continue  # StartChestCompression

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            if take_action(22):
                continue  # BagDuringCPR

        if events[4] > 0 or events[5] > 0:  # Vomit, Blood in Airway
            if take_action(31):
                continue  # UseSuction

        if events[6] > 0:  # Tongue Obstruction
            if take_action(36):
                continue  # HeadTiltChinLift

        if events[7] > 0:  # No Breathing
            if take_action(29):
                continue  # UseBagValveMask

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if take_action(15):
                continue  # GiveFluids

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            if take_action(29):
                continue  # UseBagValveMask

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if take_action(30):
                continue  # UseNonRebreatherMask

        if any(events[i] > 0 for i in range(28, 33)):  # Tachyarrhythmia
            if 28 not in actions_taken and take_action(28):
                continue  # AttachDefibPads
            if take_action(40):  # DefibrillatorCharge
                continue

        take_action(48)


if __name__ == "__main__":
    stabilize()