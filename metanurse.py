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

        # Step-by-step ABCDE assessment

        # Check airway and breathing first
        if 3 not in actions_taken:
            take_action(3)
            continue

        if events[3] == 0:
            take_action(3)
            continue

        if 5 not in actions_taken:
            take_action(5)
            continue

        if 16 not in actions_taken:
            take_action(16)
            continue

        if 25 not in actions_taken:
            take_action(25)
            continue

        if 27 not in actions_taken:
            take_action(27)
            continue
        
        # If vital signs are available and some are critical, react accordingly
        if vitals["Sats"] and vitals["Sats"] < 65:
            take_action(22)  # Bag during CPR (critical sats)
            continue

        if vitals["MAP"] and vitals["MAP"] < 20:
            take_action(17)  # Start chest compression (critical MAP)
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give fluids (to raise MAP)
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask (to improve sats)
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            take_action(29)  # Use bag valve mask (to assist breathing)
            continue

        if vitals["HeartRate"] and vitals["HeartRate"] >= 150:
            take_action(11)  # Give amiodarone (to manage tachyarrhythmia)
            continue

        # If all vital signs are stable, end the simulation
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60]
            )
        ):
            take_action(48)
            return

        take_action(48)
        return

if __name__ == "__main__":
    stabilize()