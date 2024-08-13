import sys

def main():
    max_steps = 350
    used_methods = set()
    initial_examine = [False] * 5

    def check_airway(events):
        if not events[3]:  # AirwayClear
            if events[4] or events[5] or events[6]:  # Airway issues
                return 31  # UseYankeurSucionCatheter for vomit/blood
            return 35  # PerformAirwayManoeuvres for tongue
        return None

    def check_breathing(vitals):
        if vitals["Sats"] and vitals["Sats"] < 88:
            return 30  # UseNonRebreatherMask
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            return 29  # UseBagValveMask
        return None

    def check_circulation(vitals, events):
        if vitals["MAP"] and vitals["MAP"] < 60:
            return 15  # GiveFluids
        if vitals["HeartRate"] and (vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50) or events[27]:
            if "TurnOnDefibrillator" not in used_methods:
                used_methods.add("TurnOnDefibrillator")
                return 39  # TurnOnDefibrillator
            elif "DefibrillatorCharge" not in used_methods:
                used_methods.add("DefibrillatorCharge")
                return 40  # DefibrillatorCharge
            elif "DefibrillatorSync" not in used_methods:
                used_methods.add("DefibrillatorSync")
                return 47  # DefibrillatorSync
            else:
                return 43  # DefibrillatorPace
        return None
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"])}

        if not initial_examine[0]:
            print(3)  # ExamineAirway
            initial_examine[0] = True
            continue
        if not initial_examine[1]:
            print(4)  # ExamineBreathing
            initial_examine[1] = True
            continue
        if not initial_examine[2]:
            print(5)  # ExamineCirculation
            initial_examine[2] = True
            continue
        if not initial_examine[3]:
            print(6)  # ExamineDisability
            initial_examine[3] = True
            continue
        if not initial_examine[4]:
            print(7)  # ExamineExposure
            initial_examine[4] = True
            continue

        action = check_airway(events)
        if action:
            print(action)
            continue
        
        if "UseSatsProbe" not in used_methods:
            print(25)  # UseSatsProbe
            used_methods.add("UseSatsProbe")
            continue
        if "UseBloodPressureCuff" not in used_methods:
            print(27)  # UseBloodPressureCuff
            used_methods.add("UseBloodPressureCuff")
            continue
        if "ViewMonitor" not in used_methods:
            print(16)  # ViewMonitor
            used_methods.add("ViewMonitor")
            continue

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            print(17)  # StartChestCompression
            continue

        action = check_breathing(vitals)
        if action:
            print(action)
            continue
        
        action = check_circulation(vitals, events)
        if action:
            print(action)
            continue
        
        print(48)  # Finish
        return

    print(48)

if __name__ == "__main__":
    main()