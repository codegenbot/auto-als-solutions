import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    examined_vitals = {"MAP": False, "Sats": False, "RR": False, "HR": False}
    final_check = False

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

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # StartChestCompression
            continue

        if not examined_vitals["MAP"] and vital_signs_times[4] == 0:
            examined_vitals["MAP"] = True
            take_action(27)  # UseBloodPressureCuff
            continue

        if not examined_vitals["Sats"] and vital_signs_times[5] == 0:
            examined_vitals["Sats"] = True
            take_action(25)  # UseSatsProbe
            continue

        if not examined_vitals["RR"] and vital_signs_times[1] == 0:
            examined_vitals["RR"] = True
            take_action(4)  # ExamineBreathing
            continue

        if not examined_vitals["HR"] and vital_signs_times[0] == 0:
            examined_vitals["HR"] = True
            take_action(5)  # ExamineCirculation
            continue

        if any(events[i] > 0 for i in range(3, 7)):  # Airway events
            take_action(3)  # ExamineAirway
            continue

        if any(events[7:15]):  # Breathing events
            take_action(4)  # ExamineBreathing
            continue

        if events[7] > 0:
            take_action(29)  # UseBagValveMask
            continue
        
        if events[14] > 0:
            take_action(19)  # OpenBreathingDrawer
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

        if (vitals["HR"] is not None) and (vitals["HR"] > 150):
            take_action(9)  # GiveAdenosine
            continue

        if any(events[20:26]):  # Disability events
            take_action(6)  # ExamineDisability
            continue

        if any(events[26:33]):  # Exposure events
            take_action(7)  # ExamineExposure
            continue

        if vitals["MAP"] is not None and vitals["Sats"] is not None and vitals["RR"] is not None:
            if vitals["MAP"] >= 60 and vitals["Sats"] >= 88 and vitals["RR"] >= 8:
                take_action(48)  # Finish
                break
        
        take_action(16)  # ViewMonitor

if __name__ == "__main__":
    stabilize()