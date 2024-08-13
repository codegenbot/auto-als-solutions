import sys


def main():
    max_steps = 350
    used_methods = set()
    initial_examine = False

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values,
                vital_signs_times,
                [
                    "HeartRate",
                    "RespRate",
                    "CapillaryGlucose",
                    "Temperature",
                    "MAP",
                    "Sats",
                    "Resps",
                ],
            )
        }

        if step == 0 or not initial_examine:
            print(3)  # Initial Airway Examination
            initial_examine = True
            continue

        if not events[3]:  # Ensure airway is clear
            print(35)  # PerformAirwayManoeuvres
            continue

        if "UseSatsProbe" not in used_methods:
            print(25)
            used_methods.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in used_methods:
            print(27)
            used_methods.add("UseBloodPressureCuff")
            continue

        if "ViewMonitor" not in used_methods:
            print(16)
            used_methods.add("ViewMonitor")
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
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

        if vitals["HeartRate"]:
            if vitals["HeartRate"] < 50:
                print(12)  # GiveAtropine
                continue
            elif vitals["HeartRate"] > 150:
                print(9)  # GiveAdenosine
                continue

        for i in range(27, 33):
            if events[i]:
                print(24)  # UseMonitorPads
                continue

        # Breathing examination
        if "ExaminedBreathing" not in used_methods and not any(events[7:15]):
            print(4)  # ExamineBreathing
            used_methods.add("ExaminedBreathing")
            continue

        # Circulation examination
        if "ExaminedCirculation" not in used_methods and not any(events[15:21]):
            print(5)  # ExamineCirculation
            used_methods.add("ExaminedCirculation")
            continue

        # Disability examination
        if "ExaminedDisability" not in used_methods and not any(events[21:27]):
            print(6)  # ExamineDisability
            used_methods.add("ExaminedDisability")
            continue

        # Exposure examination
        if "ExaminedExposure" not in used_methods and not any(events[27:33]):
            print(7)  # ExamineExposure
            used_methods.add("ExaminedExposure")
            continue

        print(48)  # Finish
        return

    print(48)  # Finish


if __name__ == "__main__":
    main()