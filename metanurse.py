import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    initial_setup_actions = [24, 25, 27, 26, 18, 19, 20, 21] 

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

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # StartChestCompression
            take_action(23)  # ResumeCPR
            continue

        if any(action not in actions_taken for action in initial_setup_actions):
            for action in initial_setup_actions:
                if action not in actions_taken:
                    take_action(action)
                    break
            continue

        # Airway
        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # ExamineAirway
            if events[5] > 0:
                take_action(31)  # UseYankeurSuctionCatheter
            if events[6] > 0:
                take_action(32)  # UseGuedelAirway
            continue

        # Breathing
        if (vitals["Sats"] is not None and vitals["Sats"] < 88):
            take_action(30)  # UseNonRebreatherMask
            continue

        if (vitals["RR"] is not None and vitals["RR"] < 8):
            take_action(29)  # UseBagValveMask
            continue

        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # ExamineBreathing
            continue

        # Circulation
        if (vitals["MAP"] is not None and vitals["MAP"] < 60):
            take_action(15)  # GiveFluids
            continue

        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # ExamineCirculation
            continue

        # Disability
        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)  # ExamineDisability
            continue

        # Exposure
        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # ExamineExposure
            continue

        if (
            (vitals["MAP"] is not None and vitals["MAP"] >= 60) and
            (vitals["Sats"] is not None and vitals["Sats"] >= 88) and
            (vitals["RR"] is not None and vitals["RR"] >= 8)
        ):
            take_action(48)  # Finish
            break

if __name__ == "__main__":
    stabilize()