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

    def need_measurements():
        return (
            25 not in actions_taken
            or 27 not in actions_taken
            or 16 not in actions_taken
            or 3 not in actions_taken
            or 4 not in actions_taken
            or 5 not in actions_taken
            or 6 not in actions_taken
        )

    def need_measurement_action():
        if 25 not in actions_taken:
            return 25
        if 27 not in actions_taken:
            return 27
        if 16 not in actions_taken:
            return 16
        if 3 not in actions_taken:
            return 3
        if 4 not in actions_taken:
            return 4
        if 5 not in actions_taken:
            return 5
        if 6 not in actions_taken:
            return 6
        return None

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        if need_measurements():
            measurement_action = need_measurement_action()
            if measurement_action is not None:
                take_action(measurement_action)
                continue

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # BagDuringCPR
            continue

        if any([events[3] <= 0, events[11] > 0, events[5] > 0, events[6] > 0]):
            if events[4] > 0:  # AirwayVomit
                take_action(31)  # UseYankeurSuctionCatheter
                continue
            if events[5] > 0:  # AirwayBlood
                take_action(32)  # UseGuedelAirway
                continue
            if events[6] > 0:  # AirwayTongue
                take_action(36)  # PerformHeadTiltChinLift
                continue
            else:
                take_action(3)  # ExamineAirway
                continue

        if any([events[7] > 0, events[8] > 0, events[9] > 0, events[10] > 0]):
            if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
                take_action(29)  # UseBagValveMask
                continue
            if vitals["Sats"] is not None and vitals["Sats"] < 88:
                take_action(30)  # UseNonRebreatherMask
                continue
            take_action(4)  # ExamineBreathing
            continue

        if any([events[16] > 0, events[17] > 0, events[18] > 0]):
            if vitals["MAP"] is not None and vitals["MAP"] < 60:
                take_action(15)  # GiveFluids
                continue
            take_action(5)  # ExamineCirculation
            continue

        if any([events[20] > 0, events[21] > 0, events[22] > 0]):
            take_action(6)  # ExamineDisability
            continue

        if any([events[25] > 0, events[26] > 0, events[27] > 0]):
            take_action(7)  # ExamineExposure
            continue

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()