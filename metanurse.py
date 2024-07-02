steps = 0
airway_confirmed, breathing_assessed, circulation_checked = False, False, False
disability_checked, exposure_checked = False, False
sats_assessed, bp_assessed = False, False

while steps < 350:
    steps += 1

    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        if events[3] > 0:  # AirwayClear event
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    if airway_confirmed and not breathing_assessed:
        if events[7] > 0:  # BreathingNone
            print(29)  # UseBagValveMask
            continue
        else:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue

    if breathing_assessed and not circulation_checked:
        if events[16] == 0:  # RadialPulseNonPalpable
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

    if not sats_assessed and measured_times[5] == 0:
        print(25)  # UseSatsProbe
        sats_assessed = True
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if not bp_assessed and measured_times[4] == 0:
        print(27)  # UseBloodPressureCuff
        bp_assessed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

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

    print(0)  # DoNothing