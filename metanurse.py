import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def measure_all_vitals(examined):
        if "SatsProbe" not in examined:
            take_action(25)
            examined.add("SatsProbe")
        elif "RespRate" not in examined:
            take_action(4)
            examined.add("RespRate")
        elif "BP" not in examined:
            take_action(27)
            examined.add("BP")
        elif "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
        elif "HR" not in examined:
            take_action(24)
            examined.add("HR")
        return examined

    examined = set()
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

        critical = False
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            critical = True

        if critical:
            continue

        if "airway" not in examined:
            take_action(3)
            examined.add("airway")
            continue

        if events[3] > 0:
            examined.add("airway")

        examined = measure_all_vitals(examined)

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        heart_rhythms = {
            28: "SVT",
            29: "AF",
            30: "AtrialFlutter",
            31: "VT",
            32: "MobitzI",
            33: "MobitzII",
            34: "CompleteHeartBlock",
            35: "Torsades",
            36: "Bigeminy",
            37: "VF",
        }
        for idx, rhythm in heart_rhythms.items():
            if events[idx] > 0:
                if rhythm == "SVT":
                    take_action(9)
                elif rhythm in ["VT", "VF"]:
                    take_action(24)
                    take_action(40)
                    take_action(43)
                continue

        take_action(48)
        break
    else:
        take_action(48)


if __name__ == "__main__":
    stabilize()