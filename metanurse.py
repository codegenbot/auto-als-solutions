import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()
    actions = {
        "airway": 3, "breathing": 4, "circulation": 5, "disability": 6, "exposure": 7,
        "SatsProbe": 25, "BPCuff": 27,
        "NonRebreatherMask": 30, "BagValveMask": 29, "GiveFluids": 15,
        "ChestCompression": 17
    }

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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(actions["ChestCompression"])
            continue

        if "airway" not in examined_vitals:
            take_action(actions["airway"])
            examined_vitals.add("airway")
            continue
        
        if "breathing" not in examined_vitals:
            take_action(actions["breathing"])
            examined_vitals.add("breathing")
            continue
        
        if vitals["Sats"] is None:
            take_action(actions["SatsProbe"])
            continue

        if vitals["MAP"] is None:
            take_action(actions["BPCuff"])
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(actions["NonRebreatherMask"])
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(actions["BagValveMask"])
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(actions["GiveFluids"])
            continue

        if "circulation" not in examined_vitals:
            take_action(actions["circulation"])
            examined_vitals.add("circulation")
            continue

        if "disability" not in examined_vitals:
            take_action(actions["disability"])
            examined_vitals.add("disability")
            continue

        if "exposure" not in examined_vitals:
            take_action(actions["exposure"])
            examined_vitals.add("exposure")
            continue

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()