import sys

def stabilize():
    max_steps = 350

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        # Examine the Airway initially.
        if step == 0:
            print(3)  # ExamineAirway
            continue
        
        # Ensure we have readings for necessary vitals.
        if vitals["Sats"] is None:
            print(25)  # UseSatsProbe
            continue
        if vitals["RespRate"] is None:
            print(4)  # ExamineBreathing
            continue
        if vitals["MAP"] is None:
            print(5)  # ExamineCirculation
            continue
        
        # Stabilize based on vital signs.
        if vitals["Sats"] < 65 or vitals["MAP"] < 20:
            print(17)  # StartChestCompression
            continue
        if vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue
        if vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue
        
        if all(vitals.get(vital) is not None for vital in ["Sats", "RespRate", "MAP"]) and all(
                value >= threshold for value, threshold in zip(
                    [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                    [88, 8, 60])):
            print(48)  # Finish
            return

        print(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()