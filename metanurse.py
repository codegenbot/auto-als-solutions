import sys

def stabilize():
    max_steps = 350

    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions = {25, 27, 16, 3}  # UseSatsProbe, UseBPCuff, ViewMonitor, ExamineAirway
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_times, vitals = observations[:33], observations[33:40], observations[40:]

        measurements = {
            "RespRate": vitals[1] if vital_times[1] > 0 else None,
            "MAP": vitals[4] if vital_times[4] > 0 else None,
            "Sats": vitals[5] if vital_times[5] > 0 else None,
        }

        # Initial setup - use SatProbe, BP Cuff, View Monitor
        if any(a not in actions for a in [25, 27, 16]):
            for action in [25, 27, 16]:
                if action not in actions:
                    take_action(action)
                    actions.add(action)
                    break
            continue

        # Assess Airway
        if 3 not in actions:
            take_action(3)  # Examine Airway
            actions.add(3)
            continue
        
        airway_clear = events[3] > 0

        if events[4] > 0 or events[5] > 0:
            take_action(31)  # Use Yankeur Suction Catheter
            continue

        if events[6] > 0:
            take_action(36)  # Perform Head-Tilt Chin-Lift
            continue

        # Assess Breathing
        if 30 not in actions:
            if measurements["Sats"] is not None and measurements["Sats"] < 88:
                take_action(30)  # Use Non-Rebreather Mask
                actions.add(30)
                continue
               
            if measurements["RespRate"] is not None and measurements["RespRate"] < 8:
                take_action(29)  # Use Bag-Valve Mask
                actions.add(29)
                continue

        # Assess Circulation
        if measurements["MAP"] is not None and measurements["MAP"] < 60:
            if measurements["MAP"] < 20:
                take_action(23)  # Resume CPR
                continue

            # Detect potential arrhythmias
            arrhythmias = [28, 29, 32, 33, 34, 36, 37, 38]
            if any(events[i] > 0 for i in arrhythmias):
                take_action(24)  # Use Monitor Pads
                continue

            take_action(15)  # Give Fluids
            continue
        
        # Regular monitoring steps to diagnose and stabilize further
        if 33 not in actions:
            take_action(33)  # Take Blood for Arterial Blood Gas
            actions.add(33)
            continue

        # Final check for stability and finish
        if measurements["MAP"] >= 60 and measurements["Sats"] >= 88 and measurements["RespRate"] >= 8:
            take_action(48)  # Finish if stable
            break

if __name__ == "__main__":
    stabilize()