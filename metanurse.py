import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    initial_measurements = [24, 25, 27]

    def next_initial_measurement_action():
        for action in initial_measurements:
            if action not in actions_taken:
                return action

    def needs_initial_measurements():
        return not all(action in actions_taken for action in initial_measurements)
    
    examine_events = {
        3: [4, 5, 6],
        4: [7, 8, 9, 10, 11, 12, 13, 14],
        5: [15, 16, 17, 18],
        6: [19, 20, 21, 22, 23],
        7: [24, 25, 26]
    }
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )
        
        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }
        
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # Chest compressions for cardiac arrest
            continue

        if needs_initial_measurements():
            take_action(next_initial_measurement_action())
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if events[3] > 0:
            take_action(3)  # ExamineAirway
            if events[4] > 0 or events[5] > 0 or events[6] > 0:
                take_action(31)  # UseYankeurSucionCatheter
            continue
        
        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # ExamineBreathing
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue
        
        tachyarrhythmias = [
            "HeartRhythmSVT", "HeartRhythmVT", "HeartRhythmAF",
            "HeartRhythmAtrialFlutter", "HeartRhythmTorsades", "HeartRhythmVF"
        ]
        if any(events[i] > 0 for i in [27, 28, 29, 30, 31, 32, 33]):
            take_action(24)  # UseMonitorPads
            take_action(47)  # DefibrillatorSync
            take_action(43)  # DefibrillatorPace
            continue

        for action, event_indices in examine_events.items():
            if any(events[i] > 0 for i in event_indices):
                take_action(action)
                break
        else:
            take_action(48)  # Finish
            break

if __name__ == "__main__":
    stabilize()