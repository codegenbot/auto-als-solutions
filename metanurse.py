import sys


def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    # Actions to be taken initially to gather critical measurements
    initial_actions = [25, 27, 16]  # UseSatsProbe, UseBloodPressureCuff, ViewMonitor
    initial_actions_taken = 0

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

        # Cardiac arrest conditions
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # StartChestCompression
            continue

        # Check Airway
        if not any(events[i] > 0 for i in range(3, 7)):  # No recent airway check events
            take_action(3)  # ExamineAirway
            continue
        # Check Breathing
        if (
            not any(events[i] > 0 for i in range(7, 15)) and initial_actions_taken >= 3
        ):  # No recent breathing check events and initial actions completed
            take_action(4)  # ExamineBreathing
            continue
        # Check Circulation
        if (
            not any(events[i] > 0 for i in range(15, 20)) and initial_actions_taken >= 3
        ):  # No recent circulation check events and initial actions completed
            take_action(5)  # ExamineCirculation
            continue
        # Check Disability
        if (
            not any(events[i] > 0 for i in range(20, 26)) and initial_actions_taken >= 3
        ):  # No recent disability check events and initial actions completed
            take_action(6)  # ExamineDisability
            continue
        # Check Exposure
        if (
            not any(events[i] > 0 for i in range(26, 33)) and initial_actions_taken >= 3
        ):  # No recent exposure check events and initial actions completed
            take_action(7)  # ExamineExposure
            continue

        # Address vitals
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["HR"] is not None and (vitals["HR"] > 150 or vitals["HR"] < 60):
            take_action(24)  # UseMonitorPads
            continue

        if initial_actions_taken < 3:
            take_action(initial_actions[initial_actions_taken])
            initial_actions_taken += 1
            continue

        take_action(48)  # Finish
        break


if __name__ == "__main__":
    stabilize()