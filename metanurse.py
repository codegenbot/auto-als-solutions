airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
exposure_checked = False
initial_assessments_done = False
sats_probe_used = False
breathing_drawer_opened = False
steps = 0

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Check if patient needs immediate actions (Sats, MAP critical)
    if (measured_times[5] > 0 and measured_values[5] < 65) or (measured_times[4] > 0 and measured_values[4] < 20):
        print(17)  # StartChestCompression
        continue

    # Rescue breathing if needed
    if not breathing_assessed or events[7] >= 0.7 or (measured_times[6] > 0 and measured_values[6] < 8):
        print(29)  # UseBagValveMask
        breathing_assessed = True
        continue

    # ABCDE assessment sequence
    if not initial_assessments_done:
        if not airway_confirmed:
            if events[3] > 0:  # AirwayClear
                airway_confirmed = True
            else:
                print(3)  # ExamineAirway
                continue
        if not breathing_assessed:
            print(4)  # ExamineBreathing
            continue
        if not circulation_checked:
            print(5)  # ExamineCirculation
            continue
        if not disability_checked:
            print(6)  # ExamineDisability
            continue
        if not exposure_checked:
            print(7)  # ExamineExposure
            exposure_checked = True
        initial_assessments_done = True

    # Measurement check and stabilization efforts
    if not sats_probe_used:
        if not breathing_drawer_opened:
            print(19)  # OpenBreathingDrawer
            breathing_drawer_opened = True
        else:
            print(25)  # UseSatsProbe
            sats probes_used = True
        continue

    if measured_times[4] == 0 or measured_values[4] < 60:
        print(27)  # UseBloodPressureCuff
        continue

    # Condition for stabilizing John has been met
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

    print(0)  # DoNothing as a fallback action