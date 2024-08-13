import sys

def stabilize():
    max_steps = 350
    action_sequence = [25, 27, 16, 3, 4, 5, 6, 7, 2]
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
        
        if step < len(action_sequence):
            if action_sequence[step] not in actions_taken:
                actions_taken.add(action_sequence[step])
                print(action_sequence[step])
                continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            print(22)  # Bag During CPR
            continue
        if vitals["MAP"] and vitals["MAP"] < 20:
            print(15)  # GiveFluids
            continue
        if vitals["MAP"] and vitals["MAP"] < 60:
            if events[29] > 0 or events[30] > 0:  # HeartRhythmSVT or HeartRhythmAF
                print(10)  # Give Amiodarone
            else:
                print(15)  # Give Fluids
            continue
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # Use Non-Rebreather Mask
            continue
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # Use Bag Valve Mask
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return
        
        print(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()