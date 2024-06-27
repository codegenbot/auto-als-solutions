while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate actions based on critical life-threatening conditions
    if measured_times[5] > 0 and measured_values[5] < 65:
        print(17)  # StartChestCompression
        continue
    if measured_times[4] > 0 and measured_values[4] < 20:
        print(17)  # StartChestCompression
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

    # Base level diagnostics if measurements are completely missing
    if measured_times[5] == 0:  # Sats
        print(25)  # UseSatsProbe
        continue
    if measured_times[4] == 0:  # MAP
        print(27)  # UseBloodPressureCuff
        continue
    if measured_times[6] == 0:  # Resps
        print(26)  # UseAline (assumingly they meant Respiratory Rate here)
        continue

    # Immediate care based on current vital sign measurements
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # If no specific action is required based on vitals, prioritize examining unknowns
    if all(events[3:7]) == 0:  # No airway info
        print(3)  # ExamineAirway
        continue
    if all(events[7:15]) == 0:  # No breathing info
        print(4)  # ExamineBreathing
        continue
    if events[16] == 0 and events[17] == 0:  # No circulation info
        print(5)  # ExamineCirculation
        continue
    if events[21] == 0 and events[22] == 0 and events[23] == 0:  # No Disability info
        print(6)  # ExamineDisability
        continue
    if events[26] == 0 and events[27] == 0:  # No exposure info
        print(7)  # ExamineExposure
        continue

    # Default no-action if nothing else is actionable
    print(0)  # DoNothing