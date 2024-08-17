import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined = 350, set()

    for step in range(steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        timestamps = observations[33:40]
        measurements = observations[40:]

        vitals = {
            "HR": measurements[0] if timestamps[0] > 0 else None,
            "RR": measurements[1] if timestamps[1] > 0 else None,
            "Glucose": measurements[2] if timestamps[2] > 0 else None,
            "Temp": measurements[3] if timestamps[3] > 0 else None,
            "MAP": measurements[4] if timestamps[4] > 0 else None,
            "Sats": measurements[5] if timestamps[5] > 0 else None,
            "Resps": measurements[6] if timestamps[6] > 0 else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            take_action(22)  # BagDuringCPR
            continue

        if "Monitor" not in examined:
            take_action(16)
            examined.add("Monitor")
            continue

        if "SatsProbe" not in examined:
            take_action(25)
            examined.add("SatsProbe")
            continue

        if "BPCuff" not in examined:
            take_action(27)
            examined.add("BPCuff")
            continue

        if not any(events[3:7]) and "Airway" not in examined:
            take_action(3)
            examined.add("Airway")
            continue

        if any(events[3:7]):
            if events[7] or events[8]:  # BreathingNone or BreathingSnoring
                take_action(35)  # PerformAirwayManoeuvres
                continue
            if not any(events[7:15]) and "Breathing" not in examined:
                take_action(4)
                examined.add("Breathing")
                continue

        if vitals["HR"]:
            if vitals["HR"] > 150:
                take_action(39)  # TurnOnDefibrillator
                continue
            if vitals["HR"] > 100 and vitals["MAP"] < 60:
                take_action(47)  # DefibrillatorSync
                continue
            elif vitals["HR"] > 100:
                take_action(9)  # GiveAdenosine
                continue
            elif vitals["HR"] < 50:
                take_action(12)  # GiveAtropine
                continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)
            continue

        take_action(48)
        break
    else:
        take_action(48)


if __name__ == "__main__":
    stabilize()