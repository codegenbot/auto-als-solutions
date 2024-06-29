airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False

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

    # Examine airway if not confirmed or problematic signs detected
    if not airway_confirmed or events[4] > 0.5 or events[5] > 0.5 or events[6] > 0.5:
        airway_confirmed = events[3] > 0.5  # AirwayClear
        if not airway_confirmed:
            print(3)  # ExamineAirway
            continue
        else:
            print(32)  # UseGuedelAirway if need to keep airway open
            continue

    # Breathing and oxygen status
    need_oxygen = measured_times[5] > 0 and measured_values[5] < 88
    need_ventilation = measured_times[6] > 0 and measured_values[6] < 8
    if need_oxygen:
        print(30)  # UseNonRebreatherMask
        continue
    if need_ventilation:
        print(29)  # UseBagValveMask
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Circulation
    if not circulation_checked or measured_times[4] > 0 and measured_values[4] < 60:
        if not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue
        else:
            print(15)  # GiveFluids
            continue

    # Disability assessment and management
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # If stable, end scenario
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
        is_stable = (
            measured_times[5] > 0
            and measured_values[5] >= 88
            and measured_times[6] > 0
            and measured_values[6] >= 8
            and measured_times[4] > 0
            and measured_values[4] >= 60
        )
        if is_stable:
            print(48)  # Finish
            break
        # else check for additional interventions
        else:
            print(16)  # ViewMonitor to reassess if missing some info
            continue
    else:
        print(16)  # ViewMonitor if nothing else being done