airway_confirmed = False
breathing_assessed = False
circulation_checked = False
disability_checked = False
sats_probe_used = False
bp_cuff_used = False

while True:
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    if (measured_times[5] > 0 and measured_values[5] < 65) or (
        measured_times[4] > 0 and measured_values[4] < 20
    ):
        print(17)  # StartChestCompression
        continue

    if not airway_confirmed:
        if events[3] > 0.5:  # AirwayClear is confirmed
            airway_confirmed = True
        elif (
            events[4] > 0.5 or events[5] > 0.5 or events[6] > 0.5
        ):  # Obstructions like Vomit, Blood, Tongue
            print(3)  # ExamineAirway again if there might be obstruction
            continue
        else:
            print(3)  # ExamineAirway
            continue

    if events[7] > 0.5:  # BreathingNone has high relevance
        print(29)  # UseBagValveMask
        continue
    if measured_times[5] > 0 and measured_values[5] < 88 and not sats_probe_used:
        print(25)  # UseSatsProbe
        sats_probe_used = True
        continue
    if measured_times[6] > 0 and measured_values[6] < 8:
        print(29)  # UseBagValveMask
        continue
    if not breathing_assessed:
        print(4)  # ExamineBreathing
        breathing_assessed = True
        continue

    if measured_times[4] > 0 and measured_values[4] < 60:
        print(15)  # GiveFluids
        continue
    if not circulation_checked:
        print(5)  # ExamineCirculation
        circulation_checked = True
        continue

    if not disability_checked:
        print(6)  # ExamineDisability
        disability_checked = True
        continue

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
        break  # All conditions for stabilization met, can safely finish

    if not sats_probe_used:
        print(25)  # UseSatsProbe
        sats_probe_used = True
        continue
    if not bp_cuff_used:
        print(27)  # UseBloodPressureCuff
        bp_cuff_used = True
        continue
    print(16)  # ViewMonitor if no critical condition to address