import sys
import math

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    observed = set()

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
            "Resps": values[6] if times[6] > 0 else None
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if not vitals["Sats"]:
            if "SatsProbe" not in observed:
                take_action(25)  # UseSatsProbe
                observed.add("SatsProbe")
                continue

        if not vitals["MAP"]:
            if "BP" not in observed:
                take_action(27)  # UseBloodPressureCuff
                observed.add("BP")
                continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if not vitals["RR"]:
            take_action(4)  # ExamineBreathing
            continue

        if not vitals["HR"]:
            take_action(16)  # ViewMonitor
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()