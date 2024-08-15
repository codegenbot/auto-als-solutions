import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
        sys.stdout.flush()

    initial_measurements = [25, 26, 27, 28]

    def next_initial_measurement_action():
        for action in initial_measurements:
            if action not in actions_taken:
                return action

    def needs_initial_measurements():
        return not all(action in actions_taken for action in initial_measurements)

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

        # Cardiac arrest conditions
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)
            continue

        # Initial assessments
        if needs_initial_measurements():
            take_action(next_initial_measurement_action())
            continue

        # Airway checks
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # Suction catheter
            elif events[6] > 0:
                take_action(32)  # Guedel airway
            take_action(35)  # PerformAirwayManoeuvres
            continue

        # Low oxygen saturation
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        # Low respiratory rate
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Breathing checks
        if events[7] > 0 or events[9] > 0 or events[10] > 0:
            take_action(4)  # ExamineBreathing
            continue

        # Low mean arterial pressure
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Examination for other ABCDE protocols
        if step % 5 == 0:
            take_action(3)  # ExamineAirway
            continue
        if step % 10 == 0:
            take_action(4)  # ExamineBreathing
            continue
        if step % 15 == 0:
            take_action(5)  # ExamineCirculation
            continue
        if step % 20 == 0:
            take_action(6)  # ExamineDisability
            continue

        # Finish action
        if step >= 349:
            take_action(48)

        take_action(0)

if __name__ == "__main__":
    stabilize()