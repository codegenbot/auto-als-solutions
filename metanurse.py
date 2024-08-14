import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = {25, 27, 24}

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)
    
    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def check_vitals(vitals):
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            return 23  # ResumeCPR
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            return 23  # ResumeCPR
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            return 15  # GiveFluids
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            return 30  # UseNonRebreatherMask
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            return 29  # UseBagValveMask
        return None

    def check_events(events):
        if any(events[i] > 0 for i in [4, 5]):  # Vomit, Blood
            return 31  # UseYankeurSucionCatheter
        if events[6] > 0:  # Tongue
            return 36  # PerformHeadTiltChinLift
        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):  # Breathing issues
            return 29  # UseBagValveMask
        if any(events[i] > 0 for i in range(1, 4)):  # Response issues
            return 8  # ExamineResponse
        if events[17] > 0:  # RadialPulseNonPalpable
            return 27  # UseBloodPressureCuff
        if any(events[i] > 0 for i in [31, 32, 33, 34, 35, 36, 37, 38, 39]):  # Unstable Tachyarrhythmias
            return 24  # UseMonitorPads

        # Trigger events not occurring spontaneously
        if 4 not in actions_taken:
            return 3  # ExamineAirway
        if 5 not in actions_taken:
            return 4  # ExamineBreathing
        if 6 not in actions_taken:
            return 5  # ExamineCirculation
        if 7 not in actions_taken:
            return 6  # ExamineDisability
        if 8 not in actions_taken:
            return 7  # ExamineExposure

        return None

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if needs_measurements():
            take_action(next_measurement_action())
            continue

        action = check_vitals(vitals)
        if action is not None:
            take_action(action)
            continue

        action = check_events(events)
        if action is not None:
            take_action(action)
            continue

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()