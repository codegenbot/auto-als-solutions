import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    examined_vitals = set()

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

        # Check if John is going into cardiac arrest
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)
            continue

        # Examine Airway (A)
        if any(events[i] > 0 for i in range(3, 7)) and "AirwayExamined" not in examined_vitals:
            take_action(3)
            examined_vitals.add("AirwayExamined")
            continue

        # Examine Breathing (B)
        if any(events[i] > 0 for i in range(7, 15)) and "BreathingExamined" not in examined_vitals:
            take_action(4)
            examined_vitals.add("BreathingExamined")
            continue

        # Examine Circulation (C)
        if any(events[i] > 0 for i in range(15, 20)) and "CirculationExamined" not in examined_vitals:
            take_action(5)
            examined_vitals.add("CirculationExamined")
            continue

        if vitals["MAP"] is None and "BPCuffApplied" not in examined_vitals:
            take_action(27)
            examined_vitals.add("BPCuffApplied")
            continue

        if vitals["Sats"] is None and "SatsProbeApplied" not in examined_vitals:
            take_action(25)
            examined_vitals.add("SatsProbeApplied")
            continue
        
        # Examine vitals if measurements are not recent
        if vitals["RR"] is None and "BreathingExamined" not in examined_vitals:
            take_action(4)
            examined_vitals.add("BreathingExamined")
            continue
        
        # Check if we have the measurements
        if 'monitor' not in examined_vitals:
            take_action(16)
            examined_vitals.add('monitor')
            continue
        
        # Stabilize based on vitals
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give Fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use Non-Rebreather Mask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # Use Bag Valve Mask
            continue

        # If all vital signs are stable, finish
        if (vitals["MAP"] is not None and vitals["MAP"] >= 60 and
            vitals["Sats"] is not None and vitals["Sats"] >= 88 and
            vitals["RR"] is not None and vitals["RR"] >= 8):
            take_action(48)  # Finish
            break

if __name__ == "__main__":
    stabilize()