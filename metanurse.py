import sys

def get_vital_sign(vital_signs_times, vital_signs_values, index):
    return vital_signs_values[index] if vital_signs_times[index] > 0 else None

def main():
    max_steps = 350
    status = {
        "opened_breathing_drawer": False, 
        "used_pulse_oximeter": False, 
        "viewed_monitor": False,
        "examined_airway": False,
        "examined_breathing": False,
        "examined_circulation": False,
        "examined_disability": False,
        "examined_exposure": False,
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

        if not status["examined_airway"]:
            print(3)  # ExamineAirway
            status["examined_airway"] = True
            continue
        
        if not status["examined_breathing"]:
            print(4)  # ExamineBreathing
            status["examined_breathing"] = True
            continue

        if not status["examined_circulation"]:
            print(5)  # ExamineCirculation
            status["examined_circulation"] = True
            continue

        if not status["examined_disability"]:
            print(6)  # ExamineDisability
            status["examined_disability"] = True
            continue

        if not status["examined_exposure"]:
            print(7)  # ExamineExposure
            status["examined_exposure"] = True
            continue        
        
        if not status["opened_breathing_drawer"]:
            print(19)  # OpenBreathingDrawer
            status["opened_breathing_drawer"] = True
            continue

        if not status["used_pulse_oximeter"]:
            print(25)  # UseSatsProbe
            status["used_pulse_oximeter"] = True
            continue

        if not status["viewed_monitor"]:
            print(16)  # ViewMonitor
            status["viewed_monitor"] = True
            continue

        if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
            print(17)  # StartChestCompression
            continue

        if map_value is not None and map_value < 60:
            print(15)  # GiveFluids
            continue

        if sats is not None and sats < 88:
            print(30)  # UseNonRebreatherMask
            continue

        if resp_rate is not None and resp_rate < 8:
            print(29)  # UseBagValveMask
            continue

        if heart_rate is not None:
            if heart_rate < 50:
                print(12)  # GiveAtropine
                continue
            elif heart_rate > 100:
                print(2)  # CheckRhythm
                if heart_rate > 150:
                    print(9)  # GiveAdenosine
                continue

        print(48)  # Finish
        return

    print(48)  # Finish in case steps exceed max_steps

if __name__ == "__main__":
    main()