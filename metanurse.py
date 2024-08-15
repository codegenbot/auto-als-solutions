import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = [24, 25, 27]

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def needs_measurements():
        return not all(action in actions_taken for action in required_measurements)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Handle Emergency Conditions
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # StartChestCompression
            continue
        
        # Check if all necessary measurements have been taken
        if needs_measurements():
            take_action(next_measurement_action())
            continue
        
        # A - Airway
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # ExamineAirway
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # UseYankeurSucionCatheter
            elif events[6] > 0:
                take_action(32)  # UseGuedelAirway
            continue
        
        # B - Breathing
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue
        
        # C - Circulation
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Electrical issues requiring inspection
        if vitals["HR"] is not None and any(events[i] > 0 for i in range(27, 38)):
            take_action(24)  # UseMonitorPads
            take_action(2)  # CheckRhythm
            continue

        # Final check if stabilized
        if (vitals["Sats"] is not None and vitals["Sats"] >= 88 and 
            vitals["RR"] is not None and vitals["RR"] >= 8 and 
            vitals["MAP"] is not None and vitals["MAP"] >= 60):
            take_action(48)  # Finish
            break

if __name__ == "__main__":
    stabilize()