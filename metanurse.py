import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps_taken = set()
    max_steps = 350

    def measure_vitals():
        vitals_checks = [16, 27, 25, 4]
        for check in vitals_checks:
            take_action(check)
    
    for step in range(max_steps):
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

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if "vitals_checked" not in steps_taken:
            measure_vitals()
            steps_taken.add("vitals_checked")
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

        if events[3] or (events[6] and not events[3]):
            take_action(3)  # ExamineAirway
            continue

        if vitals["HR"]:
            if vitals["HR"] < 50:
                take_action(12)  # GiveAtropine
                continue
            elif vitals["HR"] > 150 or events[29]:
                take_action(28)  # AttachDefibPads
                take_action(40)  # DefibrillatorCharge
                take_action(41)  # DefibrillatorCurrentUp
                take_action(43)  # DefibrillatorPace
                continue

        take_action(48)  # Finish
        break
    else:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()