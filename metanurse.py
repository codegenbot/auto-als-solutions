import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        # Critical failure check
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # StartChestCompression
            continue

        # Airway assessment and treatment
        if any(events[i] > 0 for i in range(3, 7)) and "airway" not in examined_vitals:
            take_action(3)  # ExamineAirway
            examined_vitals.add("airway")
            continue

        # Ensure oxygen saturation measurement
        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(25)  # UseSatsProbe
            examined_vitals.add("Sats")
            continue

        # Treat low oxygen saturation
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            if "mask" not in examined_vitals:
                take_action(30)  # UseNonRebreatherMask
                examined_vitals.add("mask")
            else:
                take_action(29)  # UseBagValveMask
            continue

        # Breathing assessment
        if any(events[i] > 0 for i in range(7, 15)) and "breathing" not in examined_vitals:
            take_action(4)  # ExamineBreathing
            examined_vitals.add("breathing")
            continue

        # Ensure MAP measurement
        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(27)  # UseBloodPressureCuff
            examined_vitals.add("MAP")
            continue

        # View monitor for MAP
        if vitals["MAP"] is None and "monitor" not in examined_vitals:
            take_action(16)  # ViewMonitor
            examined_vitals.add("monitor")
            continue

        # Treat low MAP
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Disability assessment
        if any(events[i] > 0 for i in range(20, 26)) and "disability" not in examined_vitals:
            take_action(6)  # ExamineDisability
            examined_vitals.add("disability")
            continue

        # Exposure assessment
        if any(events[i] > 0 for i in range(26, 33)) and "exposure" not in examined_vitals:
            take_action(7)  # ExamineExposure
            examined_vitals.add("exposure")
            continue

        # Check if John is stabilized
        if (vitals["Sats"] is not None and vitals["Sats"] >= 88 and 
            vitals["RR"] is not None and vitals["RR"] >= 8 and 
            vitals["MAP"] is not None and vitals["MAP"] >= 60):
            take_action(48)  # Finish
            break

if __name__ == "__main__":
    stabilize()