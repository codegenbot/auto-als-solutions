import sys

def main():
    max_steps = 350
    step_count = 0
    actions_taken = set()

    while step_count < max_steps:
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )

        vitals = {k: v for v, k in zip(vital_signs_values, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ]) if vital_signs_times[list(vitals.keys()).index(k)] > 0}

        if 'AirwayClear' not in actions_taken and events[3] == 0:
            print(3)
            actions_taken.add('AirwayClear')
            step_count += 1
            continue

        if 'MeasuredRespRate' not in actions_taken:
            print(4)
            actions_taken.add('MeasuredRespRate')
            step_count += 1
            continue
        
        if 'MeasuredMAP' not in actions_taken:
            print(5)
            actions_taken.add('MeasuredMAP')
            step_count += 1
            continue

        if 'MeasuredSats' not in actions_taken:
            print(25)
            actions_taken.add('MeasuredSats')
            step_count += 1
            continue

        if vitals.get("Sats", 100) < 65 or vitals.get("MAP", 100) < 20:
            print(17)
            step_count += 1
            continue

        if vitals.get("Sats", 100) < 88:
            print(30)
            step_count += 1
            continue

        if vitals.get("RespRate", 100) < 8:
            print(29)
            step_count += 1
            continue

        if vitals.get("MAP", 100) < 60:
            print(15)
            step_count += 1
            continue

        if 'ExamineDisability' not in actions_taken:
            print(6)
            actions_taken.add('ExamineDisability')
            step_count += 1
            continue

        if 'ExamineExposure' not in actions_taken:
            print(7)
            actions_taken.add('ExamineExposure')
            step_count += 1
            continue

        print(48)
        return

    print(48)

if __name__ == "__main__":
    main()