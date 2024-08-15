import sys
import math

def stabilize():
    max_steps = 350
    step = 0
    actions_taken = set()

    def take_action(action):
        print(action)
        sys.stdout.flush()
        actions_taken.add(action)

    def measure_vitals():
        if 25 not in actions_taken: return 25
        if 26 not in actions_taken: return 26
        if 27 not in actions_taken: return 27
        if 16 not in actions_taken: return 16
        return None

    while step < max_steps:
        observations = list(map(float, sys.stdin.readline().strip().split()))
        step += 1
        
        if len(observations) != 53:
            continue
        
        events, vitals_times, vitals_values = observations[:33], observations[33:40], observations[40:]
        vitals = {
            "HR": vitals_values[0] if vitals_times[0] > 0 else None,
            "RR": vitals_values[1] if vitals_times[1] > 0 else None,
            "MAP": vitals_values[4] if vitals_times[4] > 0 else None,
            "Sats": vitals_values[5] if vitals_times[5] > 0 else None,
        }

        if vitals["MAP"] is not None and vitals["MAP"] < 20 or vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(17)  # Start Chest Compression
            continue
        
        if any(events[i] > 0 for i in range(3, 7)):  # Airway issues
            take_action(3)
            if any(events[i] > 0 for i in [4, 5, 6]):  # Vomit, Blood, Tongue
                take_action(31)  # Use Suction
            elif events[6] > 0:
                take_action(32)  # Use Guedel Airway
            continue
        
        measurement_action = measure_vitals()
        if measurement_action:
            take_action(measurement_action)
            continue
            
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue
        
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue
        
        if any(events[i] > 0 for i in range(7, 14)):  # Breathing issues
            take_action(4)
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue
        
        if any(events[i] > 0 for i in range(14, 21)):  # Circulation issues
            take_action(5)
            continue

        if (25 in actions_taken and 26 in actions_taken and 27 in actions_taken and 16 in actions_taken and
            vitals["Sats"] >= 88 and vitals["RR"] >= 8 and vitals["MAP"] >= 60):
            take_action(48)  # Finish
            break

        take_action(0)  # Do Nothing

if __name__ == "__main__":
    stabilize()