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
        elif (
            events[4] > 0.1 or events[5] > 0.1 or events[6] > 0.1
        ):  # Vomit or Blood or Tongue
            print(31)  # UseYankeurSuctionCatheter
            continue
        elif events[7] > 0.5:  # BreathingNone high relevance
            print(17)  # StartChestCompression
            continue
        else:
            print(3)  # ExamineAirway
            continue

    # BREATHING
    if not breathing_assessed or measured_times[5] == 0:
        if measured_times[5] > 0 and measured_values[5] < 88:
            print(30)  # UseNonRebreatherMask
            continue
        if events[7] > 0.5:  # BreathingNone has high relevance
            print(29)  # UseBagValveMask
            continue
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # CIRCULATION
    if not circulation_checked:
        if (
            events[16] > 0.5 and events[17] > 0.5
        ):  # RadialPulseNonPalpable and palpable contradictory - double-check circulation
            print(5)  # ExamineCirculation
            continue
        if measured_times[4] > 0:
            if measured_values[4] < 60:
                print(15)  # GiveFluids
                continue
            circulation_checked = True
        else:
            print(27)  # UseBloodPressureCuff
            continue

    # CAPILLARY REFILL AND OTHER SIGNS
    print(
        28
    )  # AttachDefibPads - required more thorough analysis if capillary refill or other central signs are worse

    # DISABILITY
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

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