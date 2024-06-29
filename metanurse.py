airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCuffUsed = False
steps = 0

while True:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    critical_sats = measured_times[5] > 0 and measured_values[5] < 65
    critical_map = measured_times[4] > 0 and measured_values[4] < 20
    low_resp = measured_times[6] > 0 and measured_values[6] < 8

    if critical_sats or critical_map:
        print(17)  # StartChestCompression
        continue

    if low_resp:
        print(29)  # UseBagValveMask
        continue

    if not initial_assessments_done:
        if not airway_confirmed:
            print(3)  # ExamineAirway
            if events[3] > 0.1:
                airway_confirmed = True
            continue

        if not breathing_assessed:
            print(4)  # ExamineBreathing
            if events[9] > 0:
                breathing_assessed = True
            continue

        if not circulation_checked:
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue

        if not disability_checked:
            print(6)  # ExamineDisability
            disability_checked = True
            continue

        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
            continue

        initial_assessments_done = True

    if not satsProbeUsed:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        if not bpCuffUsed:
            print(27)  # UseBloodPressureCuff
            print(16)  # ViewMonitor
            bpCuffUsed = True
        continue

    if (
        measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
    ):
        print(48)  # Finish
        break