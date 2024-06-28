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

    # Airway assessment and interventions
    if events[3] > 0.5:  # AirwayClear is confirmed recently
        pass  # Airway is clear, check next steps.
    elif (
        events[1] > 0.5
        or events[2] > 0.5
        or events[4] > 0.5
        or events[5] > 0.5
        or events[6] > 0.5
    ):  # Airway problems
        print(35)  # PerformAirwayManoeuvres
        continue
    else:
        print(3)  # ExamineAirway
        continue

    # Breathing assessment and interventions
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    elif measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    elif measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    print(4)  # ExamineBreathing if no clear action determined yet
    
    # Circulation assessment
    if measured_times[4] > 0:
        if measured_values[4] < 60:
            print(15)  # GiveFluids
            continue
        elif measured_values[4] >= 60 and events[16] < 0.5 and events[17] < 0.5:
            print(5)  # ExamineCirculation to check pulses and heart rate
            continue

    # Disability assessment
    if events[21:25] == [0, 0, 0, 0]:  # No AVPU response observed
        print(6)  # ExamineDisability
        continue

    # Exposure
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue

    # Stabilization check
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

    # If no specific action has been decided yet
    print(16)  # ViewMonitor to get updates on patient's condition