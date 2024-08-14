import sys

# Define constants for action indices
DO_NOTHING = 0
USE_SATS_PROBE = 25
USE_BLOOD_PRESSURE_CUFF = 27
VIEW_MONITOR = 16
EXAMINE_AIRWAY = 3
EXAMINE_BREATHING = 4
EXAMINE_CIRCULATION = 5
EXAMINE_DISABILITY = 6
EXAMINE_EXPOSURE = 7
USE_NON_REBREATHER_MASK = 30
GIVE_FLUIDS = 15
USE_MONITOR_PADS = 24
CHECK_RHYTHM = 2
GIVE_ADRENALINE = 10
FINISH = 48

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = [USE_SATS_PROBE, USE_BLOOD_PRESSURE_CUFF, VIEW_MONITOR, EXAMINE_AIRWAY]

    def needs_measurements():
        return any(action not in actions_taken for action in required_measurements)

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            'RespRate': vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            'MAP': vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            'Sats': vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        if (vitals['MAP'] is not None and vitals['MAP'] < 20) or (
            vitals['Sats'] is not None and vitals['Sats'] < 65
        ):
            take_action(USE_MONITOR_PADS)
            take_action(CHECK_RHYTHM)
            take_action(GIVE_ADRENALINE)
            take_action(FINISH)
            continue

        if vitals['MAP'] is not None and vitals['MAP'] < 60:
            take_action(GIVE_FLUIDS)
            take_action(CHECK_RHYTHM)
            continue

        if vitals['Sats'] is not None and vitals['Sats'] < 88:
            take_action(USE_NON_REBREATHER_MASK)
            continue

        if any(events[i] > 0 for i in [1, 2, 4, 5, 6, 7, 10, 11, 12, 13, 14]):
            take_action(EXAMINE_AIRWAY)
            continue

        take_action(FINISH)
        break

if __name__ == "__main__":
    stabilize()