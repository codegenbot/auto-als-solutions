step = 0

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate concerns: Airway, Breathing, Circulation
    if events[2] > 0:  # ResponseNone indicates serious issue
        print(3)  # ExamineAirway
        continue

    # Checking critical conditions that require immediate action
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
        continue

    # Airway management
    if events[4] > 0 or events[3] > 0:  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSuctionCatheter
        continue

    # If no breathing observed
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Use monitor if vital checks are needed
    if step % 5 == 0 and (
        measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0
    ):
        print(16)  # ViewMonitor
        continue

    # Circulation: Give fluids if blood pressure is low but not critical
    if measured_times[4] > 0 and measured_values[4] < 60 and measured_values[4] >= 20:
        print(15)  # GiveFluids
        continue

    # Oxygenation: Ensure appropriate oxygen level
    if measured_times[5] > 0 and measured_values[5] < 88 and measured_values[5] >= 65:
        print(30)  # UseNonRebreatherMask
        continue

    # Determine if the patient has been stabilized
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

    # Default action
    print(0)  # DoNothing

    step += 1  # Increment step counter
    if step >= 350:
        print(48)  # Force finish to avoid a technical failure
        break