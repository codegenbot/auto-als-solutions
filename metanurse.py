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

        if step == 0:
            print(3)  # ExamineAirway
            continue

        if "initial_examinations_done" not in used_methods:
            if "ExamineBreathing" not in used_methods:
                print(4)  # ExamineBreathing
                used_methods.add("ExamineBreathing")
                continue
            if "ExamineCirculation" not in used_methods:
                print(5)  # ExamineCirculation
                used_methods.add("ExamineCirculation")
                continue
            if "ExamineDisability" not in used_methods:
                print(6)  # ExamineDisability
                used_methods.add("ExamineDisability")
                continue
            if "ExamineExposure" not in used_methods:
                print(7)  # ExamineExposure
                used_methods.add("ExamineExposure")
                continue
            used_methods.add("initial_examinations_done")

        if not events[3]:  # AirwayClear
            print(35)  # PerformAirwayManoeuvres
            continue

        if "UseSatsProbe" not in used_methods:
            print(25)  # UseSatsProbe
            used_methods.add("UseSatsProbe")
            continue

        if "UseBloodPressureCuff" not in used_methods:
            print(27)  # UseBloodPressureCuff
            used_methods.add("UseBloodPressureCuff")
            continue

        if "ViewMonitor" not in used_methods:
            print(16)  # ViewMonitor
            used_methods.add("ViewMonitor")
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            print(17)  # StartChestCompression
            continue

        if (
            (vitals["HeartRate"] and vitals["HeartRate"] > 150)
            or (vitals["HeartRate"] and vitals["HeartRate"] < 50)
            or events[27]
        ):  # Unstable rhythm
            if "TurnOnDefibrillator" not in used_methods:
                print(39)  # TurnOnDefibrillator
                used_methods.add("TurnOnDefibrillator")
                continue
            if "DefibrillatorCharge" not in used_methods:
                print(40)  # DefibrillatorCharge
                used_methods.add("DefibrillatorCharge")
                continue
            if "DefibrillatorSync" not in used_methods:
                print(47)  # DefibrillatorSync
                used_methods.add("DefibrillatorSync")
                continue
            print(43)  # DefibrillatorPace
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

        print(48)  # Finish
        return

    print(48)


if __name__ == "__main__":
    main()