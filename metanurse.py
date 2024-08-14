import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = {25, 27, 16, 24}

    def needs_measurements():
        return not required_measurements.issubset(actions_taken)
    
    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def has_unstable_tachyarrhythmia(events):
        arrhythmia_events = [28, 29, 30, 31, 32, 33, 34, 35, 36, 37]
        return any(events[i] > 0 for i in arrhythmia_events)
    
    def assess_and_treat(vitals, events):
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(23)  # Perform CPR
            return

        if needs_measurements():
            take_action(next_measurement_action())
            return

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if has_unstable_tachyarrhythmia(events):
                if 24 not in actions_taken:
                    take_action(24)  # UseMonitorPads
                elif 40 not in actions_taken:
                    take_action(40)  # DefibrillatorCharge
                elif 47 not in actions_taken:
                    take_action(47)  # DefibrillatorSync
                else:
                    take_action(40)  # DefibrillatorCharge again for cardioversion
            else:
                take_action(15)  # GiveFluids
            return

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            return

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            return

        if events[7] > 0:
            take_action(36)  # PerformHeadTiltChinLift
            return

        if any(events[i] > 0 for i in range(1, 4)):
            take_action(8)  # ExamineResponse
            return
        
        if any(events[i] > 0 for i in [5, 6]):
            take_action(31)  # UseYankeurSuctionCatheter
            return

        take_action(48)  # Finish

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        
        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        assess_and_treat(vitals, events)

if __name__ == "__main__":
    stabilize()