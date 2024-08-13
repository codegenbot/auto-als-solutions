import sys

def main():
    max_steps = 350
    used_methods = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )
        vitals = {
            name: value if vital_signs_times[i] > 0 else None
            for i, name in enumerate([
                "HeartRate", "RespRate", "CapillaryGlucose",
                "Temperature", "MAP", "Sats", "Resps"
            ])
        }

        if "ExamineAirway" not in used_methods:
            print(3)
            used_methods.add("ExamineAirway")
            continue

        if not events[3]:  # AirwayClear check
            print(35)
            continue

        if "ExamineBreathing" not in used_methods:
            print(4)
            used_methods.add("ExamineBreathing")
            continue

        if "OpenBreathingDrawer" not in used_methods:
            print(19)
            used_methods.add("OpenBreathingDrawer")
            continue

        if "UseSatsProbe" not in used_methods:
            print(25)
            used_methods.add("UseSatsProbe")
            continue

        if "ViewMonitor" not in used_methods:
            print(16)
            used_methods.add("ViewMonitor")
            continue

        if "UseBloodPressureCuff" not in used_methods:
            print(27)
            used_methods.add("UseBloodPressureCuff")
            continue

        if "ExamineCirculation" not in used_methods:
            print(5)
            used_methods.add("ExamineCirculation")
            continue

        if "TakeBloodPressure" not in used_methods:
            print(38)
            used_methods.add("TakeBloodPressure")
            continue

        # Cardiac Arrest Check
        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            print(17)  # StartChestCompression
            continue

        # Stabilization Checks
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        if vitals["HeartRate"] and vitals["HeartRate"] > 100:
            print(2)  # CheckRhythm
            continue

        if events[29]:  # HeartRhythmSVT check
            print(9)  # GiveAdenosine
            continue

        print(48)  # Finish
        return

    print(48)  # Finish

if __name__ == "__main__":
    main()