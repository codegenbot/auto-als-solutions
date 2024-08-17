import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def get_observations():
        try:
            return list(map(float, input().strip().split()))
        except:
            take_action(48)
            sys.exit()

    steps, examined, actions = 350, set(), {
        "ExamineAirway": 3, "ExamineBreathing": 4, "ExamineCirculation": 5,
        "UseSatsProbe": 25, "UseBloodPressureCuff": 27, "ViewMonitor": 16,
        "UseNonRebreatherMask": 30, "GiveFluids": 15, "UseBagValveMask": 29,
        "GiveAtropine": 12, "GiveAdenosine": 9, "StartChestCompression": 17,
        "CheckRhythm": 2, "Finish": 48
    }

    for _ in range(steps):
        observations = get_observations()
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        measured_recent = observations[33:40]
        measurements = observations[46:]

        vitals = {
            "HR": measurements[0] if measured_recent[0] > 0 else None,
            "RR": measurements[1] if measured_recent[1] > 0 else None,
            "Glucose": measurements[2] if measured_recent[2] > 0 else None,
            "Temp": measurements[3] if measured_recent[3] > 0 else None,
            "MAP": measurements[4] if measured_recent[4] > 0 else None,
            "Sats": measurements[5] if measured_recent[5] > 0 else None,
            "Resps": measurements[6] if measured_recent[6] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(actions["StartChestCompression"])
            continue

        if not any(events[3:7]) and "Airway" not in examined:
            take_action(actions["ExamineAirway"])
            examined.add("Airway")
            continue

        if vitals["Sats"] is None and "Sats" not in examined:
            take_action(actions["UseSatsProbe"])
            examined.add("Sats")
            continue

        if vitals["MAP"] is None and "MAP" not in examined:
            take_action(actions["UseBloodPressureCuff"])
            examined.add("MAP")
            continue

        if "Breathing" not in examined:
            take_action(actions["ExamineBreathing"])
            examined.add("Breathing")
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(actions["UseNonRebreatherMask"])
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(actions["GiveFluids"])
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(actions["UseBagValveMask"])
            continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(actions["CheckRhythm"])
                continue
            elif vitals["HR"] < 50:
                take_action(actions["GiveAtropine"])
                continue

        take_action(actions["Finish"])
        break
    else:
        take_action(actions["Finish"])

if __name__ == "__main__":
    stabilize()