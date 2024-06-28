while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Examine Airway if not recently done or airway problem observed
    if events[3] < 0.5 or events[4] > 0.5 or events[5] > 0.5 or events[6] > 0.5:
        print(3)  # ExamineAirway
        continue
    if events[1] > 0.5 or events[2] > 0.5:
        print(35)  # PerformAirwayManoeuvres
        continue

    # Check Airway Devices
    if events[6] > 0.5:
        print(32)  # UseGuedelAirway
        continue
    if events[4] > 0.5 or events[5] > 0.5:
        print(31)  # UseYankeurSuctionCatheter
        continue

    # Ensuring adequate breathing
    if measured_times[5] <= 0 or (measured_times[5] > 0 and measured_values[5] < 88):
        print(25)  # UseSatsProbe
        continue
    if events[7] > 0.5:
        print(29)  # UseBagValveMask
        continue

    # Ensuring adequate circulation
    if measured_times[0] <= 0:
        print(27)  # UseBloodPressureCuff
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check consciousness and neurological status (Disability)
    if events[25] > 0.5 or events[26] > 0.5:
        print(6)  # ExamineDisability
        continue

    # Exposure - check for any other signs or symptoms
    if events[27] > 0.5 or events[26] > 0.5:
        print(7)  # ExamineExposure
        continue

    # Regular monitoring using monitor and further assessments
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Condition to finish the simulation if patient is stabilized
    if (events[3] > 0.5 and
        measured_times[5] > 0 and measured_values[5] >= 88 and
        measured_times[6] > 0 and measured_values[6] >= 8 and
        measured_times[4] > 0 and measured_values[4] >= 60):
        print(48)  # Finish
        break

    # In situations where none of the above actions are necessary
    print(16)  # ViewMonitor