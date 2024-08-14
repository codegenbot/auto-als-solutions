import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)

    required_measurements = [25, 27, 16, 24]

    def next_measurement_action():
        for action in required_measurements:
            if action not in actions_taken:
                return action

    def has_unstable_tachyarrhythmia(events):
        arrhythmia_events = [31, 32, 33, 34, 36, 37]
        return any(events[i] > 0 for i in arrhythmia_events)
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        
        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if len(actions_taken) < len(required_measurements):
            take_action(next_measurement_action())
            continue

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(23)  # Perform CPR
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if has_unstable_tachyarrhythmia(events):
                if 24 not in actions_taken:
                    take_action(24)  # UseMonitorPads
                elif 40 not in actions_taken:
                    take_action(40)  # DefibrillatorCharge
                elif 47 not in actions_taken:
                    take_action(47)  # DefibrillatorSync
                else:
                    take_action(40)  # DefibrillatorCharge for cardioversion
            else:
                take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Airway assessment
        if events[3] == 0:  # Not clear airway
            take_action(3)  # ExamineAirway
            continue
    
        # Airway suction
        if events[7] > 0:
            take_action(36)  # PerformHeadTiltChinLift
            continue

        if any(events[i] > 0 for i in [5, 6]):  # Vomit or Blood in Airway
            take_action(31)  # UseYankeurSuctonCatheter
            continue

        # Check Response
        if any(events[i] > 0 for i in [1, 2]):
            take_action(8)  # ExamineResponse
            continue

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()