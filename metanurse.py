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

    # Update Vital Signs if data not recent or taken
    if measured_times[5] == 0 or measured_times[6] == 0 or measured_times[4] == 0:
        print(16)  # ViewMonitor
        continue

    # Check the 'No Breathing' condition
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Check if the patient is stabilized
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

    # Examine Airway if no relevant airway issues observed
    if all(events[i] == 0 for i in range(3, 7)):
        print(3)  # ExamineAirway
        continue
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(32)  # UseGuedelAirway
        continue

    # Examine Breathing if no significant breathing observations
    if all(events[i] == 0 for i in range(7, 15)):
        print(4)  # ExamineBreathing
        continue

    # Examine Circulation if no pulse info
    if events[16] == 0 and events[17] == 0:
        print(5)  # ExamineCirculation
        continue

    # Examine Disability if no AVPU info
    if all(events[i] == 0 for i in range(21, 24)):
        print(6)  # ExamineDisability
        continue

    # Examine Exposure if no relevant exposure observations
    if all(events[i] == 0 for i in range(26, 28)):
        print(7)  # ExamineExposure
        continue

    # Actions based on low oxygen saturation
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Actions based on very low breathing rate
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Actions based on low mean arterial pressure
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    print(0)  # DoNothing if nothing else is required