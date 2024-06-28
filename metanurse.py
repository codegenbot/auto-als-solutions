airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
saturation_checked = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions for critical conditions
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
    if not saturation_checked:
        print(25)  # UseSatsProbe
        saturation_checked = True
        continue

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
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Circulation assessment
    if not circulation_checked:
        print(27)  # UseBloodPressureCuff
        circulation_checked = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Checking ECG rhythm if circulation issues suspected
    if (
        events[18] > 0.5 or events[19] == 0
    ):  # Check if HeartSoundsMuffled or HeartSoundsNormal is not confirmed
        print(2)  # CheckRhythm
        continue

    # Disability assessment
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Regular monitoring if no critical condition to address immediately
    print(16)  # ViewMonitor