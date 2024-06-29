airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical immediate response
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway management and assessment
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear confirmed
            airway_confirmed = True
        elif events[4] > 0 or events[5] > 0 or events[6] > 0:
            print(31)  # UseYankeurSucionCatheter
            continue
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing assessments and interventions
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue

    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Circulation checks
    if events[17] > 0.5:  # RadialPulseNonPalpable
        print(15)  # GiveFluids
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    if events[18] > 0:  # HeartSoundsMuffled
        print(11)  # GiveAmiodarone
        continue

    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Disability checking
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Exposure assessment and response
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
    ):
        print(7)  # ExamineExposure
        continue

    # Stabilization check
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

    # Regular monitoring if no critical condition to address
    print(16)  # ViewMonitor