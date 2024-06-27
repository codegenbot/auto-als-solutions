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

    # Immediate action to open airway
    if events[6]:  # AirwayTongue
        print(32)  # UseGuedelAirway
        continue
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSuctionCatheter
        continue

    # Check for any 'No Breathing' condition
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        break

    # Act based on low oxygen saturation
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Examine Airway
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    # Examine Breathing
    if (
        events[7] == 0
        and events[8] == 0
        and events[9] == 0
        and events[10] == 0
        and events[11] == 0
        and events[12] == 0
        and events[13] == 0
        and events[14] == 0
    ):
        print(4)  # ExamineBreathing
        continue

    # Examine Circulation
    if events[16] == 0 and events[17] == 0:  # No pulse info
        print(5)  # ExamineCirculation
        continue

    # Examine Disability
    if events[21] == 0 and events[22] == 0 and events[23] == 0:  # No AVPU info
        print(6)  # ExamineDisability
        continue

    # Examine Exposure
    if events[26] == 0 and events[27] == 0:  # No exposure info
        print(7)  # ExamineExposure
        continue

    # View Monitor if necessary to gather missing vital signs
    if any(measurement == 0 for measurement in measured_times[:6]):
        print(16)  # ViewMonitor
        continue

    # Act based on very low breathing rate
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Act based on low mean arterial pressure
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check for stabilized condition
    stabilized = (
        events[2] > 0  # ResponseNone indicating clear airway
        and measured_times[5] > 0
        and measured_values[5] >= 88  # Sats >= 88%
        and measured_times[6] > 0
        and measured_values[6] >= 8  # Resp Rate >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60  # MAP >= 60
    )
    if stabilized:
        print(48)  # Finish
        break

    print(0)  # DoNothing if nothing else is required