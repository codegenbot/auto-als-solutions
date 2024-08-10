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

        # Actively seek vital signs if not recently measured
        if vital_signs_relevances[4] == 0:  # MeasuredMAP
            print(27)  # UseBloodPressureCuff
        elif vital_signs_relevances[5] == 0:  # MeasuredSats
            print(25)  # UseSatsProbe
        elif vital_signs_relevances[6] == 0:  # MeasuredResps
            print(4)  # ExamineBreathing
        else:
            # ABCDE Assessment and Stabilization
            if not any(event_relevances[i] > 0 for i in [3, 4, 5]):  # Airway clear
                if vital_signs_measurements[6] < 8:  # Breathing issues
                    print(29)  # UseBagValveMask
                elif (
                    vital_signs_measurements[4] < 60 or vital_signs_measurements[5] < 88
                ):  # Circulation issues
                    if vital_signs_measurements[4] < 60:
                        print(20)  # OpenCirculationDrawer
                    else:
                        print(30)  # UseNonRebreatherMask
                else:
                    print(48)  # Finish if stabilized
            else:
                print(3)  # ExamineAirway

        steps += 1


if __name__ == "__main__":
    main()