airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
equipment_set_up = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions against cardiac arrest
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check and manage airway
    if not airway_confirmed:
        if events[3] > 0:  # AirwayClear is triggered
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Emergency breathing support
    if events[7] > 0:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Circulation interventions
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Assess disability
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Set up essential monitoring equipment if not done
    if not equipment_set_up:
        print(25)  # UseSatsProbe
        print(27)  # UseBloodPressureCuff
        equipment_set_up = True
        continue

    # Monitor contextually after interventions
    if equipment_set_up:
        print(16)  # ViewMonitor
        continue

    # Check if all parameters are stabilized
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Default action if no conditions are met
    print(0)  # DoNothing