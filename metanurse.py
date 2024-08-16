import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()
    actions_map = {
        "CPR": 17,
        "MAP_Cuff": 27,
        "Sats_Probe": 25,
        "Breathing": 4,
        "Airway": 3,
        "Fluids": 15,
        "NonRebreather": 30,
        "BagValveMask": 29,
        "ViewMonitor": 16,
        "Finish": 48
    }

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(actions_map["Finish"])
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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(actions_map["CPR"])
            continue

        if vitals["MAP"] is None and "MAP" not in examined_vitals:
            take_action(actions_map["MAP_Cuff"])
            examined_vitals.add("MAP")
            continue

        if vitals["Sats"] is None and "Sats" not in examined_vitals:
            take_action(actions_map["Sats_Probe"])
            examined_vitals.add("Sats")
            continue

        if vitals["RR"] is None and "RR" not in examined_vitals:
            take_action(actions_map["Breathing"])
            examined_vitals.add("RR")
            continue

        if not all(events[3:7]):
            take_action(actions_map["Airway"])
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(actions_map["NonRebreather"])
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(actions_map["Fluids"])
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(actions_map["BagValveMask"])
            continue

        take_action(actions_map["Finish"])
        break

if __name__ == "__main__":
    stabilize()