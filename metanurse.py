import sys


def main():
    step = 0
    while step < 350:
        observations = list(map(float, input().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        sats = vital_signs_values[5] if vital_signs_times[5] > 0 else None
        map_value = vital_signs_values[4] if vital_signs_times[4] > 0 else None
        resp_rate = vital_signs_values[1] if vital_signs_times[1] > 0 else None

        if sats is not None and sats < 65 or map_value is not None and map_value < 20:
            print(17)  # Start CPR
            break
        elif sats is not None and sats < 88:
            print(30)  # Provide oxygen
        elif map_value is not None and map_value < 60:
            print(15)  # Give fluids
        elif resp_rate is not None and resp_rate < 8:
            print(29)  # Use bag valve mask
        elif check_stabilization(sats, map_value, resp_rate):
            print(48)  # Finish
            break
        else:
            if vital_signs_times[5] == 0:  # No recent sats measurement
                print(25)  # UseSatsProbe
            elif vital_signs_times[4] == 0:  # No recent MAP measurement
                print(27)  # UseBloodPressureCuff
            elif vital_signs_times[1] == 0:  # No recent resp_rate measurement
                print(4)  # ExamineBreathing
            else:
                print(16)  # ViewMonitor

        sys.stdout.flush()
        step += 1


def check_stabilization(sats, map_value, resp_rate):
    return (
        sats is not None
        and map_value is not None
        and resp_rate is not None
        and sats >= 88
        and map_value >= 60
        and resp_rate >= 8
    )


if __name__ == "__main__":
    main()