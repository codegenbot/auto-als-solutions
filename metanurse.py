while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediately critical conditions for cardiac arrest
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Airway assessment and management
    if events[3] == 0 or events[4] > 0 or events[5] > 0 or events[6] > 0:  # Check if airway is clear
        print(3)  # ExamineAirway
        continue
    elif events[7] > 0:  # BreathingNone has positive signal
        print(29)  # UseBagValveMask
        continue
    elif events[6] > 0.1:  # AirwayTongue obstruction detected
        print(32)  # UseGuedelAirway
        continue

    # Breathing checks and interventions
    if measured_times[5] == 0 or (measured_times[5] > 0 and measured_values[5] < 88):
        print(30)  # UseNonRebreatherMask
        continue

    # Circulation checks
    if measured_times[4] == 0 or (measured_times[4] > 0 and measured_values[4] < 60):
        print(15)  # GiveFluids
        continue

    # Disability (Neurologic) evaluation
    if events[21] > 0 or events[22] > 0 or events[23] > 0:  # Check if AVPU non-alert
        print(6)  # ExamineDisability
        continue

    # Ensure proper measurements of vital signs
    if measured_times[5] == 0:  # Sats not recently measured
        print(25)  # UseSatsProbe
        continue
    if measured_times[4] == 0:  # MAP not recently measured
        print(27)  # UseBloodPressureCuff
        continue

    # Check conditions for completing the scenario
    if (measured_values[5] >= 88 and measured_values[6] >= 8 and measured_values[4] >= 60):
        print(48)  # Finish
        break

    # View Monitor as a general action if no specific action is applicable
    print(16)  # ViewMonitor