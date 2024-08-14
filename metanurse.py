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
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        # Default vitals as None
        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        # Perform ABCDE assessment
        # Airway
        if any(events[i] > 0 for i in [4, 5, 6]):  # AirwayVomit, AirwayBlood, AirwayTongue
            take_action(31)  # UseYankeurSuctionCatheter
            continue

        # Breathing
        if not vitals["Sats"] or vitals["Sats"] < 88:
            if vitals["Sats"] < 65:
                take_action(22)  # BagDuringCPR
            else:
                take_action(30)  # UseNonRebreatherMask
            continue
        if not vitals["RespRate"] or vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Circulation - MAP and Tachyarrhythmia tests:
        if not vitals["MAP"] or vitals["MAP"] < 60:
            if vitals["MAP"] < 20:
                take_action(23)  # ResumeCPR
            elif has_unstable_tachyarrhythmia(events):
                take_action(24) if 24 not in actions_taken else [
                    take_action(40) if 40 not in actions_taken else [
                        take_action(47) if 47 not in actions_taken else take_action(41)
                    ]
                ]
            else:
                take_action(15)  # GiveFluids
            continue

        # Disability - evaluate AVPU scale
        if any(events[i] > 0 for i in range(21, 24)) or events[2] > 0:  # AVPU_A, AVPU_V, AVPU_U, ResponseNone
            take_action(8)  # ExamineResponse
            continue

        # Exposure evaluation
        if any(events[i] > 0 for i in range(25, 30)):  # Exposure Events
            take_action(7)  # ExamineExposure
            continue

        # If all vitals are stable, finish the scenario
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()