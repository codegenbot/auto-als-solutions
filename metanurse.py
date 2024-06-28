airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-saving interventions
    pulse_status = events[16] > 0.5 or events[17] > 0.5
    if (
        (measured_times[5] > 0 and measured_values[5] < 65)
        or (measured_times[4] > 0 and measured_values[4] < 20)
        or not pulse_status
    ):
        print(17)  # StartChestCompression
        continue

    # Airway assessment and interventions
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        elif events[5] > 0.5 or events[6] > 0.5 or events[4] > 0.5:  # Obstructions
            print(31)  # UseYankeurSuctionCatheter
            continue
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing assessment and interventions
    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        print(25)  # UseSatsProbe
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Circulation assessment
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if not circulation_checked and (events[16] == 0 and events[17] > 0.5):
        print(5)  # ExamineCirculation
        continue
    circulation_checked = True

    # Disability assessment
    if not disability_checked:
        if events[21] > 0.5 or events[22] > 0.5 or events[23] > 0.5:  # AVPU status
            disability_checked = True
        else:
            print(6)  # ExamineDisability
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