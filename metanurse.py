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

    # Check for airway obstruction issues
    if (
        events[3] < 0.1 and events[4] < 0.1 and events[5] < 0.1 and events[6] < 0.1
    ):  # None of AirwayClear, Vomit, Blood, Tongue have relevant data
        print(3)  # ExamineAirway
        continue

    # Handle airway problems
    if events[5] > 0.1:  # AirwayTongue
        print(32)  # UseGuedelAirway
        continue
    if events[4] > 0.1 or events[5] > 0.1:  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSuccionCatheter
        continue

    # Assess breathing based on examination
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # If measurements are extremely outdated or haven't been taken
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        if measured_times[5] == 0:
            print(25)  # UseSatsProbe
        elif measured_times[4] == 0:
            print(27)  # UseBloodPressureCuff
        print(16)  # ViewMonitor
        continue

    # Actions based on low oxygen saturation
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Actions based on very low breathing rate
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Actions based on low mean arterial pressure
    if measured_times[4] > 0 and measured_values[4] < 60:
        if measured_values[4] < 50:
            print(14)  # UseVenflonIVCatheter
            print(15)  # GiveFluids
            continue
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

    # Fallback to nothing if all conditions are stable or unsure
    print(0)  # DoNothing