import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    
    def take_action(action):
        if action not in actions_taken:
            print(action)
            actions_taken.add(action)
            sys.stdout.flush()
    
    required_measurements = {24, 25, 27}

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        if any(events[i] > 0 for i in [4, 5, 6]):
            take_action(3)             # ExamineAirway
            if events[5] > 0:
                take_action(31)        # UseYankeurSucionCatheter
            elif events[6] > 0:
                take_action(36)        # PerformHeadTiltChinLift
            continue
        
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)            # StartChestCompression
            continue

        if any(events[i] > 0 for i in range(1, 4)):
            take_action(1)             # CheckSignsOfLife
            take_action(2)             # CheckRhythm
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)             # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)             # UseBagValveMask
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(4)             # ExamineBreathing
            if events[7] > 0:
                take_action(29)        # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)            # GiveFluids
            continue

        take_action(48)                # Finish

if __name__ == "__main__":
    stabilize()