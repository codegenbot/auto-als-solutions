import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()
    actions = {
        "Airway": 3, "Breathing": 4, "Circulation": 5, "Disability": 6,
        "Exposure": 7, "MeasureHR": 25, "MeasureMAP": 27, "MeasureSats": 25,
        "NonRebreatherMask": 30, "GiveFluids": 15, "BagValveMask": 29,
        "AttachDefibPads": 28, "ChestCompression": 17, "Finish": 48
    }

    def initial_checks():
        if "Airway" not in examined:
            take_action(actions["Airway"])
            examined.add("Airway")
        elif "Breathing" not in examined:
            take_action(actions["Breathing"])
            examined.add("Breathing")
        elif "Circulation" not in examined:
            take_action(actions["Circulation"])
            examined.add("Circulation")
        elif "Disability" not in examined:
            take_action(actions["Disability"])
            examined.add("Disability")
        elif "Exposure" not in examined:
            take_action(actions["Exposure"])
            examined.add("Exposure")

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
            "Glucose": values[2] if times[2] > 0 else None,
            "Temp": values[3] if times[3] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
            "Resps": values[6] if times[6] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(actions["ChestCompression"])
            continue

        initial_checks()

        if vitals["HR"] is None:
            take_action(actions["MeasureHR"])
            continue

        if vitals["MAP"] is None:
            take_action(actions["MeasureMAP"])
            continue

        if vitals["Sats"] is None:
            take_action(actions["MeasureSats"])
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(actions["GiveFluids"])
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(actions["NonRebreatherMask"])
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(actions["BagValveMask"])
            continue

        if vitals["HR"] and (vitals["HR"] < 50 or vitals["HR"] > 150):
            take_action(actions["AttachDefibPads"])
            continue

        take_action(actions["Finish"])
        break
    else:
        take_action(actions["Finish"])

if __name__ == "__main__":
    stabilize()