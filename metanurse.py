airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
emergency_handled = False
steps = 0


def check_critical_conditions(measured_values, measured_times):
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        return (True, 17)  # StartChestCompression
    return (False, 0)  # No emergency


def check_stabilization(measured_values, measured_times):
    return (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    )


def execute(action):
    print(action)


while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Handle emergencies immediately
    emergency_status, emergency_action = check_critical_conditions(
        measured_values, measured_times
    )
    if emergency_status:
        execute(emergency_action)
        emergency_handled = True
        continue

    # ABCDE assessment
    if not airway_confirmed:
        execute(3)  # ExamineAirway
        if events[3] > 0.1 or events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1:
            airway_confirmed = True
        continue

    if airway_confirmed and not breathing_assessed:
        execute(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    if airway_confirmed and breathing_assessed and not circulation_checked:
        execute(5)  # ExamineCirculation
        circulation_checked = True
        continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and not disability_checked
    ):
        execute(6)  # ExamineDisability
        if events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1:
            disability_checked = True
        continue

    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and not exposure_checked
    ):
        execute(7)  # ExamineExposure
        exposure_checked = True
        continue

    # If John is not stable, apply appropriate treatments
    if not check_stabilization(measured_values, measured_times):
        if measured_times[5] == 0 or measured_values[5] < 88:
            execute(30)  # UseNonRebreatherMask
        elif measured_times[4] == 0 or measured_values[4] < 60:
            execute(15)  # GiveFluids
        else:
            execute(16)  # ViewMonitor
        continue

    # If all checks are done and John is stabilized
    if check_stabilization(measured_values, measured_times):
        execute(48)  # Finish
        break

    execute(0)  # DoNothing as a fallback, should not typically reach here