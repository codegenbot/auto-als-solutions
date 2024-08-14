import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values,
                vital_signs_times,
                [
                    "HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                    "MAP", "Sats", "Resps"
                ]
            )
        }

        def take_action(action):
            actions_taken.add(action)
            print(action)
        
        # Step 1: Airway
        if "AirwayClear" not in actions_taken:
            take_action(3)  # ExamineAirway
            continue

        # Step 2: Breathing
        if 25 not in actions_taken:
            take_action(25)  # UseSatsProbe
            continue
        if vitals["RespRate"] is None:
            take_action(26)  # UseAline
            continue
        if "Breathing" not in actions_taken:
            take_action(4)  # ExamineBreathing
            continue
        
        # Step 3: Circulation
        if 27 not in actions_taken:
            take_action(27)  # UseBloodPressureCuff
            continue
        if vitals["MAP"] is None:
            take_action(16)  # ViewMonitor
            continue

        # Assess and stabilize patient
        if vitals["MAP"] and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
            continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            take_action(22)  # BagDuringCPR
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60]
            )
        ):
            take_action(48)  # Finish
            return

        take_action(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()