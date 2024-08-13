import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

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

        if 25 not in actions_taken:
            actions_taken.add(25)
            print(25)
            continue
        if 27 not in actions_taken:
            actions_taken.add(27)
            print(27)
            continue
        if 16 not in actions_taken:
            actions_taken.add(16)
            print(16)
            continue
        
        if 3 not in actions_taken:
            actions_taken.add(3)
            print(3)
            continue
        if 4 not in actions_taken:
            actions_taken.add(4)
            print(4)
            continue
        if 5 not in actions_taken:
            actions_taken.add(5)
            print(5)
            continue

        # Airway management
        if events[3] == 0:
            print(18)  # OpenAirwayDrawer
            continue
        if events[4] > 0:
            print(31)  # UseYankeurSucionCatheter
            continue

        # Breathing management
        if vitals["Sats"] is None or vitals["RespRate"] is None:
            print(5)  # ExamineBreathing
            continue
        if vitals["Sats"] < 65:
            print(22)  # BagDuringCPR
            continue
        if vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        # Circulation management
        if events[30] > 0 and vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(10)  # GiveAdrenaline
            continue
        if vitals["MAP"] is None:
            print(5)  # ExamineCirculation
            continue
        if vitals["MAP"] < 20:
            print(15)  # GiveFluids
            continue
        if vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        # Disability management
        if events[21] == 0:
            print(6)  # ExamineDisability
            continue

        # Exposure management
        if events[25] == 0:
            print(7)  # ExamineExposure
            continue

        print(48)
        return

if __name__ == "__main__":
    stabilize()