import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    
    def take_action(action):
        print(action)
        actions_taken.add(action)

    def check_vitals(observations):
        return {
            "RespRate": observations[41] if observations[34] else None,
            "MAP": observations[44] if observations[38] else None,
            "Sats": observations[45] if observations[39] else None
        }

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = check_vitals(observations)

        if 3 in actions_taken:  # Airway
            if any(events[i] for i in [4, 5]):  # Vomit, Blood
                take_action(31)
                continue
            if events[6]:  # Tongue
                take_action(36)
                continue

        if 4 in actions_taken:  # Breathing
            if vitals["Sats"] is None:
                take_action(25)
                continue
            if vitals["Sats"] < 65 or vitals["MAP"] < 20:
                take_action(23)
                continue
            if vitals["Sats"] < 88:
                take_action(29)
                continue
            if vitals["RespRate"] is None:
                take_action(16)
                continue
            if vitals["RespRate"] < 8:
                take_action(29)
                continue
            
        if 5 in actions_taken:  # Circulation
            if vitals["MAP"] is None:
                take_action(27)
                continue
            if vitals["MAP"] < 60:
                if any(events[i] for i in range(29, 39)):  # Check arrhythmia
                    take_action(24)
                    continue
                take_action(15)
                continue

        # Do a specific exam based on remaining assessments
        if len(actions_taken) < 4:
            next_action = [3, 4, 5, 6, 7][len(actions_taken)]
            take_action(next_action)
            continue
        
        take_action(48)
        break

if __name__ == "__main__":
    stabilize()