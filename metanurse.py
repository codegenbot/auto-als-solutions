import sys

def main():
    max_steps = 350
    opened_drawers = {19: False, 20: False}
    used_pulse_oximeter = viewed_monitor = examined_breathing = False
    used_circulation_methods = {25: False, 26: False, 27: False, 10: False, 9: False, 15: False}

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vital_sign_names = ["HeartRate", "RespRate", "CapillaryGlucose", 
                            "Temperature", "MAP", "Sats", "Resps"]
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(vital_signs_values, vital_signs_times, vital_sign_names)
        }

        if not events[3]:
            print(3)
            continue

        if not opened_drawers[19]:
            print(19)
            opened_drawers[19] = True
            continue

        if not used_pulse_oximeter:
            print(25)
            used_pulse_oximeter = True
            continue

        if not viewed_monitor:
            print(16)
            viewed_monitor = True
            continue

        if not examined_breathing:
            print(4)
            examined_breathing = True
            continue

        if vitals["Sats"] and vitals["Sats"] < 65 or vitals["MAP"] and vitals["MAP"] < 20:
            print(17)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            if not used_circulation_methods[27]:
                print(27)
                used_circulation_methods[27] = True
            elif not used_circulation_methods[26]:
                print(26)
                used_circulation_methods[26] = True
            else:
                print(15)
            continue

        if vitals["HeartRate"]:
            if vitals["HeartRate"] < 50:
                print(12)
                continue
            elif vitals["HeartRate"] > 150:
                print(10)
                continue
            elif 100 < vitals["HeartRate"] < 150:
                print(9)
                continue

        print(48)
        return

    print(48)

if __name__ == "__main__":
    main()