airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCuffUsed = False
monitorViewed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    vital_times = list(map(float, observations[39:46]))
    vital_values = list(map(float, observations[46:]))

    heart_rate = vital_values[0] if vital_times[0] > 0 else None
    resp_rate = vital_values[1] if vital_times[1] > 0 else None
    capillary_glucose = vital_values[2] if vital_times[2] > 0 else None
    temperature = vital_values[3] if vital_times[3] > 0 else None
    mean_arterial_pressure = vital_values[4] if vital_times[4] > 0 else None
    oxygen_saturation = vital_values[5] if vital_times[5] > 0 else None
    resps = vital_values[6] if vital_times[6] > 0 else None

    if oxygen_saturation is not None and oxygen_saturation < 65:
        print(17)  # StartChestCompression
        continue

    if mean_arterial_pressure is not None and mean_arterial_pressure < 20:
        print(17)  # StartChestCompression
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            airway_confirmed = True
            continue

        if not breathing_assessed and airway_confirmed:
            print(4)  # ExamineBreathing
            breathing_assessed = True
            continue

        if not circulation_checked and breathing_assessed:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

        if not disability_checked and circulation_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        if not exposure_checked and disability_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            initial_assessments_done = True
            continue

    if not satsProbeUsed and breathing_assessed:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if not monitorViewed and (satsProbeUsed or bpCuffUsed):
        print(16)  # ViewMonitor
        monitorViewed = True
        continue

    if oxygen_saturation is not None and oxygen_saturation < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if not bpCuffUsed and circulation_checked:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if resp_rate is not None and resp_rate < 8:
        print(29)  # UseBagValveMask
        continue

    if mean_arterial_pressure is not None and mean_arterial_pressure < 60:
        print(15)  # GiveFluids
        continue

    if (
        oxygen_saturation is not None
        and mean_arterial_pressure is not None
        and resp_rate is not None
    ):
        if oxygen_saturation >= 88 and mean_arterial_pressure >= 60 and resp_rate >= 8:
            print(48)  # Finish
            break

    print(0)  # DoNothing as a last resort