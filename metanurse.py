import sys

def stabilize():
    max_steps = 350
    examine_steps = [False] * 6
    use_sats_probe = use_blood_pressure_cuff = view_monitor = False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        if not examine_steps[0]:
            examine_steps[0] = True
            print(3)
            continue
        if not examine_steps[1]:
            examine_steps[1] = True
            print(4)
            continue
        if not examine_steps[2]:
            examine_steps[2] = True
            print(5)
            continue
        if not examine_steps[3]:
            examine_steps[3] = True
            print(6)
            continue
        if not examine_steps[4]:
            examine_steps[4] = True
            print(7)
            continue
        if not examine_steps[5]:
            examine_steps[5] = True
            print(8)
            continue

        if not use_sats_probe:
            use_sats_probe = True
            print(25)
            continue
        if not use_blood_pressure_cuff:
            use_blood_pressure_cuff = True
            print(27)
            continue
        if not view_monitor:
            view_monitor = True
            print(16)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)
            continue

        if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
            print(39)
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)
            return
        
        print(0)

if __name__ == "__main__":
    stabilize()