airway_clear = False
breathing_checked = False
circulation_checked = False
disability_checked = False
exposure_checked = False
satsProbeUsed = False
bpCuffUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().strip().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if events[7] > 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_clear:
        if events[3] > 0:  # AirwayClear
            airway_clear = True
        else:
            print(3)  # ExamineAirway
            continue

    if not breathing_checked and airway_clear:
        if events[7] > 0:  # BreathingNone
            print(29)  # UseBagValveMask
        elif events[10] > 0:  # EqualChestExpansion indicates okay breathing
            breathing_checked = True
        else:
            print(4)  # ExamineBreathing
            continue

    if not circulation_checked and breathing_checked:
        if events[16] > 0:  # RadialPulsePalpable
            circulation_checked = True
        else:
            print(5)  # ExamineCirculation
            continue

    if not disability_checked and circulation_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    if not exposure_checked and disability_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    if not satsProbeUsed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if not bpCuffUsed:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    if (
        airway_clear
        and breathing_checked
        and circulation_checked
        and disability_checked
        and exposure_checked
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

    print(0)  # DoNothing if no other actions applicable