import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values, vital_signs_times,
                ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                 "MAP", "Sats", "Resps"]
            )
        }

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(22)  # BagDuringCPR
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(15)  # GiveFluids
            continue

        if "A" not in actions_taken:
            actions_taken.add("A")
            print(3)  # ExamineAirway
            continue
        if "B" not in actions_taken:
            actions_taken.add("B")
            print(4)  # ExamineBreathing
            continue
        if "C" not in actions_taken:
            actions_taken.add("C")
            print(5)  # ExamineCirculation
            continue
        if "D" not in actions_taken:
            actions_taken.add("D")
            print(6)  # ExamineDisability
            continue
        if "E" not in actions_taken:
            actions_taken.add("E")
            print(7)  # ExamineExposure
            continue

        if vitals["Sats"] is None:
            print(25)  # UseSatsProbe
            continue
        if vitals["MAP"] is None:
            print(27)  # UseBloodPressureCuff
            continue

        if vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue
        if vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if (events[29] > 0 or events[30] > 0 or
            events[31] > 0 or events[32] > 0 or
            events[33] > 0 or events[34] > 0 or
            events[35] > 0 or events[36] > 0 or
            events[37] > 0 or events[38] > 0):
            print(10)  # GiveAmiodarone
            continue

        if vitals["Sats"] >= 88 and vitals["RespRate"] >= 8 and vitals["MAP"] >= 60:
            print(48)  # Finish
            break

        print(48)  # Finish to avoid infinite loop

if __name__ == "__main__":
    stabilize()