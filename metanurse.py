import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False
    
    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True
    
    def check_and_add_action(action, check_conditions):
        for condition in check_conditions:
            if condition not in actions_taken:
                take_action(action)
                return True
        return False

    for step in range(max_steps):
        if done:
            break
        
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {
            name: value if vital_signs_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                     "MAP", "Sats", "Resps"], vital_signs_values
                )
            )
        }
        
        # A – Airways
        if check_and_add_action(3, [3]):
            continue
        
        if events[3] == 0:
            continue

        # B – Breathing
        if check_and_add_action(4, [4, 14]):
            continue
        
        if vitals["Sats"] and vitals["Sats"] < 65:
            take_action(22)  # Bag during CPR for sats < 65%
            continue
        
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            take_action(29)  # Use bag valve mask for low Resp Rate
            continue
        
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask for sats < 88%
            continue

        # C – Circulation
        if check_and_add_action(5, [5, 6]):
            continue
        
        if vitals["MAP"] and vitals["MAP"] < 20:
            take_action(17)  # Start Chest Compression for MAP < 20
            continue
        
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # Give fluids for MAP < 60
            continue
        
        # Ensure we've used essential measurement tools
        if check_and_add_action(25, [25]):  # Use Sats Probe
            continue
        if check_and_add_action(27, [27]):  # Use Blood Pressure Cuff
            continue
        
        if 16 not in actions_taken:
            take_action(16)  # View Monitor
            continue

        # D – Disability (Handled indirectly by the conditions above)
        if check_and_add_action(6, [6, 7, 8]):
            continue
        
        # Making sure AVPU checks
        if check_and_add_action(8, [21, 22, 23]):
            continue
        
        # E – Exposure (Handled indirectly by the context)
        if check_and_add_action(7, [26, 33, 34]):
            continue
        
        # If all vital signs are stabilised, finish
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60]
            )
        ):
            take_action(48)
            return
        
        take_action(0)  # DoNothing in case no action is applicable
        
    take_action(48)  # Ensure the finish action at the end

if __name__ == "__main__":
    stabilize()