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
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if not breathing_assessed:
        # Regular monitoring and recheck after intervention if needed
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Circulation assessment
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Checking rhythm problems or maintained very high heart rates
    if events[30] > 0:  # Detect AFib or other serious rhythms
        print(2)  # CheckRhythm
        continue

    # Disability assessment
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Ensure all measurements are up to date
    if measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue

    # Stabilization check
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88  # Sats at least 88
        and measured_times[6] > 0
        and measured_values[6] >= 8  # Resp Rate at least 8
        and measured_times[4] > 0
        and measured_values[4] >= 60  # MAP at least 60
    ):
        # All conditions for stabilization met
        print(48)  # Finish
        break

    # If all vital parameters are rechecked and stabilized, keep monitoring until recovery
    print(16)  # ViewMonitor