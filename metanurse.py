import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    step = 0

    while step < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]
        
        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Cardiac arrest condition
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
                vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            step += 1
            continue

        # A - Airway
        if any(events[i] > 0 for i in range(3, 7)):  # Airway events
            take_action(3)  # ExamineAirway
            if events[5] > 0:
                take_action(31)  # UseYankeurSucionCatheter
            if events[6] > 0:
                take_action(32)  # UseGuedelAirway
            step += 1
            continue

        # B - Breathing
        if any(events[i] > 0 for i in range(7, 15)):  # Breathing events
            take_action(4)  # ExamineBreathing
            step += 1
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            step += 1
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            step += 1
            continue

        # C - Circulation
        if vitals["MAP"] is None and 27 not in actions_taken:
            actions_taken.add(27)
            take_action(27)  # UseBloodPressureCuff
            step += 1
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            step += 1
            continue

        if vitals["HR"] is not None and vitals["HR"] > 150:
            take_action(9)  # GiveAdenosine
            step += 1
            continue

        # Essential monitoring actions
        if 24 not in actions_taken:
            actions_taken.add(24)
            take_action(24)  # UseMonitorPads
            step += 1
            continue

        if 25 not in actions_taken:
            actions_taken.add(25)
            take_action(25)  # UseSatsProbe
            step += 1
            continue

        if 26 not in actions_taken:
            actions_taken.add(26)
            take_action(26)  # UseAline
            step += 1
            continue

        take_action(48)  # Finish
        break

        step += 1

if __name__ == "__main__":
    stabilize()