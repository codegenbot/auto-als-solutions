airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
satsProbeUsed = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Start Chest Compressions if critical conditions are met
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Prioritize airway assessment
    if not airway_confirmed:
        print(3)  # ExamineAirway
        if events[3] >= 0.5:  # AirwayClear
            airway_confirmed = True
        continue

    # Use Bag-Valve Mask if no breathing
    if events[7] > 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        continue

    # Breathing assessment
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True  # Assume it's done for simplification
        continue

    # Use Sats Probe
    if not satsProbeUsed:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        print(16)  # ViewMonitor
        satsProbeUsed = True
        continue

    # Check Circulation
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Check Disability
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Check Exposure
    if not exposure_checked:
        print(7)  # ExamineExposure
        exposure_checked = True
        continue

    # Check finish conditions
    if initial_assessments_done:
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

    # Periodically review patient status
    print(16)  # ViewMonitor