loop_counter = 0

while True:
    # Break condition to avoid infinite loops and to obey the contest rules
    if loop_i > 350:
        print(48)  # Finish to avoid technical failure
        break

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

    # Check airway status
    if not events[3]:  # AirwayClear not observed or relevant
        print(3)  # ExamineAirway
        continue

    # Breathing assessment and interventions
    if events[7]:  # BreathingNone observed
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation interventions
    if not events[16]:  # RadialPulsePalpable not observed
        print(5)  # ExamineCirculation
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Disability and Exposure evaluation
    if measured_times[6] > 0 and measured_values[6] >= 8 and events[21]:  # AVPU_U observed
        print(6)  # ExamineDisability
        continue
    if measured_times[6] > 0 and measured_values[6] >= 8 and events[22]:  # AVPU_V observed
        print(6)  # ExamineDisability
        continue
    print(7)  # ExamineExposure just to ensure no missed evaluations

    # Stabilization check
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        # All conditions for stabilization met
        print(48)  # Finish
        break

    # Regular monitoring
    print(16)  # ViewMonitor

    # Update the loop counter
    loop_counter += 1