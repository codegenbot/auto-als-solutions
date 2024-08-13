import sys

def stabilize():
    max_steps = 350
    examine_steps = [16, 25, 27, 38, 3, 4, 5, 7, 8, 6]  # Steps to examine in sequence
    treatments = {
        'low_sats': 30,   # UseNonRebreatherMask for low oxygen saturation
        'low_resp_rate': 29,  # UseBagValveMask for low respiratory rate
        'low_map': 15,    # GiveFluids for low mean arterial pressure
        'tachyarrhythmia': 40,  # DefibrillatorCharge for unstable tachyarrhythmia
        'cardiac_arrest': 17   # StartChestCompression for cardiac arrest
    }
    examine_index = 0
    map_measured, sats_measured = False, False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(
            vital_signs_values, vital_signs_times,
            ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"]
        )}
        
        # Examine steps (Make sure to attach proper tools before examining)
        if not map_measured:
            print(27)  # Attach blood pressure cuff
            map_measured = True
            continue
        if not sats_measured:
            print(25)  # Attach sats probe
            sats_measured = True
            continue
        if examine_index < len(examine_steps):
            print(examine_steps[examine_index])
            examine_index += 1
            continue
        
        # Detect and handle emergencies
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(treatments['cardiac_arrest'])
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(treatments['cardiac_arrest'])
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(treatments['low_sats'])
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(treatments['low_resp_rate'])
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(treatments['low_map'])
            continue
        if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or events[32] > 0):
            print(treatments['tachyarrhythmia'])
            continue
        
        # Check if stabilized
        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
            print(48)  # Finish
            return
        
        print(0)  # DoNothing if no specific action required

if __name__ == "__main__":
    stabilize()