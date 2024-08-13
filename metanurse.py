import sys

def main():
    max_steps = 350
    used_methods = set()
    examine_steps = [3, 4, 5, 6, 7, 8]
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {name: value if time > 0 else None for value, time, name in zip(vital_signs_values, vital_signs_times, [
            "HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"
        ])}

        # Initial examination steps
        if step < len(examine_steps):
            print(examine_steps[step])
            continue

        # Ensure initial checks with probes and monitors
        if "UseSatsProbe" not in used_methods:
            print(25)
            used_methods.add("UseSatsProbe")
            continue
        if "UseBloodPressureCuff" not in used_methods:
            print(27)
            used_methods.add("UseBloodPressureCuff")
            continue
        if "ViewMonitor" not in used_methods:
            print(16)
            used_methods.add("ViewMonitor")
            continue

        # Handle unstable critical values for cardiac arrest
        if vitals["Sats"] is not None and (vitals["Sats"] < 65 or vitals["MAP"] is not None and vitals["MAP"] < 20):
            print(17)  # Start chest compressions
            continue
        
        # Administer treatment based on vitals assessments
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)  # Use non-rebreather mask
            continue
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)  # Use bag-valve mask
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)  # Administer fluids
            continue
        
        # Handle abnormal heart rate if MAP is low
        if vitals["MAP"] is not None and vitals["MAP"] < 60 and (vitals["HeartRate"] < 60 or vitals["HeartRate"] > 100):
            if "TurnOnDefibrillator" not in used_methods:
                print(39)
                used_methods.add("TurnOnDefibrillator")
                continue
            if "DefibrillatorCharge" not in used_methods:
                print(40)
                used_methods.add("DefibrillatorCharge")
                continue
            print(43)  # Pace heart
            continue
        
        # Finish if all vitals are stable
        if all(vital is not None and vital >= threshold for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60])):
            print(48)
            return
        
        # Default to finish
        print(48)
        return

if __name__ == "__main__":
    main()