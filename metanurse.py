import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    
    def take_action(action):
        actions_taken.add(action)
        print(action)
        sys.stdout.flush()
    
    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {
            name: value if time > 0 else None
            for value, time, name in zip(
                vital_signs_values,
                vital_signs_times,
                [
                    "HeartRate",
                    "RespRate",
                    "CapillaryGlucose",
                    "Temperature",
                    "MAP",
                    "Sats",
                    "Resps"
                ]
            )
        }

        # Perform ABCDE assessment to gather all necessary information
        if 25 not in actions_taken:
            take_action(25)  # UseSatsProbe
            continue
        if 27 not in actions_taken:
            take_action(27)  # UseBloodPressureCuff
            continue
        if 16 not in actions_taken:
            take_action(16)  # ViewMonitor
            continue
        if 3 not in actions_taken:
            take_action(3)   # ExamineAirway
            continue
        if 4 not in actions_taken:
            take_action(4)   # ExamineBreathing
            continue
        if 5 not in actions_taken:
            take_action(5)   # ExamineCirculation
            continue
        if 6 not in actions_taken:
            take_action(6)   # ExamineDisability
            continue
        if 7 not in actions_taken:
            take_action(7)   # ExamineExposure
            continue

        # Handle critical conditions first
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # BagDuringCPR
            continue

        unstable_tachyarrhythmia = events[29] > 0 or events[30] > 0 or events[31] > 0
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)  # AttachDefibPads
                continue
            take_action(40)      # DefibrillatorCharge
            continue

        # Stabilization actions for vitals
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Check if patient is stable
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60]
            )
        ):
            take_action(48)  # Finish
            return

        # Default action to finish if all conditions met
        take_action(48)
        return

if __name__ == "__main__":
    stabilize()