import sys

def stabilize():
    max_steps = 350
    
    def take_action(action):
        print(action)
        sys.stdout.flush()
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        
        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] else None,
        }
        
        if not vital_signs_times[5]:
            take_action(25)  # Use Sats Probe
            continue
        if not vital_signs_times[4]:
            take_action(27)  # Use Blood Pressure Cuff
            continue
        if not vital_signs_times[1]:
            take_action(24)  # Use Monitor Pads
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # Start Chest Compressions
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue
        
        if any(events[i] > 0 for i in range(1, 4)):  # Examine response
            take_action(8)  # Examine response
            continue
        
        if any(events[i] > 0 for i in [10, 11, 12, 13, 14]):  # Breathing problems
            if events[13] > 0:
                take_action(5)  # Perform needle decompression
            else:
                take_action(4)  # Examine Breathing
            continue
        
        if any(events[i] > 0 for i in [3, 4, 5, 6, 7]):  # Airway problems
            if events[6] > 0:
                take_action(36)  # Perform Head Tilt Chin Lift
            else:
                take_action(3)  # Examine Airway
            continue
        
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()