import sys

ACTIONS = {
    "DoNothing": 0,
    "StartChestCompression": 17,
    "UseBloodPressureCuff": 27,
    "UseSatsProbe": 25,
    "ExamineAirway": 3,
    "ExamineBreathing": 4,
    "ExamineCirculation": 5,
    "ExamineDisability": 6,
    "ExamineExposure": 7,
    "ExamineResponse": 8,
    "UseYankeurSuctionCatheter": 31,
    "UseGuedelAirway": 32,
    "UseBagValveMask": 29,
    "UseNonRebreatherMask": 30,
    "GiveFluids": 15,
    "GiveAdenosine": 9,
    "UseMonitorPads": 24,
    "Finish": 48,
}


def stabilize():
    def take_action(action):
        print(ACTIONS[action])
        sys.stdout.flush()

    actions_taken = set()
    first_checks = ["UseBloodPressureCuff", "UseSatsProbe"]

    for step in range(350):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action("DoNothing")
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

        if (vitals["Sats"] and vitals["Sats"] < 65) or (
            vitals["MAP"] and vitals["MAP"] < 20
        ):
            take_action("StartChestCompression")
            continue

        for check in first_checks:
            if check not in actions_taken:
                actions_taken.add(check)
                take_action(check)
                break
        else:
            if any(events[i] > 0 for i in range(3, 7)):  # Airway events
                take_action("ExamineAirway")
                continue
            if events[5] > 0:  # AirwayVomit
                take_action("UseYankeurSuctionCatheter")
                continue
            if events[6] > 0:  # AirwayTongue
                take_action("UseGuedelAirway")
                continue

            if any(events[i] > 0 for i in range(7, 15)):  # Breathing events
                take_action("ExamineBreathing")
                continue
            if events[7] > 0:  # BreathingNone
                take_action("UseBagValveMask")
                continue
            if events[14] > 0:  # BreathingPneumothoraxSymptoms
                take_action("ExamineBreathing")
                continue

            if vitals["Sats"] and vitals["Sats"] < 88:
                take_action("UseNonRebreatherMask")
                continue

            if vitals["RR"] and vitals["RR"] < 8:
                take_action("UseBagValveMask")
                continue

            if vitals["MAP"] and vitals["MAP"] < 60:
                take_action("GiveFluids")
                continue

            if vitals["HR"] and vitals["HR"] > 150:
                take_action("GiveAdenosine")
                continue

            if any(events[i] > 0 for i in range(15, 20)):  # Circulation events
                take_action("ExamineCirculation")
                continue

            if any(events[i] > 0 for i in range(20, 26)):  # Disability events
                take_action("ExamineDisability")
                continue

            if any(events[i] > 0 for i in range(26, 33)):  # Exposure events
                take_action("ExamineExposure")
                continue

            take_action("Finish")
            break


if __name__ == "__main__":
    stabilize()