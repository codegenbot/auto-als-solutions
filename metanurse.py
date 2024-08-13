import sys

def main():
    max_steps = 350
    step_actions = [
        3,  # ExamineAirway
        4,  # ExamineBreathing
        5,  # ExamineCirculation
        25, # UseSatsProbe
        27, # UseBloodPressureCuff
        16, # ViewMonitor
    ]

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        if step < len(step_actions):
            print(step_actions[step])
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)  # Finish
            return

        print(0)  # DoNothing

if __name__ == "__main__":
    main()