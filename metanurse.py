airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False

while True:
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
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    if measured_times[5] == 0:
        print(19)  # OpenBreathingDrawer
        print(25)  # UseSatsProbe
        print(16)  # ViewMonitor
        continue

    if measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[6] == 0 or measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if not circulation_checked:
        if events[17] > 0.5:  # RadialPulseNonPalpable
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue
        elif events[16] > 0.5:  # RadialPulsePalpable
            print(14)  # UseVenflonIVCatheter
            print(15)  # GiveFluids
            circulation_checked = True
            continue

    if not disability_checked:
        print(6)  # ExamineDisability
        if events[22] > 0.5 or events[21] > 0.5:  # AVPU_V or AVPU_U
            disability_checked = True
        continue

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

    print(16)  # ViewMonitor