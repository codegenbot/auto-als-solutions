while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # A - Airway assessment and intervention
    if events[3] < 0.5:  # AirwayClear has low relevance
        print(3)  # ExamineAirway
        continue
    if events[4] > 0.5:  # AirwayVomit
        print(31)  # UseYankeurSucionCatheter
        continue

    # B - Breathing assessment and intervention
    if measured_times[6] > 0 and measured_values[6] < 8:  # Respiratory rate low
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:  # Oxygen saturation low
        print(30)  # UseNonRebreatherMask
        continue
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # C - Circulation assessment and intervention
    if measured_times[4] > 0 and measured_values[4] < 60:  # Mean Arterial Pressure low
        print(15)  # GiveFluids
        continue

    # D - Disability assessment and intervention
    if events[22] > 0.5 or events[21] > 0.5:  # AVPU_V or AVPU_U
        print(6)  # ExamineDisability
        continue

    # E - Exposure
    if events[26] > 0.5:  # ExposurePeripherallyShutdown
        print(7)  # ExamineExposure
        continue

    # Regular checks (if no critical condition, improve monitoring)
    # Check breathing and circulation if not done already
    if events[36] < 0.5: # RadialPulseNonPalpable
        print(5)  # ExamineCirculation
        continue

    if events[12] < 0.5:  # BreathingWheeze low relevance
        print(4)  # ExamineBreathing
        continue

    # Stabilization achieved
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

    # Default action if no other conditions met
    print(16)  # ViewMonitor