airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
emergency_intervention_performed = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if not emergency_intervention_performed and ((measured_times[5] > 0 and measured_values[5] < 65) or
       (measured_times[4] > 0 and measured_values[4] < 20)):
        print(17)  # StartChestCompression
        emergency_intervention_performed = True
        continue

    if not airway_confirmed and events[3] > 0.7:  # AirwayClear
        airway_confirmed = True
        
    if not airway_confirmed:
        print(3)  # ExamineAirway
        continue

    if not breathing_assessed and (events[7] > 0.7 or events[11] > 0.7):  # Severe breathing issues
        print(29)  # UseBagValveMask
        breathing_assessed = True
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

    if measured_times[4] == 0:
        print(27)  # UseBloodPressureCuff
        continue
    elif measured_times[5] == 0:
        print(25)  # UseSatsProbe
        continue
    else:
        print(16)  # ViewMonitor
        continue

    if airway_confirmed and breathing_assessed and circulation_checked and disability_checked:
        if (measured_times[5] > 0 and measured_values[5] >= 88 and measured_times[6] > 0 and measured_values[6] >= 8 and 
            measured_times[4] > 0 and measured_values[4] >= 60):
            print(48)  # Finish
            break
        else:
            print(16)  # ViewMonitor