import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    step = 0

    while step < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        def measure_vitals():
            if vitals["Sats"] is None and 25 not in actions_taken:
                actions_taken.add(25)
                take_action(25)  # UseSatsProbe
                return True
            if vitals["MAP"] is None and 27 not in actions_taken:
                actions_taken.add(27)
                take_action(27)  # UseBloodPressureCuff
                return True
            if vitals["RR"] is None and 24 not in actions_taken:
                actions_taken.add(24)
                take_action(24)  # UseMonitorPads
                return True
            return False

        if measure_vitals():
            continue

        # Cardiac arrest conditions
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
                vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        # A - Airway
        for i in range(3, 7):
            if events[i] > 0:
                take_action(3)
                if events[5] > 0:
                    take_action(31)
                if events[6] > 0:
                    take_action(32)
                break
        else:
            # B - Breathing
            for i in range(7, 15):
                if events[i] > 0:
                    take_action(4)
                    break
            else:
                if vitals["Sats"] is not None and vitals["Sats"] < 88:
                    take_action(30)
                elif vitals["RR"] is not None and vitals["RR"] < 8:
                    take_action(29)
                # C - Circulation
                elif vitals["MAP"] is not None and vitals["MAP"] < 60:
                    take_action(15)
                elif any(events[i] > 0 for i in range(15, 20)):
                    take_action(5)
                # D - Disability
                elif any(events[i] > 0 for i in range(20, 26)):
                    take_action(6)
                # E - Exposure
                elif any(events[i] > 0 for i in range(26, 33)):
                    take_action(7)
                # Ensure necessary measurements
                elif measure_vitals():
                    continue
                else:
                    take_action(48)  # Finish
                    break
        step += 1

if __name__ == "__main__":
    stabilize()