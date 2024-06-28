step = 0

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check if need to intervene immediately for life-threatening conditions
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue

    # Airway examination should be done if response is none or airway clear is not recent
    if events[2] > 0:  # ResponseNone
        print(3)  # ExamineAirway
        continue

    # If airway complications like vomit or blood
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSuctionCatheter
        continue

    # Check breathing issues
    if events[7] > 0.1:  # BreathingNone
        if events[16] < 0.1:  # RadialPulsePalpable is not recent or not palpable
            print(17)  # StartChestCompression
        else:
            print(29)  # UseBagValveMask
        continue

    # Monitor and stabilize circulation specifics frequently
    if step % 5 == 0:
        print(27)  # UseBloodPressureCuff
        continue
    if step % 5 == 1:
        print(25)  # UseSatsProbe
        continue

    # Circulation responses, offer fluids if pressure is just below normal but not critical
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Oxygenation interventions
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Ensure all stabilization thresholds are met before finishing
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

    # If nothing urgent, repeat monitoring and measurements
    if step % 10 == 0:
        print(16)  # ViewMonitor
    else:
        print(0)  # DoNothing

    step += 1
    if step >= 350:
        print(48)  # Finish to avoid a technical failure
        break