airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
saturation_checked = False
blood_pressure_checked = False

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

    # Check and stabilize airway
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Check and assist breathing
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Check and support circulation
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check disability status
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Check oxygen saturation with probe
    if not saturation_checked:
        print(25)  # UseSatsProbe
        print(16)  # ViewMonitor
        saturation_checked = True
        continue

    # Check blood pressure regularly
    if not blood_pressure_checked:
        print(27)  # UseBloodPressureCuff
        print(16)  # ViewWolfMonitor
        blood_pressure_checked = True
        continue

    # Check for stabilization
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

    # If no critical condition to address, monitor regularly
    print(16)  # ViewMonitor