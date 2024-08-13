import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        actions_taken.add(action)
        print(action)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )
        vitals_names = [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ]
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(vital_signs_values, vital_signs_times, vitals_names)
        }

        if 25 not in actions_taken:  # UseSatsProbe
            take_action(25)
            continue
        if 27 not in actions_taken:  # UseBloodPressureCuff
            take_action(27)
            continue
        if 16 not in actions_taken:  # ViewMonitor
            take_action(16)
            continue
        if 3 not in actions_taken:   # ExamineAirway
            take_action(3)
            continue
        if 4 not in actions_taken:   # ExamineBreathing
            take_action(4)
            continue
        if 5 not in actions_taken:   # ExamineCirculation
            take_action(5)
            continue

        # Stabilize based on vital sign checks
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(29)  # UseBagValveMask
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(15)  # GiveFluids
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if events[29] > 0 or events[30] > 0:
                take_action(10)  # GiveAdrenaline
            else:
                take_action(15)  # GiveFluids
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if events[29] > 0 or events[30] > 0:
            take_action(10)  # GiveAdrenaline
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)
            return

    print(48)  # Finish the scenario

if __name__ == "__main__":
    stabilize()