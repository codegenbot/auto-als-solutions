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

        # Handle airway issues first
        if events[4] > 0 or events[5] > 0:  # Vomit, Blood in Airway
            if take_action(31):
                continue  # UseSuction
        if events[6] > 0:  # Tongue Obstruction
            if take_action(36):
                continue  # HeadTiltChinLift

        # Handle breathing issues
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            if take_action(29):
                continue  # UseBagValveMask
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if take_action(30):
                continue  # UseNonRebreatherMask

        # Handle circulation issues
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if take_action(15):
                continue  # GiveFluids

        # Finish the process when stabilized criteria met
        if (vitals["MAP"] is not None and vitals["MAP"] >= 60 and
            vitals["Sats"] is not None and vitals["Sats"] >= 88 and
            vitals["RespRate"] is not None and vitals["RespRate"] >= 8):
            if take_action(48, False):  # Finish
                break

if __name__ == "__main__":
    stabilize()