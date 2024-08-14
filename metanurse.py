import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {
            name: value if vital_signs_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                     "MAP", "Sats", "Resps"], vital_signs_values
                )
            )
        }

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)
            continue
        
        if 3 not in actions_taken:  # Airway Check
            take_action(3)
            continue
        
        if events[3] > 0:  # AirwayClear
            if 25 not in actions_taken:  # UseSatsProbe
                take_action(25)
                continue
            if vitals["Sats"] is not None and vitals["Sats"] < 88:
                take_action(30)  # UseNonRebreatherMask
                continue
            if 27 not in actions_taken:  # UseBloodPressureCuff
                take_action(27)
                continue
            if 16 not in actions_taken:  # ViewMonitor
                take_action(16)
                continue
            if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
                take_action(29)  # UseBagValveMask
                continue
            if vitals["MAP"] is not None and vitals["MAP"] < 60:
                take_action(15)  # GiveFluids
                continue
            
            if 6 not in actions_taken:  # Disability Check
                take_action(6)
                continue
            
            if 7 not in actions_taken:  # Exposure Check
                take_action(7)
                continue

            if all(
                vitals[vital] is not None and vitals[vital] >= threshold
                for vital, threshold in [
                    ("Sats", 88), ("RespRate", 8), ("MAP", 60)
                ]
            ):
                take_action(48)
                return

        take_action(0)

if __name__ == "__main__":
    stabilize()