import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()

    reassess_countdown = 5  # Cycle through all assessments every 5 steps

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Cardiac arrest condition
        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # StartChestCompression
            continue

        # Actions to ensure airway is managed
        if events[3] > 0 and "exam_airway" not in actions_taken:
            take_action(3)  # ExamineAirway
            actions_taken.add("exam_airway")
            continue
        if events[4] > 0:
            take_action(31)  # UseYankeurSucionCatheter
            continue
        if events[6] > 0:
            take_action(32)  # UseGuedelAirway
            continue

        # Start examination cycles over each reassess_countdown steps
        reassess_countdown -= 1
        if reassess_countdown <= 0:
            take_action(3)  # ExamineAirway
            continue

        # Check vitals: measured priorities (MAP, Sats first)
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        # Ensure essential equipment is attached
        if 27 not in actions_taken:
            take_action(27)  # UseBloodPressureCuff
            actions_taken.add(27)
            continue
        if 25 not in actions_taken:
            take_action(25)  # UseSatsProbe
            actions_taken.add(25)
            continue
        if 24 not in actions_taken:
            take_action(24)  # UseMonitorPads
            actions_taken.add(24)
            continue
        if 26 not in actions_taken:
            take_action(26)  # UseAline
            actions_taken.add(26)
            continue

        # Perform a full ABCDE cycle
        if reassess_countdown == 0:
            take_action(3)  # ExamineAirway
            take_action(4)  # ExamineBreathing
            take_action(5)  # ExamineCirculation
            take_action(6)  # ExamineDisability
            take_action(7)  # ExamineExposure
            reassess_countdown = 5
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()