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
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Check if sats and MAP are being measured, otherwise prompt measurement
    if measured_times[5] <= 0:
        print(25)  # UseSatsProbe
        continue
    if measured_times[4] <= 0:
        print(27)  # UseAline, if there's no arterial line consider blood pressure cuff
        continue

    # Airway assessment and interventions
    if not airway_confirmed:
        if events[3] > 0:  # AirwayClear is confirmed
            airway_confirmed = True
        elif events[4] > 0.1 or events[5] > 0.1:  # AirwayVomit or AirwayBlood
            print(31)  # UseYankeurSuctionCatheter
            continue
        elif events[6] > 0.1:  # AirwayTongue
            print(32)  # UseGuedelAirway
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
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Circulation assessment
    if measured_times[0] > 0 and measured_values[0] < 60:
        print(15)  # GiveFluids
        continue
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Disability assessment
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
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
        # All conditions for stabilization met
        print(48)  # Finish
        break

    # Regular monitoring if no critical condition to address
    print(16)  # ViewMonitor