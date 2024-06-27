import sys

input = sys.stdin.read

while True:
    try:
        data = input().strip().split()
        if not data:
            break

        # Extract measurements and their relevances
        event_relevance = list(map(float, data[:39]))
        measured_relevance = list(map(float, data[39:46]))
        measurements = list(map(float, data[46:]))

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

        # Check patient's vitals and decide on actions
        if measured_relevance[MEASURED_MAP] > 0 and measurements[MEASURED_MAP] < 20:
            print(
                FINISH
            )  # Patient in critical condition, might simulate immediate intervention
        elif measured_relevance[MEASURED_SATS] == 0:
            print(USE_SATS_PROBE)
        elif measured_relevance[MEASURED_SATS] > 0 and measurements[MEASURED_SATS] < 65:
            print(FINISH)  # Critical condition requiring immediate action
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
    except EOFError:
        break