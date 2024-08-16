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
            take_action(4)  # ExamineBreathing
            examined.add("RespRate")
        elif "HeartRhythm" not in examined:
            take_action(2)  # CheckRhythm
            examined.add("HeartRhythm")

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

        # Immediate cardiac arrest check
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        # Assess Airway
        if events[3] > 0:
            examined.add("airway")
        if "airway" not in examined:
            take_action(3)  # ExamineAirway
            continue

        # Check vital signs
        measure_vitals()

        # Circulation intervention
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Breathing intervention
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        if vitals["RR"] and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Check unstable rhythm and handle arrhythmias
        if events[29] > 0 or events[30] > 0 or (vitals["HR"] and (vitals["HR"] < 50 or vitals["HR"] > 150)):
            take_action(24)  # UseMonitorPads
            take_action(40)  # DefibrillatorCharge
            take_action(41)  # DefibrillatorCurrentUp
            continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()