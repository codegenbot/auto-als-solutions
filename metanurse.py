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

        # High priority checks for critical conditions
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # Start chest compressions
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # Bag during CPR
            continue

        unstable_tachyarrhythmia = any(events[i] > 0 for i in range(29, 33))
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)  # Attach defib pads
                continue
            take_action(40)  # Charge defibrillator
            continue
        
        if step % 5 == 0:
            if 25 not in actions_taken:
                take_action(25)  # UseSatsProbe
                continue
            if 27 not in actions_taken:
                take_action(27)  # UseBloodPressureCuff
                continue
            if 16 not in actions_taken:
                take_action(16)  # ViewMonitor
                continue
            if 3 not in actions_taken:
                take_action(3)  # ExamineAirway
                continue
        
        # Treat airway obstructions immediately
        if any(events[i] > 0 for i in range(4, 7)):
            take_action(31)  # Use Yankeur Suction Catheter
            continue
        if events[6] > 0:
            take_action(36)  # Perform Head Tilt Chin Lift
            continue

        # Respond to moderate issues
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()