import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        sys.stdout.flush()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )

        def get_vital_sign(index):
            return vital_signs_values[index] if vital_signs_times[index] > 0 else None

        vitals = {
            "RespRate": get_vital_sign(1),
            "MAP": get_vital_sign(4),
            "Sats": get_vital_sign(5),
        }

        if 25 not in actions_taken: take_action(25); continue  # UseSatsProbe
        if 27 not in actions_taken: take_action(27); continue  # UseBloodPressureCuff
        if 24 not in actions_taken: take_action(24); continue  # UseMonitorPads

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17); continue  # Start chest compression
        if vitals["Sats"] is None: take_action(16); continue  # View Monitor for sats
        if vitals["MAP"] is None: take_action(38); continue  # Take Blood Pressure

        if any(events[i] > 0 for i in [4, 5, 6]):
            take_action(3);  # Examine Airway
            if events[5] > 0: take_action(31); continue  # Use Yankeur Suction Catheter
            if events[6] > 0: take_action(36); continue  # Perform Head-Tilt Chin-Lift

        if vitals["Sats"] is not None and vitals["Sats"] < 88: take_action(30); continue  # Use Non-Rebreather Mask
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8: take_action(29); continue  # Use Bag-Valve Mask
        if any(events[i] > 0 for i in [7, 11, 12, 13, 14]):
            take_action(4);  # Examine Breathing
            if events[7] > 0: take_action(29); continue  # Use Bag-Valve Mask

        if vitals["MAP"] is not None and vitals["MAP"] < 60: take_action(15); continue  # Give Fluids
        if 39 in actions_taken:
            if any(events[i] > 0 for i in [28, 32, 33, 34, 35, 37, 38, 41]):
                take_action(24); continue  # UseMonitorPads
            else:
                take_action(40); continue  # DefibrillatorCharge

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()