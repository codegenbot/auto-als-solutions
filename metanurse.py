import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()

    actions_priority = [
        (32, "events[4]", None, None),       # OpenAirway if AirwayVomit
        (31, "events[5]", None, None),       # Suction if AirwayBlood
        (36, "events[6]", None, None),       # HeadTiltChinLift if AirwayTongue 
        (25, "vitals['Sats'] is None", None, None),  # Use Sats Probe if Sats not measured
        (3, "True", None, None),             # Examine Airway
        (30, "vitals['Sats'] < 88", None, None),  # Use NonRebreatherMask if Sats < 88
        (4, "vitals['RR'] is None", None, None),   # Examine Breathing
        (29, "vitals['RR'] < 8", None, None),      # Use BagValveMask if RR < 8
        (5, "vitals['MAP'] is None", None, None),  # Examine Circulation
        (27, "vitals['MAP'] < 60", None, None),    # Use Blood Pressure Cuff if MAP < 60
        (15, "vitals['MAP'] < 60", None, None),    # Give Fluids if MAP < 60
        (6, "events[20]", None, None),       # Examine Disability if AVPU_A event
        (7, "events[26]", None, None),       # Examine Exposure if ExposureRash
    ]

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # Start Chest Compression
            continue

        for action, condition, fallback, dependent in actions_priority:
            if eval(condition):
                take_action(action)
                if fallback is not None:
                    examined_vitals.add(fallback)
                break
        else:
            take_action(48)
            break

if __name__ == "__main__":
    stabilize()