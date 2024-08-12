import sys


def main():
    max_steps = 350
    actions_taken = {
        "BreathingDrawer": False,
        "SatsProbe": False,
        "Monitor": False,
        "BPCuff": False,
        "Fluids": False,
        "A_Line": False,
        "HeartRateChecked": False,
        "AirwayExamine": False,
    }

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

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

        # Check and ensure Airway
        if not events[3] and not actions_taken["AirwayExamine"]:
            print(3)  # ExamineAirway
            actions_taken["AirwayExamine"] = True
            continue

        # Check Sats and vital signs
        if not actions_taken["BreathingDrawer"]:
            print(19)  # OpenBreathingDrawer
            actions_taken["BreathingDrawer"] = True
            continue

        if not actions_taken["SatsProbe"]:
            print(25)  # UseSatsProbe
            actions_taken["SatsProbe"] = True
            continue

        if not actions_taken["Monitor"]:
            print(16)  # ViewMonitor
            actions_taken["Monitor"] = True
            continue

        # Cardiac Arrest check
        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            print(17)  # StartChestCompression
            continue

        # Stabilizing measures
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            if not actions_taken["BPCuff"]:
                print(27)  # UseBloodPressureCuff
                actions_taken["BPCuff"] = True
                continue
            elif not actions_taken["Fluids"]:
                print(15)  # GiveFluids
                actions_taken["Fluids"] = True
                continue
            elif not actions_taken["A_Line"]:
                print(26)  # UseAline
                actions_taken["A_Line"] = True
                continue

        if vitals["HeartRate"] and not actions_taken["HeartRateChecked"]:
            actions_taken["HeartRateChecked"] = True
            if vitals["HeartRate"] > 150:
                print(10)  # GiveAdrenaline
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(9)  # GiveAdenosine
                continue
            elif vitals["HeartRate"] < 50:
                print(12)  # GiveAtropine
                continue

        print(48)  # Finish
        return

    print(48)  # Finish at the end of max steps


if __name__ == "__main__":
    main()