import sys


def parse_input():
    return list(map(float, sys.stdin.readline().strip().split()))


def main():
    steps = 0
    checked_airway = (
        checked_breathing
    ) = checked_circulation = checked_disability = False

    while steps < 350:
        observations = parse_input()
        event_relevances = observations[:33]
        vital_signs_relevances = observations[33:40]
        vital_signs_measurements = observations[40:]

        if vital_signs_measurements[5] < 65 or vital_signs_measurements[4] < 20:
            print(48)  # Finish due to cardiac arrest
            return

        # A - Airway
        if not checked_airway:
            if event_relevances[3] == 0:  # AirwayClear not observed
                print(36)  # PerformHeadTiltChinLift
            else:
                for i in [4, 5]:  # AirwayVomit, AirwayBlood
                    if event_relevances[i] > 0:
                        print(31)  # UseYankeurSucionCatheter
                        break
            checked_airway = True
            steps += 1
            continue

        # B - Breathing
        if not checked_breathing:
            if vital_signs_relevances[6] > 0 and vital_signs_measurements[6] < 8:
                print(29)  # UseBagValveMask
            elif vital_signs_relevances[5] > 0 and vital_signs_measurements[5] < 88:
                print(30)  # UseNonRebreatherMask
            checked_breathing = True
            steps += 1
            continue

        # C - Circulation
        if not checked_circulation:
            if vital_signs_relevances[4] > 0 and vital_signs_measurements[4] < 60:
                print(20)  # OpenCirculationDrawer
            checked_circulation = True
            steps += 1
            continue

        # D - Disability
        if not checked_disability:
            if (
                vital_signs_relevances[2] > 0 and vital_signs_measurements[2] < 4
            ):  # Hypoglycemia
                print(15)  # GiveFluids
            checked_disability = True
            steps += 1
            continue

        # Stabilization Check
        if all(vital_signs_measurements[i] >= [60, 88, 8][i] for i in range(3)):
            print(48)  # Finish
            return

        print(0)  # DoNothing if no action is required
        steps += 1


if __name__ == "__main__":
    main()