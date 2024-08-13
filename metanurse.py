import sys

def stabilize():
    max_steps = 350

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if vital_signs_times[i] != 0 else None for i, (name, value) in enumerate(zip([
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ], vital_signs_values))}

        if events[3] == 0:
            print(3)  # ExamineAirway
            continue

        if not vitals["Sats"]:
            print(25)  # UseSatsProbe
            continue

        if not vitals["RespRate"] and events[7] == 0:
            print(4)  # ExamineBreathing
            continue

        if not vitals["MAP"]:
            print(38)  # TakeBloodPressure
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

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
            print(39)  # TurnOnDefibrillator
            continue

        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)  # Finish
            return

        print(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()