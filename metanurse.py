import sys

def main():
    max_steps = 350
    use_sats_probe = True
    use_bp_cuff = True
    view_monitor = True
    initial_checklist = [3, 4, 5]  # ExamineAirway, ExamineBreathing, ExamineCirculation

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        if step < len(initial_checklist):
            print(initial_checklist[step])
            continue

        if use_sats_probe:
            print(25)  # UseSatsProbe
            use_sats_probe = False
            continue

        if use_bp_cuff:
            print(27)  # UseBloodPressureCuff
            use_bp_cuff = False
            continue

        if view_monitor:
            print(16)  # ViewMonitor
            view_monitor = False
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65 or vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
                print(43)  # DefibrillatorPace
                continue
            print(15)  # GiveFluids
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)  # Finish
            return

        print(48)  # Finish
        return

if __name__ == "__main__":
    main()