import sys

def main():
    max_steps = 350
    used_methods = set()
    initial_examine = False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:40],
            observations[40:47],
            observations[47:],
        )

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] else None,
            "CapillaryGlucose": vital_signs_values[2] if vital_signs_times[2] else None,
            "Temperature": vital_signs_values[3] if vital_signs_times[3] else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] else None,
            "Resps": vital_signs_values[6] if vital_signs_times[6] else None
        }

        if step == 0 or not initial_examine:
            print(3)  # ExamineAirway
            initial_examine = True
            continue
        
        if "UseMonitor" not in used_methods:
            print(16)  # ViewMonitor
            used_methods.add("UseMonitor")
            continue
        
        if "UseSatsProbe" not in used_methods:
            print(25)  # UseSatsProbe
            used_methods.add("UseSatsProbe")
            continue
        
        if "UseBloodPressureCuff" not in used_methods:
            print(27)  # UseBloodPressureCuff
            used_methods.add("UseBloodPressureCuff")
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue
        
        if vitals["HeartRate"] and (vitals["HeartRate"] > 150 or events[27]):
            print(40)  # DefibrillatorCharge
            continue

        if events[15] and "ExamineCirculation" not in used_methods:
            print(5)  # ExamineCirculation
            used_methods.add("ExamineCirculation")
            continue

        print(48)  # Finish
        return

    print(48)  # Finish

if __name__ == "__main__":
    main()