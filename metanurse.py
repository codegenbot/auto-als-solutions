while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Assess airway first
    if events[2] > 0:  # ResponseNone
        print(3)  # ExamineAirway
        continue

    # Check critical conditions leading to cardiac arrest
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Check for airway blockages
    if events[4] > 0:  # AirwayVomit
        print(31)  # UseYankeurSuctionCatheter
        continue
    if events[5] > 0:  # AirwayBlood
        print(31)  # UseYankeurSuctionCatheter
        continue
    if events[6] > 0:  # AirwayTongue
        print(32)  # UseGuedelAirway
        continue

    # Ensure breathing
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Ensure circulation
    if measured_times[0] > 0 and (measured_values[0] < 60 or measured_values[0] > 100):
        print(15)  # GiveFluids
        continue

    # Disability examination
    if events[22] > 0:  # AVPU_U (unresponsive to voice)
        print(8)  # ExamineResponse
        continue

    # Exposure examination
    if events[26] > 0:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue

    # Re-checking vitals if not measured recently or adequately
    if all(mt == 0 for mt in measured_times):
        print(16)  # ViewMonitor
        continue
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Performing systematic rechecks
    if events[3] == 0:  # AirwayClear not checked
        print(3)  # ExamineAirway
        continue
    if events[11] == 0:  # Breathing issues not checked
        print(4)  # ExamineBreathing
        continue
    if events[16] == 0:  # Circulation not checked
        print(5)  # ExamineCirculation
        continue

    # If all conditions for finishing are met
    if (
        (measured_times[5] > 0 and measured_values[5] >= 88)
        and (measured_times[6] > 0 and measured_values[6] >= 8)
        and (measured_times[4] > 0 and measured_values[4] >= 60)
    ):
        print(48)  # Finish
        break

    # Default action if no other immediate action is required
    print(0)  # DoNothing