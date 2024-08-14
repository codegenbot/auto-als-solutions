import sys

def stabilize():
    max_steps = 350
    
    def take_action(action):
        print(action)
        
    actions = {25, 27, 16, 3}  # Required: UseSatProbe, UseBPCuff, ViewMonitor, ExamineAirway
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_times, vitals = observations[:33], observations[33:40], observations[40:]

        measurements = {
            "RespRate": vitals[1] if vital_times[1] > 0 else None,
            "MAP": vitals[4] if vital_times[4] > 0 else None,
            "Sats": vitals[5] if vital_times[5] > 0 else None,
        }
        
        if any(a not in actions for a in [25, 27, 16]):
            for action in [25, 27, 16]:
                if action not in actions:
                    take_action(action)
                    actions.add(action)
                    break
            continue
        if 3 not in actions:
            take_action(3)
            actions.add(3)
            continue

        if measurements["MAP"] is not None and measurements["MAP"] < 20 or measurements["Sats"] is not None and measurements["Sats"] < 65:
            take_action(23)  # Resume CPR
            continue

        if measurements["MAP"] is not None and measurements["MAP"] < 60:
            if any(events[i] > 0 for i in [28, 29, 32, 33, 34]):
                take_action(24)  # Use Monitor Pads
            else:
                take_action(15)  # Give Fluids
            continue

        if measurements["Sats"] is not None and measurements["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if measurements["RespRate"] is not None and measurements["RespRate"] < 8:
            take_action(29)  # Use Bag-Valve Mask
            continue

        if any(events[i] > 0 for i in [4, 5]):
            take_action(31)  # Use Yankeur Suction Catheter
            continue
        
        if events[6] > 0:
            take_action(36)  # Perform Head-Tilt Chin-Lift
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(29)  # Use Bag-Valve Mask
            continue

        take_action(48)  # Finish if stable
    
if __name__ == "__main__":
    stabilize()