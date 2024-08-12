import sys

def main():
    max_steps = 350
    opened_drawers = {19: False, 20: False}
    used_methods = {'UsedSatsProbe': False, 'ViewedMonitor': False, 
                    'BP_Cuff': False, 'A_Line': False, 'Fluids': False}
    finished = False
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        
        vitals = {name: value if time > 0 else None for value, time, name in 
                  zip(vital_signs_values, vital_signs_times, 
                      ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"])}
        
        if not events[3]:
            print(3)  # ExamineAirway
            continue
        
        if not opened_drawers[19]:
            print(19)  # OpenBreathingDrawer
            opened_drawers[19] = True
            continue

        if not used_methods['UsedSatsProbe']:
            print(25)  # UseSatsProbe
            used_methods['UsedSatsProbe'] = True
            continue

        if not used_methods['ViewedMonitor']:
            print(16)  # ViewMonitor
            used_methods['ViewedMonitor'] = True
            continue
        
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)  # Start chest compressions
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # Use non-rebreather mask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # Use bag valve mask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            if not used_methods['BP_Cuff']:
                print(27)  # Apply BP cuff
                used_methods['BP_Cuff'] = True
            elif not used_methods['A_Line']:
                print(26)  # Use arterial line
                used_methods['A_Line'] = True
            elif not used_methods['Fluids']:
                print(15)  # Give fluids
                used_methods['Fluids'] = True
            continue

        if vitals["HeartRate"]:
            if vitals["HeartRate"] < 50:
                print(12)  # Give Atropine
                continue
            elif vitals["HeartRate"] > 150:
                print(2)  # Check rhythm
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(2)  # Check rhythm
                continue
        
        finished = True
        print(48)
        break

    if not finished:
        print(48)

if __name__ == "__main__":
    main()