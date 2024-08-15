import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    for step in range(350):
        observations = list(map(float, input().strip().split()))

        if len(observations) != 53:
            take_action(0)  # DoNothing
            continue

        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)  # StartChestCompression
            continue

        if vitals["MAP"] is None:
            take_action(27)  # UseBloodPressureCuff
            continue

        if vitals["Sats"] is None:
            take_action(25)  # UseSatsProbe
            continue

        if events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0:
            take_action(3)  # ExamineAirway
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # UseYankeurSucionCatheter
            elif events[6] > 0:
                take_action(32)  # UseGuedelAirway
            continue

        if events[7] > 0 or events[8] > 0 or events[9] > 0 or events[10] > 0 or events[11] > 0 or events[12] > 0 or events[13] > 0 or events[14] > 0:
            take_action(4)  # ExamineBreathing
            if events[7] > 0:
                take_action(29)  # UseBagValveMask
            elif events[14] > 0:
                take_action(30)  # UseNonRebreatherMask
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if events[15] > 0 or events[16] > 0 or events[17] > 0 or events[18] > 0 or events[19] > 0:
            take_action(5)  # ExamineCirculation
            continue

        if events[20] > 0 or events[21] > 0 or events[22] > 0 or events[23] > 0 or events[24] > 0 or events[25] > 0:
            take_action(6)  # ExamineDisability
            continue
            
        if events[26] > 0 or events[27] > 0 or events[28] > 0 or events[29] > 0 or events[30] > 0 or events[31] > 0 or events[32] > 0:
            take_action(7)  # ExamineExposure
            continue

        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()