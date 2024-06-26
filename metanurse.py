import sys


def handle_airway(events, times, measurements):
    if events[3] <= 0.1:  # AirwayClear has low relevance
        return 3  # ExamineAirway
    if events[6] > 0.1:  # AirwayTongue
        return 32  # UseGuedelAirway
    if events[7] > 0.1:  # BreathingNone
        return 29  # UseBagValveMask
    return None


def handle_breathing(events, times, measurements):
    sats = measurements[5] if times[5] > 0 else None
    if sats is None or sats < 88:
        return 30  # UseNonRebreatherMask
    return None


def handle_circulation(events, times, measurements):
    radial_pulse_palp = events[16]
    radial_pulse_nonpalp = events[17]
    if radial_pulse_nonpalp > 0.1:
        return 17  # StartChestCompression
    if radial_pulse_palp <= 0.2:
        return 5  # ExamineCirculation
    map_value = measurements[4] if times[4] > 0 else None
    if map_value is None or map_value < 60:
        return 27  # UseBloodPressureCuff
    return None


def handle_disability(events, times, measurements):
    avpu_u = events[21]
    if avpu_u <= 0.1:
        return 6  # ExamineDisability
    return None


def main():
    loop_counter = 0
    while True:
        observations = input().strip().split()
        events = [float(e) for e in observations[:39]]
        times = [float(t) for t in observations[39:46]]
        measurements = [float(m) for m in observations[46:]]

        sats = measurements[5] if times[5] > 0 else None
        map_value = measurements[4] if times[4] > 0 else None
        resp_rate = measurements[6] if times[6] > 0 else None

        # Immediate Critical Handling
        if sats is not None and sats < 65 or (map_value is not None and map_value < 20):
            print(17)  # StartChestCompression
            continue

        action = (
            handle_airway(events, times, measurements)
            or handle_breathing(events, times, measurements)
            or handle_circulation(events, times, measurements)
            or handle_disability(events, times, measurements)
        )

        if action is not None:
            print(action)
        else:
            # Check stabilization condition
            if (
                sats is not None
                and sats >= 88
                and map_value is not None
                and map_value >= 60
                and resp_rate is not None
                and resp_rate >= 8
            ):
                print(48)  # Finish - John is stabilized
                break
            else:
                print(0)  # Default action when no immediate intervention is needed

        loop_counter += 1
        if loop_counter >= 350:
            break


main()