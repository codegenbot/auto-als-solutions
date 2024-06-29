airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False
steps = 0

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical conditions check
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway check
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue
    elif events[4] > 0.1 or events[5] > 0.1:  # Vomit or Blood in Airway
        print(31)  # UseYankeurSucionCatheter
        continue
    elif events[6] > 0.1:  # Airway Obstructed by Tongue
        print(32)  # UseGuedelAirway
        continue

    # Breathing check
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        continue
    elif events[7] > 0.1:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Circulation check
    if not circulation_checked:
        print(5)  # ExamineCirculation
        continue
    elif events[16] < 0.1 and events[17] > 0.1:  # No palpable radial pulse
        print(14)  # UseVenflonIVCatheter
        print(15)  # GiveFluids
        continue

    # Disability check
    if not disability_checked:
        print(6)  # ExamineDisability
        continue

    # Stabilization conditions
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

    print(0)  # DoNothing as default if no other conditions apply.
    steps += 1
    if steps >= 350:
        print(48)  # Finish
        break