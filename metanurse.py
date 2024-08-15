import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    mandatory_actions = [27, 25, 38, 25]  # UseBloodPressureCuff, UseSatsProbe, TakeBloodPressure, UseSatsProbe
    examine_order = [3, 4, 5, 6, 7, 8]

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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["HR"] is not None and vitals["HR"] > 150:  # Tachyarrhythmia
            take_action(24)  # UseMonitorPads (for synchronized cardioversion)
            continue

        for action in mandatory_actions:
            if action not in actions_taken:
                actions_taken.add(action)
                take_action(action)
                break
        else:
            for exam in examine_order:
                if exam not in actions_taken:
                    actions_taken.add(exam)
                    take_action(exam)
                    break

        if any(events[i] > 0 for i in range(3, 7)):  # Airway events
            take_action(3)  # ExamineAirway
            continue

        if events[5] > 0:  # AirwayVomit
            take_action(31)  # UseYankeurSuctionCatheter
            continue
        if events[6] > 0:  # AirwayTongue
            take_action(32)  # UseGuedelAirway
            continue

        if any(events[i] > 0 for i in range(7, 15)):  # Breathing events
            take_action(4)  # ExamineBreathing
            continue
        if events[7] > 0:  # BreathingNone
            take_action(29)  # UseBagValveMask
            continue
        if events[14] > 0:  # BreathingPneumothoraxSymptoms
            take_action(19)  # OpenBreathingDrawer
            continue

        if any(events[i] > 0 for i in range(15, 20)):  # Circulation events
            take_action(5)  # ExamineCirculation
            continue

        if any(events[i] > 0 for i in range(20, 26)):  # Disability events
            take_action(6)  # ExamineDisability
            continue

        if any(events[i] > 0 for i in range(26, 33)):  # Exposure events
            take_action(7)  # ExamineExposure
            continue

        take_action(0)  # DoNothing

if __name__ == "__main__":
    stabilize()