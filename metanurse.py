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

    # Airway assessment and intervention
    if events[1] > 0.5 or events[2] > 0.5 or events[4] > 0.5 or events[5] > 0.5 or events[6] > 0.5:
        if events[6] > 0.5:  # AirwayTongue
            print(32)  # UseGuedelAirway
        else:
            print(35)  # PerformAirwayManoeuvres
        continue
    elif events[3] < 0.5:  # AirwayClear not recently confirmed
        print(3)  # ExamineAirway
        continue

    # Breathing assessment and interventions
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    elif measured_times[5] > 0 and measured_values[5] < 88:  # MeasuredSats
        print(30)  # UseNonRebreatherMask
        continue
    elif measured_times[6] > 0 and measured_values[6] < 8:  # MeasuredResps
        print(29)  # UseBagValveMask
        continue

    # Circulation assessment and interventions
    if events[17] > 0.5:  # RadialPulseNonPalpable
        print(15)  # GiveFluids
        continue
    elif measured_times[0] > 0 and measured_values[0] < 60:  # HeartRate
        print(5)  # ExamineCirculation
        continue

    # Disability assessment
    if events[21:25] == [0] * 4:  # PupilsNormal to unresponsive
        print(6)  # ExamineDisability
        continue

    # Exposure
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue

    # Regular monitoring, needs revisiting for signs of life or rhythm
    if events[0] < 0.5:  # ResponseVerbal
        print(8)  # ExamineResponse
        continue

    # Stabilization check (Finishing the assessment)
    if (
        events[3] > 0.5  # AirwayClear
        and measured_times[5] > 0
        and measured_values[5] >= 88  # Sats at least 88
        and measured_times[6] > 0
        and measured_values[6] >= 8  # Resp Rate at least 8
        and measured_times[4] > 0
        and measured_values[4] >= 60  # MAP at least 60
    ):
        print(48)  # Finish
        break

    # View Monitor if nothing else to do
    print(16)  # ViewMonitor