import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values, vital_signs_times,
                ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                 "MAP", "Sats", "Resps"]
            )
        }

        # Interventions for critical conditions
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression for critically low oxygen saturation
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression for critically low MAP
            continue

        # Stabilize based on less critical but urgent conditions
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        # Initial examinations to retrieve required vitals
        initial_exams = [25, 27, 16, 3, 4, 5, 6, 2]
        for action in initial_exams:
            if action not in actions_taken:
                actions_taken.add(action)
                print(action)
                break

        # Check specific events to handle airway obstructions
        airway_events = [3, 1, 2]  # ExamineAirway, CheckSignsOfLife, CheckRhythm
        for event in airway_events:
            if events[event] > 0.5 and event not in actions_taken:  # Adjust event threshold as needed
                actions_taken.add(event)
                print(event)
                break

        # End criteria - if vital signs are stable, indicate completion.
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

if __name__ == "__main__":
    stabilize()