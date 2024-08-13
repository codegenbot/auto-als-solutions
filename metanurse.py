import sys

def stabilize():
    max_steps = 350
    examine_steps = [3, 4, 5, 27, 16, 25, 38]
    treatments = {
        'low_sats': 30,
        'low_resp_rate': 29,
        'low_map': 15,
        'tachyarrhythmia': 40,
        'cardiac_arrest': 17,
    }
    examine_index = 0
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(
            vital_signs_values, vital_signs_times,
            ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"]
        )}

        if examine_index < len(examine_steps):
            print(examine_steps[examine_index])
            examine_index += 1
            continue

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

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60])):
            print(48)
            return

        print(0)

if __name__ == "__main__":
    stabilize()