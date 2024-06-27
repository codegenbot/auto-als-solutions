while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate actions based on critical conditions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Begin with constant monitoring if needed
    if measured_times[4] == 0:  # if MAP is outdated
        print(27)  # UseBloodPressureCuff
        continue
    if measured_times[5] == 0:  # if sats are outdated
        print(25)  # UseSatsProbe
        continue

    # Regular examinations to get more data
    if events[3:8] == [0]*5:  # if airway status is unknown
        print(3)  # ExamineAirway
        continue
    if events[8:15] == [0]*7:  # if breathing is not recently checked
        print(4)  # ExamineBreathing
        continue

    # Assess airway and manage obstructions
    if events[4] > 0:  # AirwayVomit
        print(31)  # UseYankeurSuctionCatheter
        continue
    if events[5] > 0:  # AirwayBlood
        print(31)  # UseYankeurSuctionCatheter
        continue

    # Assess and manage breathing
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Manage circulation issues
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check if the patient is stabilized
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Default to viewing monitor if no further cues on what to do
    print(16)  # ViewMonitor