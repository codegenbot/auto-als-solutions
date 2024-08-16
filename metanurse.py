import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    assessed = {
        "Airway": False,
        "Breathing": False,
        "Circulation": False,
        "Disability": False,
        "Exposure": False,
    }
    actions = {
        "Airway": 3, "Breathing": 4, "Circulation": 5, "Disability": 6, "Exposure": 7,
        "MeasureHR": 16, "MeasureMAP": 27, "MeasureSats": 25, "NonRebreatherMask": 30,
        "GiveFluids": 15, "BagValveMask": 29, "AttachDefibPads": 28, "ChestCompression": 17,
        "Finish": 48
    }

    def initial_checks():
        if not assessed["Airway"]:
            take_action(actions["Airway"])
            assessed["Airway"] = True
        elif not assessed["Breathing"]:
            take_action(actions["Breathing"])
            assessed["Breathing"] = True
        elif not assessed["Circulation"]:
            take_action(actions["Circulation"])
            assessed["Circulation"] = True
        elif not assessed["Disability"]:
            take_action(actions["Disability"])
            assessed["Disability"] = True
        elif not assessed["Exposure"]:
            take_action(actions["Exposure"])
            assessed["Exposure"] = True

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

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(actions["GiveFluids"])
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(actions["NonRebreatherMask"])
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(actions["BagValveMask"])
            continue

        take_action(actions["Finish"])
        break
    else:
        take_action(actions["Finish"])

if __name__ == "__main__":
    stabilize()