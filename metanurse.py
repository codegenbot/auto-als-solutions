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
            observations[40:],
        )

        if 3 not in actions_taken:
            take_action(3)  # ExamineAirway
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

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        unstable_tachyarrhythmia = any(events[i] > 0 for i in range(29, 32))
        if unstable_tachyarrhythmia:
            if 28 not in actions_taken:
                take_action(28)  # Attach defib pads
                continue
            take_action(40)  # DefibrillatorCharge
            continue

        if events[4] > 0 or events[5] > 0:
            take_action(31)  # UseYankeurSucionCatheter for vomit or blood
            continue

        if events[6] > 0:
            take_action(36)  # PerformHeadTiltChinLift for tongue obstruction
            continue

        if events[7] > 0:
            take_action(35)  # PerformAirwayManoeuvres for no breathing
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # Start chest compression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # Bag during CPR
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give fluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use nonrebreather mask
            continue

        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use bag valve mask
            continue

        take_action(48)  # Finish


if __name__ == "__main__":
    stabilize()