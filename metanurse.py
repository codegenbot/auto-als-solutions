import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = {"Monitor": False, "BP": False, "SatsProbe": False, "RespRate": False, "airway": False}
    
    def check_all_vitals():
        if not examined["Monitor"]:
            take_action(16)
            examined["Monitor"] = True
            return True
        elif not examined["BP"]:
            take_action(27)
            examined["BP"] = True
            return True
        elif not examined["SatsProbe"]:
            take_action(25)
            examined["SatsProbe"] = True
            return True
        elif not examined["RespRate"]:
            take_action(4)
            examined["RespRate"] = True
            return True
        return False
        
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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue

        if not examined["airway"]:
            take_action(3)
            if events[3] > 0:
                examined["airway"] = True
            continue

        if check_all_vitals():
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if events[28] or events[29] or events[30] or events[31] or events[32]:
            take_action(40)
            take_action(41)
            take_action(43)
            continue

        take_action(48)
        break
    else:
        take_action(48)

if __name__ == "__main__":
    stabilize()