step = 0

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Conditions for critical medical interventions:
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Steps between measurements, default actions if vital signs aren't measured
    if step % 10 == 0 and (
        measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0
    ):
        print(25)  # UseSatsProbe
        continue

    # Assess airway and breathing
    if events[2] > 0:  # ResponseNone - Check airway
        print(3)  # ExamineAirway
        continue
    if events[4] > 0 or events[3] > 0:  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSuctionCatheter
        continue
    if events[7] > 0.5:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Circulation checks and actions
    if measured_times[4] > 0 and measured_values[4] < 60 and measured_values[4] >= 20:
        print(15)  # GiveFluids
        continue

    # Ensuring sufficient oxygenation
    if measured_times[5] > 0 and measured_values[5] < 88 and measured_values[5] >= 65:
        print(30)  # UseNonRebreatherMask
        continue

    # End condition for stabilization
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

    # Assess other needs periodically
    if step % 5 == 0:
        print(16)  # ViewMonitor
    else:
        print(0)  # DoNothing

    step += 1  # Increment step counter
    if step >= 350:
        print(48)  # Output Finish to avoid a technical failure
        break