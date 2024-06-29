airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
step_count = 0

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

    # Airway assessment and interventions
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing assessment and interventions
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    
    if measured_times[5] > 0:
        if measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if measured_values[5] >= 88:
            breathing_assessed = True

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        continue

    # Circulation assessment
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Disability assessment
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Stabilization check
    if (airway_confirmed and breathing_assessed and circulation_checked and disability_checked
        and measured_times[5] > 0 and measured_values[5] >= 88  # Sats at least 88%
        and measured_times[6] > 0 and measured_values[6] >= 8  # Resp rate at least 8
        and measured_times[4] > 0 and measured_values[4] >= 60):  # MAP at least 60
        print(48)  # Finish
        break

    # Regular monitoring if no critical condition to address
    if step_count % 5 == 0:
        print(16)  # ViewMonitor
    else:
        print(0)  # DoNothing

    step-Hcount += 1

    # to avoid an infinite loop if stuck in a nonproductive cycle
    if step_count >= 350:
        print(48)  # Finish
        break