import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()

    for step in range(350):
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

        # Immediate checks for critical conditions
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        # Attach necessary monitoring devices once
        necessary_monitors = [27, 25, 24, 26]
        if any(action not in actions_taken for action in necessary_monitors):
            for action in necessary_monitors:
                if action not in actions_taken:
                    actions_taken.add(action)
                    take_action(action)
                    break
            continue

        # AIRWAY checks and interventions
        if events[4] > 0 or events[5] > 0 or events[6] > 0:  # AirwayVomit, AirwayBlood, AirwayTongue
            take_action(32 if events[6] > 0 else 31)  # UseGuedelAirway or UseYankeurSucionCatheter
            continue

        # BREATHING checks and interventions
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing events
            take_action(4)  # ExamineBreathing
            continue

        # CIRCULATION checks and interventions
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["HR"] is not None and vitals["HR"] > 150:  # Tachyarrhythmia
            take_action(28)  # AttachDefibPads (if not already attached)
            take_action(40)  # DefibrillatorCharge
            take_action(43)  # DefibrillatorPace
            continue

        if any(events[i] > 0 for i in range(15, 20)):  # Circulation events
            take_action(5)  # ExamineCirculation
            continue

        # DISABILITY checks
        if any(events[i] > 0 for i in range(20, 26)):  # Disability events
            take_action(6)  # ExamineDisability
            continue

        # EXPOSURE checks
        if any(events[i] > 0 for i in range(26, 33)):  # Exposure events
            take_action(7)  # ExamineExposure
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()