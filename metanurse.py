airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
steps = 0

while steps < 350:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate critical conditions handling
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # First, ensure Airway is checked
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            steps += 1
            continue

    # Next, check Breathing
    if not breathing_assessed:
        if events[7] > 0.5:  # BreathingNone has high relevance
            print(29)  # UseBagValveMask
        elif measured_times[5] > 0 and measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
        elif measured_times[6] > 0 and measured_values[6] < 8:
            print(29)  # UseBagValveMask
        else:
            print(4)  # ExamineBreathing
        steps += 1
        breathing_assessed = True
        continue

    # Then check Circulation
    if not circulation_checked:
        if measured_times[4] > 0 and measured_values[4] < 60:
            print(15)  # GiveFluids
        else:
            print(5)  # ExamineCirculation
        steps += 1
        circulation_checked = True
        continue

    # Check Disability
    if not disability_checked:
        if (
            events[22] > 0.5 or events[23] > 0.5
        ):  # Check AVPU Unresponsive or other negative signs
            print(6)  # ExamineDisability
        steps += 1
        disability_checked = True
        continue

    # Regular monitoring and remaining examinations
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
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
        else:
            print(16)  # ViewMonitor

    steps += 1

# Should only reach here if there is no proper conclusion
print(
    48
)  # Finish as a safety protocol to avoid infinite loop if the protocol above fails