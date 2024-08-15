import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    next_action = 0
    
    def take_action(action):
        print(action)
        actions_taken.add(action)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue
        
        events, vital_signs_times, vital_signs_values = (observations[:33], observations[33:40], observations[40:])
        vital_signs = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vital_signs["MAP"] is not None and vital_signs["MAP"] < 20) or (vital_signs["Sats"] is not None and vital_signs["Sats"] < 65):
            take_action(17)  # Start Chest Compression
            continue
        
        if 24 not in actions_taken:
            take_action(24)  # Use Monitor Pads
            continue
        
        if 27 not in actions_taken:
            take_action(27)  # Use BP Cuff
            continue
            
        if 25 not in actions_taken:
            take_action(25)  # Use Sats Probe
            continue

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # Examine Airway
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # Use Yankeur Suction
            elif events[6] > 0:
                take_action(32)  # Use Guedel Airway
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # Examine Breathing
            continue
        
        if vital_signs["Sats"] is not None and vital_signs["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vital_signs["RR"] is not None and vital_signs["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # Examine Circulation
            continue

        if vital_signs["MAP"] is not None and vital_signs["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()