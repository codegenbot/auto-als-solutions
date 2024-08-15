import sys

def stabilize():
    max_steps = 350
    step = 0
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = [24, 25, 27]

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def needs_measurements():
        return not all(action in actions_taken for action in required_measurements)

    while step < max_steps:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
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

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)
            step += 1
            continue

        if needs_measurements():
            take_action(next_measurement_action())
            step += 1
            continue

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)
            elif events[6] > 0:
                take_action(32)
            step += 1
            continue

        if (vitals["Sats"] is not None and vitals["Sats"] < 88) or (vitals["RR"] is not None and vitals["RR"] < 8):
            if vitals["Sats"] is not None and vitals["Sats"] < 88:
                take_action(30)
            if vitals["RR"] is not None and vitals["RR"] < 8:
                take_action(29)
            step += 1
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            step += 1
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            step += 1
            continue

        tachyarrhythmias = ["HeartRhythmSVT", "HeartRhythmVT", "HeartRhythmAF",
                            "HeartRhythmAtrialFlutter", "HeartRhythmTorsades", "HeartRhythmVF"]
        if any(events[i] > 0 for i in [27 + i for i in range(len(tachyarrhythmias))]):
            take_action(24)
            take_action(43)
            step += 1
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            step += 1
            continue
        
        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)
            step += 1
            continue
            
        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)
            step += 1
            continue

        take_action(48)
        break
    
        step += 1

if __name__ == "__main__":
    stabilize()