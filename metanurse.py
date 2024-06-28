airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
saturation_measured = False

while True:
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

    # AIRWAY
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        elif events[5] > 0.1 or events[6] > 0.1:  # Vomit or Blood
            print(31)  # UseYankeurSucionCatheter
            continue
        else:
            print(3)  # ExamineAirway
            continue

    # BREATHING
    if not breathing_assessed or (measured_times[5] > 0 and measured_values[5] < 88):
        if events[7] > 0.5:  # BreathingNone has high relevance
            print(29)  # UseBagValveMask
            continue
        if not saturation_measured:
            print(25)  # UseSatsProbe
            saturation_measured = True
            continue
        print(30)  # UseNonRebreatherMask
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # CIRCULATION
    if not circulation_checked:
        if events[17] > 0.5:  # RadialPulseNonPalpable
            print(5)  # ExamineCirculation
            circulation_checked = True
            continue
        if measured_times[4] > 0 and measured_values[4] < 60:
            print(15)  # GiveFluids
            continue
        circulation_checked = True

    # DISABILITY
    if not disability_checked:
        if (
            events[22] > 0.5 or events[23] > 0.5 or events[24] > 0.5
        ):  # Check AVPU_U, AVPU_V, AVPU_P
            print(6)  # ExamineDisability
            continue
        disability_checked = True

    # STABILIZATION CHECK
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88  # Sats at least 88
        and measured_times[6] > 0
        and measured_values[6] >= 8  # Resp Rate at least 8
        and measured_times[4] > 0
        and measured_values[4] >= 60  # MAP at least 60
    ):
        print(48)  # Finish
        break

    # If nothing critical, reassess with Monitor
    print(16)  # ViewMonitor