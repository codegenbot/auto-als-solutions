airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
equipment_set = {"sats_probe": False, "bp_cuff": False, "monitor_pads": False}

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Immediate life-threatening conditions handling
    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    # Ensure proper equipment is deployed when measurements are potentially unreliable
    if not equipment_set["sats_probe"] and events[25] == 0:
        print(25)  # UseSatsProbe
        equipment_set["sats_probe"] = True
        continue
    if not equipment_set["bp_cuff"] and events[27] == 0:
        print(27)  # UseBloodPressureCuff
        equipment_set["bp_cuff"] = True
        continue

    # Check for airway problems
    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear is strongly indicated
            airway_confirmed = True
        else:
            print(3)  # ExamineAirway
            continue

    # Breathing interventions and assessments
    if events[7] > 0.5 or (
        measured_times[6] > 0 and measured_values[6] < 8
    ):  # BreathingNone has high relevance or low breath rate
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88:
        print(30)  # UseNonRebreatherMask
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    # Circulation assessments and interventions
    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    # Check disability
    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

    # Once all systems are checked and no immediate risks, stabilize and finish
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and measured_times[5] > 0
        and measured_values[5] >= 88
        and measured_times[6] > 0
        and measured_values[6] >= 8
        and measured_times[4] > 0
        and measured_values[4] >= 60
    ):
        print(48)  # Finish
        break

    # View monitor for updates only if all necessary measurements are set
    if (
        airway_confirmed
        and breathing_assessed
        and circulation_checked
        and disability_checked
        and equipment_set["sats_probe"]
        and equipment_set["bp_cuff"]
    ):
        print(16)  # ViewMonitor
    else:
        print(0)  # DoNothing