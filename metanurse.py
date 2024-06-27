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

    # Ensure basic measurements are available
    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue
    if measured_times[4] == 0 or measured_times[6] == 0:
        print(27)  # UseBloodPressureCuff
        continue
    if measured_times[6] == 0:
        print(16)  # ViewMonitor
        continue

    # A - Airway Assessment and Management
    if events[7:11].count(0) == len(events[7:11]):  # No airway assessment yet
        print(3)  # ExamineAirway
        continue
    if events[6] > 0:  # Airway needs clearing
        print(36)  # PerformHeadTiltChinLift
        continue

    # B - Breathing Management
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue
    if measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # C - Circulation Management
    if (
        events[16] > 0.5 and measured_values[4] < 60
    ):  # RadialPulseNonPalpable and low MAP
        print(15)  # GiveFluids
        continue

    # D - Disability Assessment
    if (
        events[21] > 0.5 or events[22] > 0.5
    ):  # AVPU_U or AVPU_V (less responsive states)
        print(6)  # ExamineDisability
        continue

    # Check if the patient is stabilized
    if (
        events[3] > 0
        and measured_values[5] >= 88
        and measured_values[6] >= 8
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Regularly check overall conditions
    print(16)  # ViewMonitor