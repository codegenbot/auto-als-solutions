import sys

def stabilize():
    max_steps = 350
    
    def take_action(action):
        print(action)

    actions_taken = set()
    done = False
    critical_condition = False

    for step in range(max_steps):
        if done:
            break
        
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if vitals["MAP"] is None or vitals["Sats"] is None:
            if 25 not in actions_taken:
                actions_taken.add(25)
                take_action(25)
                continue
            if 27 not in actions_taken:
                actions_taken.add(27)
                take_action(27)
                continue
            if 16 not in actions_taken:
                actions_taken.add(16)
                take_action(16)
                continue
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)
            critical_condition = True
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)
            critical_condition = True
            continue
            
        if critical_condition:
            take_action(23)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if events[4] > 0 or events[5] > 0:  # Vomit, Blood in Airway
            take_action(31)
            continue

        if events[6] > 0:  # Tongue Obstruction
            take_action(36)
            continue

        if events[7] > 0:  # No Breathing
            take_action(29)
            continue

        if any(events[i] > 0 for i in range(28, 33)):  # Unstable Tachyarrhythmia
            if 28 not in actions_taken:
                take_action(28)
                continue
            take_action(40)
            continue

        take_action(48)  # Finish
        done = True

if __name__ == "__main__":
    stabilize()