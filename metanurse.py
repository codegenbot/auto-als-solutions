import sys

def stabilize():
    max_steps = 350

    def take_action(action):
        print(action)
        sys.stdout.flush()
    
    def should_use_readings(vital_signs_times):
        examine = []
        if vital_signs_times[5] <= 0:  # Check Sats
            examine.append(25)
        if vital_signs_times[4] <= 0:  # Check MAP
            examine.append(27)
        if vital_signs_times[1] <= 0:  # Check RR
            examine.append(26)
        if vital_signs_times[0] <= 0:  # Check HR
            examine.append(28)
        return examine

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        initial_measurements = should_use_readings(vital_signs_times)
        if initial_measurements:
            take_action(initial_measurements[0])
            continue

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if vitals["MAP"] is not None and vitals["MAP"] < 20 or vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(17)  # Cardiac arrest, start CPR
            continue

        # ABCDE Assessment
        # A: Airways
        if events[1] > 0 or events[2] > 0:
            take_action(3)  # Examine airway
            continue
        if events[4] > 0 or events[5] > 0 or events[6] > 0:
            take_action(31)  # Use suction
            continue
        
        # B: Breathing
        if events[7] > 0:
            take_action(4)  # Examine breathing
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use bag valve mask
            continue
        
        # C: Circulation
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue
        if events[16] <= 0 and events[17] <= 0:
            take_action(5)  # Examine circulation
            continue
   
        # D: Disability
        if events[22] > 0 or events[21] > 0:
            take_action(6)  # Examine disability
            continue

        # E: Exposure
        if events[25] <= 0:
            take_action(7)  # Examine exposure
            continue

        # If step >= 349 then finish
        if step >= 349:
            take_action(48)
            break
        
        take_action(0)  # Do nothing

if __name__ == "__main__":
    stabilize()