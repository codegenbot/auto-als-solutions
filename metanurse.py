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
                    [
                        "HeartRate",
                        "RespRate",
                        "CapillaryGlucose",
                        "Temperature",
                        "MAP",
                        "Sats",
                        "Resps"
                    ],
                    vital_signs_values
                )
            )
        }

        if 2 not in actions_taken:
            take_action(2)  # CheckRhythm
            continue

        if 3 not in actions_taken:
            take_action(3)  # ExamineAirway
            continue

        if 4 not in actions_taken:
            take_action(4)  # ExamineBreathing
            continue

        if 25 not in actions_taken:
            take_action(25)  # UseSatsProbe
            continue

        if 27 not in actions_taken:
            take_action(27)  # UseBloodPressureCuff
            continue

        if 16 not in actions_taken:
            take_action(16)  # ViewMonitor
            continue

        # Check for unstable arrhythmia that indicates cardioversion
        if any(events[idx] > 0 for idx in [31, 32, 36]):
            if 28 not in actions_taken:
                take_action(28)  # AttachDefibPads
                continue
            if 40 not in actions_taken:
                take_action(40)  # DefibrillatorCharge
                continue
            take_action(43)  # DefibrillatorPace
            continue

        # Check for immediate CPR needs
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # BagDuringCPR
            continue

        # Address hypotension
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Address low oxygen saturation
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        # Address low respiratory rate
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if all(
            vital is not None and vital >= threshold
            for vital, threshold in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            take_action(48)  # Finish
            return

        take_action(48)  # Finish (if steps exhausted)

if __name__ == "__main__":
    stabilize()