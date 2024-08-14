import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = {25, 27, 16, 24}

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def has_unstable_tachyarrhythmia(events):
        arrhythmia_events = [31, 32, 33, 34, 35, 36, 37, 38]
        return any(events[i] > 0 for i in arrhythmia_events)

    def examine_order():
        for action in [3, 4, 5, 6, 7, 8]:
            if action not in actions_taken:
                return action

    def perform_initial_exams():
        return all(action in actions_taken for action in [3, 4, 5])

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        
        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(23)  # Perform CPR
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if has_unstable_tachyarrhythmia(events):
                if 24 not in actions_taken:
                    take_action(24)  # UseMonitorPads
                elif 40 not in actions_taken:
                    take_action(40)  # DefibrillatorCharge
                elif 47 not in actions_taken:
                    take_action(47)  # DefibrillatorSync
                else:
                    take_action(40)  # DefibrillatorCharge (for actual cardioversion)
            else:
                take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if any(events[i] > 0 for i in [4, 5]):
            take_action(31)  # UseYankeurSuctionCatheter
            continue

        if events[6] > 0:
            take_action(36)  # PerformHeadTiltChinLift
            continue

        if not perform_initial_exams() and not any(events[i] > 0 for i in range(1, 4)):
            take_action(examine_order())  # Perform ABCDE examination in order
            continue

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()