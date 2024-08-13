import sys

def stabilize():
    max_steps = 350
    steps_taken = 0
    
    # Flags for each examination step
    examined = {'Airway': False, 'Breathing': False, 'Circulation': False, 'Disability': False, 'Exposure': False}
    
    # Initial steps to probe and measure vitals
    def initial_probing():
        nonlocal steps_taken
        steps_list = [25, 27, 16, 3]
        for step in steps_list:
            print(step)
            steps_taken += 1
            if steps_taken >= max_steps:
                print(48)  # Finish
                return True
        return False
    
    if initial_probing():
        return

    while steps_taken < max_steps:
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values,
                vital_signs_times,
                [
                    'HeartRate', 'RespRate', 'CapillaryGlucose',
                    'Temperature', 'MAP', 'Sats', 'Resps'
                ]
            )
        }

        # Perform ABCDE examinations
        if not examined['Airway']:
            print(3)  # ExamineAirway
            examined['Airway'] = True
            steps_taken += 1
            continue
        
        if not examined['Breathing']:
            print(4)  # ExamineBreathing
            examined['Breathing'] = True
            steps_taken += 1
            continue
        
        if not examined['Circulation']:
            print(5)  # ExamineCirculation
            examined['Circulation'] = True
            steps_taken += 1
            continue
        
        if not examined['Disability']:
            print(6)  # ExamineDisability
            examined['Disability'] = True
            steps_taken += 1
            continue
        
        if not examined['Exposure']:
            print(7)  # ExamineExposure
            examined['Exposure'] = True
            steps_taken += 1
            continue

        # Treatment steps based on vitals
        if vitals['Sats'] is not None and vitals['Sats'] < 65:
            print(17)  # StartChestCompression
            steps_taken += 1
            continue

        if vitals['MAP'] is not None and vitals['MAP'] < 20:
            print(17)  # StartChestCompression
            steps_taken += 1
            continue

        if vitals['HeartRate'] is not None and (vitals['HeartRate'] > 150 or vitals['HeartRate'] < 50):
            print(41)  # DefibrillatorCurrentUp
            steps_taken += 1
            continue

        if vitals['MAP'] is not None and vitals['MAP'] < 60:
            print(15)  # GiveFluids
            steps_taken += 1
            continue

        if vitals['Sats'] is not None and vitals['Sats'] < 88:
            print(30)  # UseNonRebreatherMask
            steps_taken += 1
            continue

        if vitals['RespRate'] is not None and vitals['RespRate'] < 8:
            print(29)  # UseBagValveMask
            steps_taken += 1
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals['Sats'], vitals['RespRate'], vitals['MAP']], [88, 8, 60]
            )
        ):
            print(48)  # Finish
            return

        print(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()