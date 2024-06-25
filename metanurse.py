observations = input().strip().split()
observations = list(map(float, observations))

# Parsing inputs
events = observations[:39]  # All event observations
measured_timeliness = observations[39:46]  # Timeliness of measurement
measurements = observations[46:]  # Actual values of measurements

# Mapping indices for clearer understanding
AirwayClear, BreathingNone, MeasuredSats, MeasuredMAP, MeasuredResps = 3, 7, 45, 47, 46

# Critical conditions that require immediate action
if measured_timeliness[MeasuredSats - 39] > 0 and measurements[MeasuredSats - 46] < 65:
    print(17)  # StartChestCompression
elif measured_timeliness[MeasuredMAP - 39] > 0 and measurements[MeasuredMAP - 46] < 20:
    print(17)  # StartChestCompression

# Detailed Conditions Analysis and Action Plan
# Start with Examination if necessary measurements are not available or are insufficient
elif (
    measured_timeliness[MeasuredSats - 39] == 0
    or measured_timeliness[MeasuredMAP - 39] == 0
    or measured_timeliness[MeasuredResps - 39] == 0
):
    if events[AirwayClear] == 0:
        print(3)  # ExamineAirway
    elif events[BreathingNone] > 0:
        print(4)  # ExamineBreathing
    elif measurements[MeasuredMAP - 46] < 60:
        print(5)  # ExamineCirculation
    elif measurements[MeasuredSats - 46] < 88:
        if events[AirwayClear] > 0:
            print(30)  # UseNonRebreatherMask
        else:
            print(3)  # ExamineAirway
else:
    # All necessary parameters have been measured, evaluate for stabilization
    airway_okay = events[AirwayClear] > 0
    breathing_okay = (
        measurements[MeasuredResps - 46] >= 8 and measurements[MeasuredSats - 46] >= 88
    )
    circulation_okay = measurements[MeasuredMAP - 46] >= 60

    if airway_okay and breathing_okay and circulation_okay:
        print(48)  # Finish
    else:
        # Take corrective actions based on the issues found
        if not airway_okay:
            print(3)  # ExamineAirway
        elif not breathing_okay:
            print(29)  # UseBagValveMask
        elif not circulation_okay:
            print(15)  # GiveFluids