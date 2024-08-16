import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]
        
        vital_signs = {
            "HR": values[0] if times[0] != 0 else None,
            "RR": values[1] if times[1] != 0 else None,
            "Glucose": values[2] if times[2] != 0 else None,
            "Temp": values[3] if times[3] != 0 else None,
            "MAP": values[4] if times[4] != 0 else None,
            "Sats": values[5] if times[5] != 0 else None,
            "Resps": values[6] if times[6] != 0 else None,
        }

        # Immediate life-threatening conditions
        if (vital_signs["Sats"] is not None and vital_signs["Sats"] < 65) or (vital_signs["MAP"] is not None and vital_signs["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        # Airway
        if not any(events[3:7]):  # Airway events
            take_action(3)  # ExamineAirway
            continue

        if events[2]:  # Check response
            take_action(8)  # ExamineResponse
            continue

        # Breathing
        if vital_signs["Sats"] is None:
            take_action(25)  # UseSatsProbe
            continue
        
        if vital_signs["RR"] is None:
            take_action(4)  # ExamineBreathing
            continue

        if vital_signs["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vital_signs["RR"] and vital_signs["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Circulation
        if vital_signs["MAP"] is None:
            take_action(27)  # UseBloodPressureCuff
            continue

        if vital_signs["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Ensure all vitals are checked before finishing
        if None in vital_signs.values():
            take_action(24)  # UseMonitorPads
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()