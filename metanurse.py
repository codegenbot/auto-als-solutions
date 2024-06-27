import sys


def main():
    input = sys.stdin.read
    # Constants for indices
    MEASURED_MAP = 4
    MEASURED_SATS = 5
    MEASURED_RESPS = 6

    # Constants for action codes
    FINISH = 48
    EXAMINE_AIRWAY = 3
    EXAMINE_BREATHING = 4
    EXAMINE_CIRCULATION = 5
    USE_NON_REBREATHER_MASK = 30
    USE_BLOOD_PRESSURE_CUFF = 27
    USE_SATS_PROBE = 25

    try:
        while True:
            data = input().split()
            if not data:
                break

            event_relevance = list(map(float, data[:39]))
            measured_relevance = list(map(float, data[39:46]))
            measurements = list(map(float, data[46:]))

            if measured_relevance[MEASURED_MAP] > 0 and measurements[MEASURED_MAP] < 20:
                print(FINISH)
                break
            elif measured_relevance[MEASURED_SATS] == 0:
                print(USE_SATS_PROBE)
            elif (
                measured_relevance[MEASURED_SATS] > 0
                and measurements[MEASURED_SATS] < 65
            ):
                print(FINISH)
                break
            elif (
                measured_relevance[MEASURED_SATS] > 0
                and measurements[MEASURED_SATS] < 88
            ):
                print(USE_NON_REBREATHER_MASK)
            elif measured_relevance[MEASURED_RESPS] == 0:
                print(EXAMINE_BREATHING)
            elif (
                measured_relevance[MEASURED_RESPS] > 0
                and measurements[MEASURED_RESPS] < 8
            ):
                print(USE_NON_REBREATHER_MASK)
            elif measured_relevance[MEASURED_MAP] == 0:
                print(USE_BLOOD_PRESSURE_CUFF)
            elif (
                measured_relevance[MEASURED_MAP] > 0 and measurements[MEASURED_MAP] < 60
            ):
                print(EXAMINE_CIRCULATION)
            else:
                print(FINISH)
                break
    except Exception as e:
        sys.stderr.write("Error encountered: " + str(e))
        sys.exit(1)


if __name__ == "__main__":
    main()