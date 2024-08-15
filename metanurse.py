import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    initial_measurements = [24, 25, 27, 26]

    def take_action(action):
        print(action)
        sys.stdout.flush()
        actions_taken.add(action)

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

        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # StartChestCompression
            take_action(23)  # ResumeCPR
            continue

        if needs_initial_measurements():
            take_action(next_initial_measurement_action())
            continue

        if any(events[i] > 0 for i in range(3, 7)):
            take_action(3)  # ExamineAirway
            if events[5] > 0:
                take_action(31)  # UseYankeurSuctionCatheter
            if events[6] > 0:
                take_action(32)  # UseGuedelAirway
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue
        if any(events[i] > 0 for i in range(7, 15)):
            take_action(4)  # ExamineBreathing
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            if vitals["MAP"] is not None and vitals["MAP"] < 60:
                take_action(10)  # GiveAdrenaline for inotropic support
            continue
        if any(events[i] > 0 for i in range(15, 20)):
            take_action(5)  # ExamineCirculation
            continue

        if any(events[i] > 0 for i in range(20, 26)):
            take_action(6)  # ExamineDisability
            continue

        if any(events[i] > 0 for i in range(26, 33)):
            take_action(7)  # ExamineExposure
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()