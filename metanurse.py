import sys

def stabilize():
    max_steps = 350
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True

    actions_taken = set()
    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        # Ensure initial vital observations
        if 25 not in actions_taken:
            take_action(25)
            continue
        if 27 not in actions_taken:
            take_action(27)
            continue
        if 16 not in actions_taken:
            take_action(16)
            continue
        if 3 not in actions_taken:
            take_action(3)
            continue

        # Extract current vital signs
        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Check for cardiac arrest conditions
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or \
           (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(23)  # Resume CPR
            continue

        # Treat low MAP
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Treat low oxygen saturation
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        # Treat low respiratory rate
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # Suction airway for vomit or blood
        if events[4] > 0 or events[5] > 0:
            take_action(31)  # UseYankeurSuctionCatheter
            continue

        # Perform airway maneuver if tongue obstruction
        if events[6] > 0:
            take_action(36)  # PerformHeadTiltChinLift
            continue

        # Provide ventilation support if abnormal breathing events occur
        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(29)  # UseBagValveMask
            continue

        # Handle heart rhythm abnormalities
        if any(events[i] > 0 for i in [28, 29, 32]):
            if 28 not in actions_taken:
                take_action(28)  # AttachDefibPads
            elif 40 not in actions_taken:
                take_action(40)  # DefibrillatorCharge
            elif 24 not in actions_taken:
                take_action(24)  # UseMonitorPads
            continue

        # Administer medication if required by heart rhythm
        if any(events[i] > 0 for i in range(30, 32)):
            take_action(9)  # GiveAdenosine
            continue

        # Finalize
        take_action(48)

if __name__ == "__main__":
    stabilize()