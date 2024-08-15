import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    essential_measurements = [16, 24, 25, 27, 26]
    observed_measurements = set()
    stabilized = False

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] else None,
        }

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if not observed_measurements.issuperset(essential_measurements):
            for action in essential_measurements:
                if action not in observed_measurements:
                    observed_measurements.add(action)
                    take_action(action)
                    break
            continue

        if any(events[i] > 0 for i in range(3, 7)):  # Airway events
            take_action(3)  # ExamineAirway
            if events[5] > 0:
                take_action(31)  # UseYankeurSucionCatheter
            if events[6] > 0:
                take_action(32)  # UseGuedelAirway
            continue

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing events
            take_action(4)  # ExamineBreathing
            if vitals["Sats"] and vitals["Sats"] < 88:
                take_action(30)  # UseNonRebreatherMask
            if vitals["RR"] and vitals["RR"] < 8:
                take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if any(events[i] > 0 for i in range(15, 20)):  # Circulation events
            take_action(5)  # ExamineCirculation
            if vitals["HR"] and vitals["HR"] > 150:
                take_action(40)  # DefibrillatorCharge
                take_action(43)  # DefibrillatorPace
                continue
            continue

        if any(events[i] > 0 for i in range(20, 26)):  # Disability events
            take_action(6)  # ExamineDisability
            continue

        if any(events[i] > 0 for i in range(26, 33)):  # Exposure events
            take_action(7)  # ExamineExposure
            continue

        if all(
            val is not None and val >= target
            for val, target in [
                (vitals["Sats"], 88),
                (vitals["RR"], 8),
                (vitals["MAP"], 60)
            ]
        ):
            take_action(48)  # Finish
            stabilized = True
            break
        
        take_action(0)  # DoNothing

    if not stabilized:
        take_action(48)  # Ensure to finish after loop

if __name__ == "__main__":
    stabilize()