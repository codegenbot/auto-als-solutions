import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    
    def take_action(action):
        print(action)
        actions_taken.add(action)
        sys.stdout.flush()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Initial measurements
        if 25 not in actions_taken:
            take_action(25)  # UseSatsProbe
            continue
        if 27 not in actions_taken:
            take_action(27)  # UseBloodPressureCuff
            continue
        if 24 not in actions_taken:
            take_action(24)  # UseMonitorPads
            continue

        # Critical conditions
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # Start chest compression
            continue

        # Airway
        if any(events[i] > 0 for i in [4, 5, 6]):
            take_action(3)  # Examine Airway
            if events[5] > 0:
                take_action(31)  # Use Yankeur Suction Catheter
            elif events[6] > 0:
                take_action(36)  # Perform Head-Tilt Chin-Lift
            continue

        # Breathing
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use bag-valve mask
            continue
        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(4)  # Examine Breathing
            if events[7] > 0:
                take_action(29)  # Use bag-valve mask
            continue

        # Circulation
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue
        if events[15] > 0:  # VentilationResistance
            take_action(2)  # CheckRhythm
            continue
        if events[20] > 0:  # HeartSoundsMuffled
            take_action(40)  # DefibrillatorCharge
            continue
            
        # Disability
        if any(events[i] > 0 for i in [1, 2, 3]):
            take_action(8)  # Examine Response
            continue
        
        # Exposure
        if any(events[i] > 0 for i in range(27, 30)):
            take_action(7)  # Examine Exposure
            continue

        # Default action if everything is stable
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()