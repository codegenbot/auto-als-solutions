import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()
    
    examined = set()
    vitals_measured = set()

    def measure_vitals():
        if "Monitor" not in vitals_measured:
            take_action(16)  # ViewMonitor
            vitals_measured.add("Monitor")
        elif "BP" not in vitals_measured:
            take_action(27)  # UseBloodPressureCuff
            vitals_measured.add("BP")
        elif "SatsProbe" not in vitals_measured:
            take_action(25)  # UseSatsProbe
            vitals_measured.add("SatsProbe")
        elif "RR" not in vitals_measured:
            take_action(4)  # ExamineBreathing
            vitals_measured.add("RR")

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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if "SignsOfLifeChecked" not in examined:
            take_action(1)  # CheckSignsOfLife
            examined.add("SignsOfLifeChecked")
            continue

        if events[3] > 0:
            examined.add("airway")
        if "airway" not in examined:
            take_action(3)  # ExamineAirway
            examined.add("airway")
            continue

        measure_vitals()

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if events[29] > 0 or events[30] > 0 or (vitals["HR"] is not None and (vitals["HR"] < 50 or vitals["HR"] > 150)):
            take_action(28)  # AttachDefibPads
            continue

        if "all_vitals_checked" not in examined:
            examined.add("all_vitals_checked")
            continue
        
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()