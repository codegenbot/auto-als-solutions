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

    if not events[3]:  # AirwayClear not confirmed
        print(3)  # ExamineAirway
        continue
    if events[5] > 0 or events[6] > 0:  # Airway obstruction like blood or tongue
        print(31)  # UseYankeurSucionCatheter
        continue

    if events[7]:  # BreathingNone has occurred
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if events[17]:  # RadialPulseNonPalpable
        print(15)  # GiveFluids
        continue
    if events[16] == 0:  # RadialPulsePalpable not confirmed
        print(5)  # ExamineCirculation
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check if disoriented or unconscious
    if not any(events[21:25]):  # AVPU responses are not observed
        print(6)  # ExamineDisability
        continue

    # Exposure - check for apparent problems
    if not events[25]:  # PupilsNormal not confirmed recently
        print(7)  # ExamineExposure
        continue

    # Stabilization check
    if (
        events[3] > 0.5
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break

    # Regular monitoring
    print(16)  # ViewMonitor