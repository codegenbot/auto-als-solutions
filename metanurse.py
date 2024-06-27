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

    # Update Vital Signs frequently
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Check for any 'No Breathing' condition and start chest compressions immediately
    if events[7] > 0:  # BreathingNone
        print(17)  # StartChestCompression
        continue

    # Check for stabilized condition
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

    # Examine Airway if there's no detailed information on airway obstacles
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    # If there's vomit or blood obstructing airway, take immediate measures
    if events[4] > 0:  # AirwayVomit
        print(31)  # UseYankeurSucionCatheter
        continue
    if events[5] > 0:  # AirwayBlood
        print(32)  # UseGuedelAirway
        continue

    # Examine Breathing if there are no detailed observations
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

    # Examine Circulation if no pulse detected
    if events[16] == 0 and events[17] == 0:  # RadialPulse not palpable
        print(5)  # ExamineCirculation
        continue

    # Check Disability if no AVPU info present
    if events[21] == 0 and events[22] == 0 and events[23] == 0:  
        print(6)  # ExamineDisability
        continue

    # Check Exposure if no pertinent data to explain patient's state
    if events[26] == 0 and events[27] == 0:  
        print(7)  # ExamineExposure
        continue

    # Act based on low oxygen saturation
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Act based on very low breathing rate
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Act based on low mean arterial pressure
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    print(0)  # DoNothing if nothing else is required