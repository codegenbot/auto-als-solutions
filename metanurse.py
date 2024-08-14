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

    def need_examination():
        return 25 not in actions_taken or 27 not in actions_taken or 16 not in actions_taken or 3 not in actions_taken

    def examine():
        if 25 not in actions_taken:
            take_action(25)  # UseSatsProbe
        elif 27 not in actions_taken:
            take_action(27)  # UseBloodPressureCuff
        elif 16 not in actions_taken:
            take_action(16)  # ViewMonitor
        elif 3 not in actions_taken:
            take_action(3)   # ExamineAirway

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

        if need_examination():
            examine()
            continue

        if events[4] > 0 or events[5] > 0:
            take_action(31)   # Use Yankeur Suction Catheter for airway vomit/blood
            continue

        if events[6] > 0:
            take_action(36)   # Perform Head Tilt Chin Lift for tongue obstruction
            continue

        unstable_tachyarrhythmia_events = [29, 30, 31, 32, 35, 36, 37, 38]
        unstable_tachyarrhythmia = any(events[i] > 0 for i in unstable_tachyarrhythmia_events)
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)   # Attach defib pads
                continue
            take_action(40)       # Defibrillator charge
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # Start Chest Compression for extreme hypotension
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # Use Bag Valve Mask for extreme hypoxia
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids for hypotension
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask for hypoxia
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag Valve Mask for low respiration
            continue

        take_action(48)
        return

if __name__ == "__main__":
    stabilize()