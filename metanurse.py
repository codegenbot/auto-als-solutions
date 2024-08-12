import sys

def main():
    max_steps = 350
    opened_drawers = {19: False, 20: False}
    used_methods = {'UsedSatsProbe': False, 'ViewedMonitor': False, 'BP_Cuff': False, 
                    'A_Line': False, 'Fluids': False, 'ExaminedCirculation': False}
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        
        vitals = {name: value if time > 0 else None for value, time, name in 
                  zip(vital_signs_values, vital_signs_times, ["HeartRate", "RespRate", "CapillaryGlucose", 
                                                              "Temperature", "MAP", "Sats", "Resps"])}
        
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
            print(17)  # StartChestCompression
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            print(29)  # UseBagValveMask
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            if not used_methods['ExaminedCirculation']:
                print(5)  # ExamineCirculation
                used_methods['ExaminedCirculation'] = True
                continue
            if not used_methods['BP_Cuff']:
                print(27)  # UseBloodPressureCuff
                used_methods['BP_Cuff'] = True
                continue
            if not used_methods['A_Line']:
                print(26)  # UseAline
                used_methods['A_Line'] = True
                continue
            if not used_methods['Fluids']:
                print(15)  # GiveFluids
                used_methods['Fluids'] = True
                continue

        if vitals["HeartRate"]:
            if vitals["HeartRate"] > 150:
                print(9)  # GiveAdenosine
                continue
            elif 100 < vitals["HeartRate"] <= 150:
                print(10)  # GiveAdrenaline
                continue
            elif vitals["HeartRate"] < 50:
                print(12)  # GiveAtropine
                continue
        
        print(48)  # Finish
        return

    print(48)

if __name__ == "__main__":
    main()