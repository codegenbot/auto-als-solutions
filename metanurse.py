import sys

ACTIONS = {
    "DoNothing": 0,
    "CheckSignsOfLife": 1,
    "CheckRhythm": 2,
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
    "UseMonitorPads": 24,
    "StartChestCompression": 17,
    "UseSatsProbe": 25,
    "UseBloodPressureCuff": 27,
    "Finish": 48
}

def stabilize():
    def take_action(action):
        print(ACTIONS[action])
        sys.stdout.flush()

    first_checks = ["UseSatsProbe", "UseBloodPressureCuff"]
    examine_order = ["ExamineAirway", "ExamineBreathing", "ExamineCirculation", "ExamineDisability", "ExamineExposure"]

    actions_taken = set()

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

        if (vitals["Sats"] and vitals["Sats"] < 65) or (vitals["MAP"] and vitals["MAP"] < 20):
            take_action("StartChestCompression")
            continue

        for check in first_checks:
            if check not in actions_taken:
                actions_taken.add(check)
                take_action(check)
                break

        if vitals["Sats"] is None or vitals["MAP"] is None:
            continue

        if vitals["Sats"] < 88:
            take_action("UseNonRebreatherMask")
            continue

        if vitals["RR"] and vitals["RR"] < 8:
            take_action("UseBagValveMask")
            continue

        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action("GiveFluids")
            continue

        for exam in examine_order:
            if exam not in actions_taken:
                actions_taken.add(exam)
                take_action(exam)
                break

        if any(events[i] > 0 for i in range(3, 7)):  # Airway events
            take_action("ExamineAirway")
            continue
        if events[5] > 0:  # AirwayVomit
            take_action("UseYankeurSuctionCatheter")
            continue
        if events[6] > 0:  # AirwayTongue
            take_action("UseGuedelAirway")
            continue
        if events[7] > 0:  # BreathingNone
            take_action("UseBagValveMask")
            continue

        take_action("Finish")
        break

if __name__ == "__main__":
    stabilize()