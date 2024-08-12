import sys

def get_vital_sign(vital_signs_times, vital_signs_values, index):
    return vital_signs_values[index] if vital_signs_times[index] > 0 else None

def main():
    max_steps = 350
    status = {
        "opened_breathing_drawer": False, 
        "used_pulse_oximeter": False, 
        "viewed_monitor": False,
        "opened_circulation_drawer": False,
        "used_blood_pressure_cuff": False
    }

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        sats = get_vital_sign(vital_signs_times, vital_signs_values, 5)
        map_value = get_vital_sign(vital_signs_times, vital_signs_values, 4)
        resp_rate = get_vital_sign(vital_signs_times, vital_signs_values, 1)
        heart_rate = get_vital_sign(vital_signs_times, vital_signs_values, 0)

        if events[3]:  # AirwayClear
            if not status["opened_breathing_drawer"]:
                print(19)
                status["opened_breathing_drawer"] = True
                continue

            if not status["used_pulse_oximeter"]:
                print(25)
                status["used_pulse_oximeter"] = True
                continue

            if not status["viewed_monitor"]:
                print(16)
                status["viewed_monitor"] = True
                continue

            if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
                print(17)
                continue

            if map_value is not None and map_value < 60:
                if not status["opened_circulation_drawer"]:
                    print(20)
                    status["opened_circulation_drawer"] = True
                    continue
                if not status["used_blood_pressure_cuff"]:
                    print(27)
                    status["used_blood_pressure_cuff"] = True
                    continue
                print(15)
                continue

            if sats is not None and sats < 88:
                print(30)
                continue

            if resp_rate is not None and resp_rate < 8:
                print(29)
                continue

            if heart_rate is not None:
                if heart_rate < 50:
                    print(12)
                    continue
                elif heart_rate > 100:
                    print(2)  # CheckRhythm before deciding action
                    if heart_rate > 150:
                        print(9)  # GiveAdenosine; adjust to the specific situation
                    continue

            if sats >= 88 and map_value >= 60 and resp_rate >= 8:
                print(48)
                return

        print(3)  # ExamineAirway

if __name__ == "__main__":
    main()