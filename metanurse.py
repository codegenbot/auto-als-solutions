import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

    def measure_all_vitals():
        if "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
        elif "BP" not in examined:
            take_action(27)
            examined.add("BP")
        elif "SatsProbe" not in examined:
            take_action(25)
            examined.add("SatsProbe")
        elif "RespRate" not in examined:
            take_action(4)
            examined.add("RespRate")

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] != 0 else None,
            "RR": values[1] if times[1] != 0 else None,
            "Glucose": values[2] if times[2] != 0 else None,
            "Temp": values[3] if times[3] != 0 else None,
            "MAP": values[4] if times[4] != 0 else None,
            "Sats": values[5] if times[5] != 0 else None,
            "Resps": values[6] if times[6] != 0 else None,
        }

        # Check for critical conditions
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        # Perform ABCDE assessment steps
        if "airway" not in examined:
            take_action(3)
            examined.add("airway")
            continue
        if "breathing" not in examined:
            take_action(4)
            examined.add("breathing")
            continue
        if "circulation" not in examined:
            take_action(5)
            examined.add("circulation")
            continue
        if "disability" not in examined:
            take_action(6)
            examined.add("disability")
            continue
        if "exposure" not in examined:
            take_action(7)
            examined.add("exposure")
            continue

        # Measure all vitals if assessments are done
        measure_all_vitals()

        # Treatment for unstable vitals
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        # If respiration-related emergencies like a tension pneumothorax
        if events[29] > 0 or events[30] > 0:
            take_action(40)
            take_action(41)
            take_action(43)
            continue

        # Finalize if all conditions are met
        if (vitals["Sats"] is not None and vitals["Sats"] >= 88 and
            vitals["RR"] is not None and vitals["RR"] >= 8 and
            vitals["MAP"] is not None and vitals["MAP"] >= 60):
            take_action(48)
            break

    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()