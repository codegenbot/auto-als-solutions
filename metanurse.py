import sys

def stabilize():
    max_steps = 350
    step_state = {"examine_airway": False, "use_sats_probe": False, "use_blood_pressure_cuff": False, "view_monitor": False, "use_aline": False, "check_resprate": False}
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values,
                vital_signs_times,
                ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"]
            )
        }

        if step == 0 or not step_state["examine_airway"]:
            step_state["examine_airway"] = True
            print(3)
            continue
        
        if not step_state["use_sats_probe"]:
            step_state["use_sats_probe"] = True
            print(25)
            continue
        
        if not step_state["use_blood_pressure_cuff"]:
            step_state["use_blood_pressure_cuff"] = True
            print(27)
            continue
        
        if not step_state["view_monitor"]:
            step_state["view_monitor"] = True
            print(16)
            continue
        
        if not step_state["use_aline"]:
            step_state["use_aline"] = True
            print(26)
            continue
        
        if not step_state["check_resprate"]:
            step_state["check_resprate"] = True
            print(4)
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            print(17)
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            print(17)
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            print(15)
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            print(30)
            continue
        
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            print(29)
            continue
        
        if vitals["HeartRate"] is not None:
            if vitals["HeartRate"] > 150 or vitals["HeartRate"] < 50:
                print(24)
                continue
        
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            print(48)
            return
        
        print(48)
        return

if __name__ == "__main__":
    stabilize()