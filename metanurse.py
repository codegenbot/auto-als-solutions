while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving conditions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Immediate actions for no breathing
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Regular monitoring of vital signs
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Examine Airway if no information on airway state
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    # Management of Airway obstructions
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(32)  # UseGuedelAirway
        continue

    # Re-check Breathing conditions
    if sum(events[7:15]) == 0:
        print(4)  # ExamineBreathing
        continue

    # Check Circulation if no pulse information
    if events[16] == 0 and events[17] == 0:
        print(5)  # ExamineCirculation
        continue

    # Check Disability if no AVPU info
    if sum(events[21:24]) == 0:
        print(6)  # ExamineDisability
        continue

    # Examine Exposure if limited info
    if events[26] == 0 and events[27] == 0:
        print(7)  # ExamineExposure
        continue

    # Address low oxygenation if not critical but below normal
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Assist ventilation if respiratory rate is very low
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Treat hypotension
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Stabilization check
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

    # Default action if nothing else is required
    print(0) 