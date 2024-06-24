import sys
import math

def get_action(observations):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if step == 1:
        return 25  # Use SatsProbe
    elif step == 2:
        return 27  # Use BloodPressureCuff
    elif step == 3:
        return 3  # Examine Airway
    elif step >= 4:
        if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
            return 17  # Start Chest Compression
        if events[7] > 0:  # BreathingNone
            return 22  # Bag During CPR
        
        if (sats is not None and sats >= 88) and (resp_rate is not None and resp_rate >= 8) and (map_value is not None and map_value >= 60):
            return 48  # Finish
            
        if sats is None:
            return 16  # View Monitor for Sats
        if resp_rate is None:
            return 4  # Examine Breathing
        if map_value is None:
            return 16  # View Monitor
    
    return 1  # Default to Check Signs of Life

step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    step += 1
    action = get_action(input_data)
    print(action)
    if action == 48:
        break