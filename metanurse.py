import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    def get_observations():
        return list(map(float, input().strip().split()))

    def needs_measurements(vitals):
        return (vitals["HR"] is None or vitals["RR"] is None or 
                vitals["MAP"] is None or vitals["Sats"] is None)

    def perform_abcde(events, vitals):
        if any(events[i] > 0 for i in range(3, 7)):  # Airway issues
            take_action(3)  # Examine Airway
            if events[4] > 0 or events[5] > 0:  # Vomit or Blood
                take_action(31)  # Suction
            if events[6] > 0:  # Tongue obstruction
                take_action(32)  # Guedel Airway
            return

        if vitals["Sats"] is not None and vitals["Sats"] < 88:  # Low Oxygen
            take_action(30)  # Use Non-Rebreather Mask
            return

        if vitals["RR"] is not None and vitals["RR"] < 8:  # Low Resp Rate
            take_action(29)  # Use Bag-Valve Mask
            return

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing issues
            take_action(4)  # Examine Breathing
            return

        if vitals["MAP"] is not None and vitals["MAP"] < 60:  # Low MAP
            take_action(15)  # Administer fluids
            return

        if any(events[i] > 0 for i in range(15, 20)):  # Circulation issues
            take_action(5)  # Examine Circulation
            return

        # Checking abnormal heart rhythms
        if vitals["HR"] is not None and any(events[i] > 0 for i in range(27, 40)):
            take_action(24)  # Use Monitor Pads
            take_action(2)   # Check Rhythm
            return

        take_action(48)  # Finish action

    actions_taken = set()
    required_measurements = [24, 25, 27]  # MonitorPads, SatsProbe, BP Cuff

    for step in range(350):  # Max steps
        observations = get_observations()
        if len(observations) != 53:
            continue

        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:])

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] else None,
        }

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # Start chest compression immediately
            continue

        if needs_measurements(vitals):
            for action in required_measurements:
                if action not in actions_taken:
                    take_action(action)
                    actions_taken.add(action)
                    break  # Continue from here after this action

        perform_abcde(events, vitals)
        if vitals["HR"] is not None and vitals["RR"] is not None and vitals["MAP"] is not None and vitals["Sats"] is not None:
            break  # End loop as we issue 'Finish' inside perform_abcde

if __name__ == "__main__":
    stabilize()