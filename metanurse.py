import sys

def main():
    max_steps = 350
    actions_taken = {
        'AirwayClear': False, 'BreathingDrawer': False, 'SatsProbe': False,
        'Monitor': False, 'BP_Cuff': False, 'Fluids': False, 'A_Line': False
    }
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, 
                        ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"])}
        
        # AIRWAY
        if not actions_taken['AirwayClear']:
            print(3)  # ExamineAirway
            actions_taken['AirwayClear'] = True
            continue
        
        # BREATHING
        if not actions_taken['BreathingDrawer']:
            print(19)  # OpenBreathingDrawer
            actions_taken['BreathingDrawer'] = True
            continue
        
        if not actions_taken['SatsProbe']:
            print(25)  # UseSatsProbe
            actions_taken['SatsProbe'] = True
            continue
        
        if not actions_taken['Monitor']:
            print(16)  # ViewMonitor
            actions_taken['Monitor'] = True
            continue
        
        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)  # StartChestCompression
            continue
        
        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue
        
        # CIRCULATION
        if not actions_taken['BP_Cuff']:
            print(27)  # UseBloodPressureCuff
            actions_taken['BP_Cuff'] = True
            continue
        
        if not actions_taken['Fluids']:
            print(15)  # GiveFluids
            actions_taken['Fluids'] = True
            continue
        
        if not actions_taken['A_Line']:
            print(26)  # UseAline
            actions_taken['A_Line'] = True
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            print(15)  # GiveFluids
            continue

        # Check Heart Rate for pharmacological intervention
        if vitals["HeartRate"]:
            if vitals["HeartRate"] > 150:
                print(10)  # GiveAdrenaline
                continue
            elif vitals["HeartRate"] > 100:
                print(9)  # GiveAdenosine
                continue
            elif vitals["HeartRate"] < 50:
                print(12)  # GiveAtropine
                continue
            
        print(48)  # Finish
        return

    print(48)

if __name__ == "__main__":
    main()