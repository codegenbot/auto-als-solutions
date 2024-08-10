import sys


def parse_input():
    return list(map(float, sys.stdin.readline().strip().split()))


def main():
    steps = 0
    while steps < 350:
        observations = parse_input()
        event_relevances = observations[:33]
        vital_signs_relevances = observations[33:40]
        vital_signs_measurements = observations[40:]

        # Check for critical conditions
        if vital_signs_measurements[5] < 65 or vital_signs_measurements[4] < 20:
            print(48)  # Finish
            return

        # Ensure recent observations
        if vital_signs_relevances[4] == 0:  # MAP not measured
            print(27)  # UseBloodPressureCuff
            continue
        if vital_signs_relevances[6] == 0:  # Respiratory rate not measured
            print(16)  # ViewMonitor
            continue
        if vital_signs_relevances[5] == 0:  # Sats not measured
            print(25)  # UseSatsProbe
            continue

        # ABCDE Assessment and Stabilization
        if not any(event_relevances[i] > 0 for i in [3, 4, 5]):  # Airway clear
            print(36)  # PerformHeadTiltChinLift or 37 PerformJawThrust
        elif vital_signs_measurements[6] < 8:  # Breathing insufficient
            print(29)  # UseBagValveMask or 30 UseNonRebreatherMask
        elif vital_signs_measurements[4] < 60:  # Circulation insufficient (MAP)
            print(20)  # OpenCirculationDrawer or 16 ViewMonitor
        elif vital_signs_measurements[5] < 88:  # Circulation insufficient (Sats)
            print(30)  # UseNonRebreatherMask
        elif not any(event_relevances[i] > 0 for i in range(3)):  # Response issues
            print(8)  # ExamineResponse or 6 ExamineDisability
        elif not any(event_relevances[i] > 0 for i in range(26, 33)):  # Exposure issues
            print(7)  # ExamineExposure
        else:
            # Check for stabilization and take appropriate actions
            if all(vital_signs_measurements[i] >= [60, 88, 8][i] for i in range(3)):
                print(48)  # Finish if stabilized
            else:
                print(0)  # DoNothing

        steps += 1


if __name__ == "__main__":
    main()