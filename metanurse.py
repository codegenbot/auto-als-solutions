import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined = set()

    def measure_vitals():
        if "Monitor" not in examined:
            take_action(16)  # ViewMonitor
            examined.add("Monitor")
        elif "BP" not in examined:
            take_action(27)  # UseBloodPressureCuff
            examined.add("BP")
        elif "SatsProbe" not in examined:
            take_action(25)  # UseSatsProbe
            examined.add("SatsProbe")
        elif "RespRate" not in examined:
            take_action(4)   # ExamineBreathing
            examined.add("RespRate")

    def intervene(vitals):
        if vitals["MAP"] and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
        elif vitals["Sats"] and vitals["Sats"] < 65:
            take_action(17)  # StartChestCompression
        elif vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
        elif vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
        elif vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
        if vitals["HR"] and (vitals["HR"] < 50 or vitals["HR"] > 150):
            take_action(28)  # AttachDefibPads
            take_action(40)  # DefibrillatorCharge
            take_action(41)  # DefibrillatorCurrentUp
            take_action(43)  # DefibrillatorPace

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
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

        measure_vitals()
        intervene(vitals)

        if events[3] > 0:  # AirwayClear
            examined.add("airway")
        if "airway" not in examined:
            take_action(3)  # ExamineAirway
            examined.add("airway")
            continue

        if all(v is not None for v in [vitals["MAP"], vitals["Sats"], vitals["RR"]]) and \
                vitals["MAP"] >= 60 and vitals["Sats"] >= 88 and vitals["RR"] >= 8:
            take_action(48)  # Finish
            break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()