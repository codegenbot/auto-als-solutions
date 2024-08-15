import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    required_measurements = {24, 25, 27, 16}
    unstable_tach_arrhythmias = {36, 37, 38, 41, 42, 43, 47}

    def take_action(action):
        print(action)
        actions_taken.add(action)

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)

    for step in range(max_steps):
        observations = list(map(float, sys.stdin.readline().strip().split()))
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

        # Cardiac arrest conditions
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)
            continue

        # Initial measurements
        if needs_measurements():
            take_action(next_measurement_action())
            continue

        # Airway exams and actions
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)
            elif events[6] > 0:
                take_action(32)
            continue

        # Tachyarrhythmia and hemodynamic instability 
        if any(events[i] > 0 for i in range(32, 39)):
            take_action(28)  # AttachDefibPads before cardioversion
            take_action(40)  # DefibrillatorCharge
            take_action(43)  # DefibrillatorPace for cardioversion
            continue

        # Oxygen saturation < 88%
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        # Respiratory rate < 8
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        # Breathing exams
        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)
            continue

        # MAP < 60
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        # Circulation exams
        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)
            continue

        if step % 5 == 0:
            take_action(1)

        if step % 10 == 0:
            take_action(2)

        take_action(48)
        break

if __name__ == "__main__":
    stabilize()