airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
bpCuffUsed = False
steps = 0

while steps < 350:
    steps += 1
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

    # Check airway
    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] > 0:  # AirwayClear
            airway_confirmed = True
        continue

    # Check breathing
    if not breathing_assessed and airway_confirmed:
        print(4)  # ExamineBreathing
        if any(events[i] > 0 for i in range(7, 15)):  # any breathing related events
            breathing_assessed = True
        continue

    # Check circulation
    if not circulation_checked and breathing_assessed:
        print(5)  # ExamineCirculation
        if any(events[i] > 0 for i in (16, 17, 18, 19)):  # circulation related events
            circulation_checked = True
        continue

    # Check disability
    if not disability_checked and circulation_checked:
        print(6)  # ExamineDisability
        if events[21] > 0 or events[22] > 0 or events[23] > 0:  # AVPU responses
            disability_checked = True
        continue

    # Exposure
    if not exposure_checked and disability_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        initial_assessments_done = True
        continue

    # Use Sats Probe if not used
    if not satsProbeUsed and initial_assessments_done:
        print(25)  # UseSatsProbe
        satsProbeUsed = True
        continue

    # Ensure adequate oxygen saturation
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Ensure Blood pressure is measured
    if not bpCuffUsed and initial_assessments_done:
        print(27)  # UseBloodPressureCuff
        bpCuffUsed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        if not events[27]:  # not palpitating hypotension
            print(15)  # GiveFluids
        continue

    # Check for stabilization condition
    if (
        initial_assessments_done
        and measured_times[4] > 0
        and measured_values[4] >= 60
        and measured_times[5] > 0
        and measured_values[5] >= 88
    ):
        print(48)  # Finish
        break

    print(0)  # DoNothing as default action if no specific action can be determined