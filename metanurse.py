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

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_clear:
        print(3)  # ExamineAirway
        if events[3] > 0:
            airway_clear = True
        continue

    if not breathing_checked and airway_clear:
        print(4)  # ExamineBreathing
        if (
            events[10] > 0
            or events[11] > 0
            or events[12] > 0
            or events[13] > 0
            or events[14] > 0
        ):
            breathing_checked = True
        continue

    if not circulation_checked and breathing_checked:
        print(5)  # ExamineCirculation
        if (
            events[16] > 0.3 or events[17] > 0.3
        ):  # RadialPulsePalpable or RadialPulseNonPalpable
            circulation_checked = True
        continue

    if not disability_checked and circulation_checked:
        print(6)  # ExamineDisability
        if (
            events[21] > 0 or events[22] > 0 or events[23] > 0 or events[24] > 0
        ):  # Pupils or AVPU
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

    if measured_times[1] > 0 and measured_values[1] < 8:
        print(29)  # UseBagValveMask
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