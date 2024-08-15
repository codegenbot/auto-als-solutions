import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = [24, 25, 27]  # MonitorPads, SatsProbe, BloodPressureCuff

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def needs_measurements():
        return not set(required_measurements).issubset(actions_taken)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
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

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # StartChestCompression
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if any(events[i] > 0 for i in [4, 5, 6]):
            take_action(3)  # ExamineAirway
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # UseYankeurSuctionCatheter
            elif events[6] > 0:
                take_action(32)  # UseGuedelAirway
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(4)  # ExamineBreathing
            if events[7] > 0:
                take_action(29)  # UseBagValveMask
            continue

        if any(events[i] > 0 for i in range(1, 4)):
            take_action(8)  # ExamineResponse
            continue

        cardiac_events = [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
        if any(events[i] > 0 for i in cardiac_events):
            take_action(24)  # UseMonitorPads
            continue

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()