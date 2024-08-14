import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True

    # Define necessary actions for initial setup
    required_measurements = {25, 27, 38, 16}

    def initial_measurements():
        for action in required_measurements:
            if action not in actions_taken:
                return action
        return None

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        initial_action = initial_measurements()
        if initial_action is not None:
            take_action(initial_action)
            continue

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Handle emergencies:
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(23)  # ResumeCPR
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(29)  # UseBagValveMask
            continue

        # Check and stabilize:
        # Airway
        if events[3] == 0:
            take_action(3)  # ExamineAirway
            continue

        if any(events[i] > 0 for i in [4, 5, 6]):
            take_action(31)  # UseYankeurSuctionCatheter or PerformHeadTiltChinLift
            continue

        # Breathing
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if events[7] > 0:
            take_action(29)  # UseBagValveMask
            continue

        # Circulation
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Check heart rhythm:
        take_action(2)  # CheckRhythm
        continue

    take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()