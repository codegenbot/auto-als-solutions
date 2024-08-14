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

    def ensure_action_taken(action):
        if action not in actions_taken:
            take_action(action)
            return True
        return False

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )

        vitals = {
            name: value if vital_signs_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                     "MAP", "Sats", "Resps"], vital_signs_values
                )
            )
        }

        # Action priorities for ABCDE
        if ensure_action_taken(25):  # UseSatsProbe
            continue
        if ensure_action_taken(27):  # UseBloodPressureCuff
            continue
        if ensure_action_taken(16):  # ViewMonitor
            continue

        if ensure_action_taken(3):  # ExamineAirway
            continue
        if ensure_action_taken(4):  # ExamineBreathing
            continue
        if ensure_action_taken(5):  # ExamineCirculation
            continue
        if ensure_action_taken(6):  # ExamineDisability
            continue
        if ensure_action_taken(7):  # ExamineExposure
            continue

        # Check if any vital signs are missing
        if vitals["MAP"] is None and ensure_action_taken(38):  # TakeBloodPressure
            continue
        if vitals["RespRate"] is None and ensure_action_taken(4):  # ExamineBreathing
            continue
        if vitals["Sats"] is None and ensure_action_taken(16):  # ViewMonitor
            continue

        # Immediate interventions for critical conditions
        if vitals["MAP"] and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
            continue

        if vitals["Sats"] and vitals["Sats"] < 65:
            take_action(22)  # BagDuringCPR
            continue

        # Stabilization for deficient parameters
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RespRate"] and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Check end condition
        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]],
                [88, 8, 60]
            )
        ):
            take_action(48)  # Finish
            return

        take_action(48)  # Fail-safe Finish

if __name__ == "__main__":
    stabilize()