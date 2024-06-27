import sys


def main():
    # Use sys.stdin.readline for faster input reading
    input = sys.stdin.readline

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

    # Continue processing until the process is terminated by the system or a FINISH command
    while True:
        data = input().strip()
        if not data:
            break  # Terminate the loop if no input is available, it's the end of data stream

        # Split the input data and transform them into float
        data = data.split()
        event_relevance = list(map(float, data[:39]))
        measured_relevance = list(map(float, data[39:46]))
        measurements = list(map(float, data[46:]))

        # Check patient's vitals and decide on actions
        if measured_relevance[MEASURED_MAP] > 0 and measurements[MEASURED_MAP] < 20:
            print(
                FINISH
            )  # Patient in critical condition, might simulate immediate intervention
            break
        elif measured_relevance[MEASURED_SATS] == 0:
            print(USE_SATS_PROBE)
        elif measured_relevance[MEASURED_SATS] > 0 and measurements[MEASURED_SATS] < 65:
            print(FINISH)  # Critical condition requiring immediate action
            break
        elif measured_relevance[MEASURED_SATS] > 0 and measurements[MEASURED_SATS] < 88:
            print(USE_NON_REBREATHER_MASK)
        elif measured_relevance[MEASURED_RESPS] == 0:
            print(EXAMINE_BREATHING)
        elif (
            measured_relevance[MEASURED_RESPS] > 0 and measurements[MEASURED_RESPS] < 8
        ):
            print(USE_NON_REBREATHER_MASK)
        elif measured_relevance[MEASURED_MAP] == 0:
            print(USE_BLOOD_PRESSURE_CUFF)
        elif measured_relevance[MEASURED_MAP] > 0 and measurements[MEASURED_MAP] < 60:
            print(EXAMINE_CIRCULATION)
        else:
            print(
                FINISH
            )  # If no critical actions are needed, attempt to finish the scenario.
            break


if __name__ == "__main__":
    main()