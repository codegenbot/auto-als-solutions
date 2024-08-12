import sys

def main():
    max_steps = 350
    actions_taken = {'BreathingDrawer': False, 'SatsProbe': False, 'Monitor': False, 'BPCuff': False, 
                     'Fluids': False, 'A_Line': False, 'CirculationDrawer': False}

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, 
                        ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"])}

        # A - Airway
        if not events[3]:  # Check if airway is clear
            print(3)
            continue

        # B - Breathing
        if not actions_taken['BreathingDrawer']:
            print(19)
            actions_taken['BreathingDrawer'] = True
            continue
            
        if not actions_taken['SatsProbe']:
            print(25)
            actions_taken['SatsProbe'] = True
            continue
            
        if not actions_taken['Monitor']:
            print(16)
            actions_taken['Monitor'] = True
            continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            print(17)  # Cardiac arrest if sats < 65
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)
            continue

        # C - Circulation
        if not actions_taken['CirculationDrawer']:
            print(20)
            actions_taken['CirculationDrawer'] = True
            continue

        if vitals["MAP"] and vitals["MAP"] < 20:
            print(17)  # Cardiac arrest if MAP < 20
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            if not actions_taken['BPCuff']:
                print(27)
                actions_taken['BPCuff'] = True
                continue
            if not actions_taken['Fluids']:
                print(15)
                actions_taken['Fluids'] = True
                continue
            if not actions_taken['A_Line']:
                print(26)
                actions_taken['A_Line'] = True
                continue
        
        # Heart rate treatments
        if vitals["HeartRate"]:
            if vitals["HeartRate"] > 150:
                print(10)
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(9)
                continue
            elif vitals["HeartRate"] < 50:
                print(12)
                continue
        
        # Finish if all stable
        if all([vitals["Sats"] >= 88, vitals["RespRate"] >= 8, vitals["MAP"] >= 60]):
            print(48)
            return

        print(0)  # Do nothing if no specific action required yet

    print(48)  # Ensure to finish after max steps

if __name__ == "__main__":
    main()