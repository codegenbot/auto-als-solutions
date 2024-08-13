import sys

def stabilize():
    max_steps = 350
    assess_status = {'A': False, 'B': False, 'C': False, 'D': False, 'E': False}
    actions_taken = set()
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}
        
        if not assess_status['A']:
            assess_status['A'] = True
            print(3)  # Examine Airway
            continue
            
        if not assess_status['B']:
            assess_status['B'] = True
            print(4)  # Examine Breathing
            continue
        
        if not assess_status['C']:
            assess_status['C'] = True
            print(5)  # Examine Circulation
            continue

        if vitals["Sats"] is None and 25 not in actions_taken:
            print(25)  # Use Sats Probe
            actions_taken.add(25)
            continue

        if vitals["MAP"] is None and 27 not in actions_taken:
            print(27)  # Use Blood Pressure Cuff
            actions_taken.add(27)
            continue
        
        if not any("HeartRhythm" in event_name for event_name in events) and 2 not in actions_taken:
            print(2)  # CheckRhythm
            actions_taken.add(2)
            continue

        if not assess_status['E'] and all(checked for _, checked in assess_status.items()):
            assess_status['E'] = True
            print(7)  # Examine Exposure
            continue

        if vitals["HeartRate"] is not None and vitals["HeartRate"] > 150:
            if any(event in events and events[event] > 0 
                   for event in ["HeartRhythmAF", "HeartRhythmVT", "HeartRhythmSVT"]):
                print(47)  # DefibrillatorSync
                continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)  # Start Chest Compression
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)  # Start Chest Compression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # Give Fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # Use Non Rebreather Mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # Use Bag Valve Mask
            continue
        
        if vitals["HeartRate"] is not None and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50):
            print(43)  # Defibrillator Pace
            continue

        if all([vitals["Sats"] is not None and vitals["Sats"] >= 88,
                vitals["RespRate"] is not None and vitals["RespRate"] >= 8,
                vitals["MAP"] is not None and vitals["MAP"] >= 60]):
            print(48)  # Finish
            return

        print(48)  # Finish
        return

if __name__ == "__main__":
    stabilize()