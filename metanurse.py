import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        sys.stdout.flush()

    initial_measurements_steps = [
        (25, 27, 26, 28)  # UseSatsProbe, UseBloodPressureCuff, UseAline, AttachDefibPads
    ]

    def needs_initial_measurements():
        return not all(action in actions_taken for action in initial_measurements_steps[0])

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue
            
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Cardiac arrest check
        if (vitals["MAP"] and vitals["MAP"] < 20) or (vitals["Sats"] and vitals["Sats"] < 65):
            take_action(17)  # StartChestCompression
            continue

        # Gather initial measurements if needed
        if needs_initial_measurements():
            for action in initial_measurements_steps[0]:
                if action not in actions_taken:
                    take_action(action)
                    break
            continue
            
        # Airway issues
        if any(events[i] > 0 for i in range(3, 7)):  # Check airway events
            take_action(3)
            if events[4] > 0 or events[5] > 0:  # Vomit, Blood
                take_action(31)  # UseSuction
            elif events[6] > 0:  # Tongue obstruction
                take_action(32)  # UseGuedelAirway
            continue

        # Breathing assessment and treatment
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vital_signs_values[1] == 0 or any(events[7:11]):  # BreathingNone, Snoring, SeeSaw, Unequal Chest Expansion
            take_action(4)  # ExamineBreathing
            if events[7] > 0:  # BreathingNone
                take_action(29)  # UseBagValveMask
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        
        if any(events[i] > 0 for i in range(7, 15)):  # Check other breathing events
            take_action(4)
            continue

        # Circulatory support
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue
        
        if any(events[i] > 0 for i in range(15, 20)):  # Check circulation events
            take_action(5)  # ExamineCirculation
            continue

        if any(events[i] > 0 for i in [33, 34, 36, 37, 38]):  # Rhythms that might need defib or cardiovert
            take_action(24)  # UseMonitorPads
            take_action(47)  # DefibrillatorSync
            continue

        # Finish when stabilized or on last step
        if step >= 349:
            take_action(48)  # Finish

        take_action(0)  # Default action: DoNothing when nothing urgent

if __name__ == "__main__":
    stabilize()