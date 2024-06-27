while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-threatening conditions
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # View Monitor if vital signs are never measured or outdated
    if 0 in measured_times[:3]:
        print(16)  # ViewMonitor
        continue

    # Examine airway if no airway problems have been noted yet
    if events[3] == 0 and events[4] == 0 and events[5] == 0 and events[6] == 0:
        print(3)  # ExamineAirway
        continue

    # Intervention for no breathing situation
    if events[7] > 0:  # BreathingNone
        print(29)  # UseBagValveMask
        continue

    # Check breathing issues and listen for lung sounds
    if all(e == 0 for e in events[8:15]):  # Breathing issues indices
        print(4)  # ExamineBreathing
        continue

    # Adjust to airway obstructions
    if events[4] > 0 or events[5] > 0:  # AirwayVomit or AirwayBlood
        print(31)  # UseYankeurSucionCatheter
        continue

    # Examine circulation if no pulse data
    if events[16] == 0 and events[17] == 0:
        print(5)  # ExamineCirculation
        continue

    # Handle low vessel perfusion or shocks
    if events[26] > 0 or events[27] > 0:  # ExposurePeripherallyShutdown
        print(15)  # GiveFluids
        continue

    # Examine disability - consciousness level
    if events[21] == 0 and events[22] == 0 and events[23] == 0:
        print(6)  # ExamineDisability
        continue

    # Non-invasive oxygen provision if saturation low
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue

    # Ventilatory support if respiratory rate is very low
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue

    # Fluid resuscitation if mean arterial pressure is low
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue

    # Check for steady stabilization
    if (
        measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # Otherwise, continue monitoring the patient
    print(0)  # DoNothing