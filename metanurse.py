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

    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear
            airway_confirmed = True
        elif events[4] > 0.5 or events[5] > 0.5 or events[6] > 0.5:  # AirwayVomit, AirwayBlood, AirwayTongue
            print(31)  # UseYankeurSuctionCatheter
            continue
        print(3)  # ExamineAirway
        continue
    
    if not breathing_assessed:
        if measured_times[5] > 0 and measured_values[5] >= 88:
            breathing_assessed = True
        elif measured_times[5] > 0 and measured_values[5] < 65:
            print(29)  # UseBagValveMask
            continue
        if not satsProbeUsed:
            print(25)  # UseSatsProbe
            satsProbeUsed = True
            continue
        print(4)  # ExamineBreathing
        continue

    if not circulation_checked:
        if measured_times[4] > 0 and measured_values[4] >= 60:
            circulation_checked = True
        elif measured_times[4] > 0 and measured_values[4] < 20:
            print(17)  # StartChestCompression
            continue
        print(5)  # ExamineCirculation
        continue
    
    if not disability_checked:
        if events[21] > 0.1 or events[22] > 0.1 or events[23] > 0.1:  # AVPU statuses
            disability_checked = True
        print(6)  # ExamineDisability
        continue

    if not exposure_checked:
        exposure_checked = True
        print(7)  # ExamineExposure
        continue

    initial_assessments_done = airway_confirmed and breathing_assessed and circulation_checked and disability_checked and exposure_checked
    
    if initial_assessments_done:
        if all([
            measured_times[5] > 0 and measured_values[5] >= 88,  # Sats >= 88%
            measured_times[6] > 0 and measured_values[6] >= 8,  # Resp Rate >= 8
            measured_times[4] > 0 and measured_values[4] >= 60  # MAP >= 60mmHg
        ]):
            print(48)  # Finish
            break

    print(0)  # DoNothing as last resort