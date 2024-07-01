sats_minimum = 88
resp_rate_minimum = 8
map_minimum = 60
critical_low_sats = 65
critical_low_map = 20

while steps < 350:
    steps += 1
    observations = input().split()
    events = list(map(float, observations[:39]))
    measured_times = list(map(float, observations[39:46]))
    measured_values = list(map(float, observations[46:]))

    # Critical immediate response
    if measured_times[5] > 0 and measured_values[5] < critical_low_sats:
        print(17)  # Extreme low sats, start chest compression
        continue
    if measured_times[4] > 0 and measured_values[4] < critical_low_map:
        print(17)  # Extreme low MAP, start chest compression
        continue

    # Assessments according to ABCDE
    if not airway_confirmed:
        print(3)  # ExamineAirway
        airway_confirmed = True
    elif events[7] > 0 or (
        measured_times[6] > 0 and measured_values[6] < resp_rate_minimum
    ):
        print(29)  # UseBagValveMask for insufficient breathing
    elif (
        measured_times[5] == 0 or measured_values[5] < sats_minimum
    ) and not satsProbeUsed:
        print(19)  # OpenBreathingDrawer
    elif measured_times[5] == 0 or measured_values[5] < sats_minimum:
        print(25)  # UseSatsProbe
    elif measured_times[4] == 0 or measured_values[4] < map_minimum:
        print(27)  # UseBloodPressureCuff
    elif (
        measured_times[5] > 0
        and measured_values[5] >= sats_minimum
        and measured_times[6] > 0
        and measured_values[6] >= resp_rate_minimum
        and measured_times[4] > 0
        and measured_values[4] >= map_minimum
    ):
        print(48)  # Finish the game if stabilized
        break
    else:
        print(0)  # DoNothing