import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    examined = {"Airway": False, "Breathing": False, "Circulation": False, "Disability": False, "Exposure": False}
    vitals_measured = {"MAP": False, "Sats": False, "RespRate": False}
    
    def take_action(action):
        print(action)
        actions_taken.add(action)

    def examine_type():
        if not examined["Airway"]:
            return 3
        if not examined["Breathing"]:
            return 4
        if not examined["Circulation"]:
            return 5
        if not examined["Disability"]:
            return 6
        if not examined["Exposure"]:
            return 7

    def needs_vitals():
        for k in vitals_measured:
            if not vitals_measured[k]:
                return True
        return False
    
    def next_vital_action():
        measurement_map = {"MAP": 27, "Sats": 25, "RespRate": 24}
        for k in vitals_measured:
            if not vitals_measured[k]:
                return measurement_map[k]

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        
        if step == 0:
            take_action(1)
            continue

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }
        
        vitals_measured.update({
            "RespRate": True if vitals["RespRate"] is not None else vitals_measured["RespRate"],
            "MAP": True if vitals["MAP"] is not None else vitals_measured["MAP"],
            "Sats": True if vitals["Sats"] is not None else vitals_measured["Sats"]
        })

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)
            continue

        if needs_vitals():
            take_action(next_vital_action())
            continue

        if not all(examined.values()):
            action = examine_type()
            examined.update({"Airway": examined["Airway"] or action == 3,
                             "Breathing": examined["Breathing"] or action == 4,
                             "Circulation": examined["Circulation"] or action == 5,
                             "Disability": examined["Disability"] or action == 6,
                             "Exposure": examined["Exposure"] or action == 7})
            take_action(action)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)
            continue

        take_action(48)
    
if __name__ == "__main__":
    stabilize()