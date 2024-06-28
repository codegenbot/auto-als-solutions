loop_counter = 0

while True:
    if loop=counter >= 350:
        print(48)  # Finish
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
    if events[3] <= 0.5:  # AirwayClear has low relevance
        print(3)  # ExamineAirway
        continue
    elif events[4] > 0.5 or events[5] > 0.5:  # AirwayVomit or AirwayBlood
        print(18)  # OpenAirwayDrawer
        print(31)  # UseYankeurSucionCatheter
        continue
        
    # Breathing assessment and interventions
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Circulation interventions
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
        # All conditions for stabilization met
        print(48)  # Finish
        break

    # Regular monitoring
    print(16)  # ViewMonitor

    # Update the loop counter
    loop_counter += 1