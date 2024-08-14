import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]

        # Prioritize checking measurements
        if step == 0:
            take_action(25)  # UseSatsProbe
            continue
        if step == 1:
            take_action(27)  # UseBloodPressureCuff
            continue
        if step == 2:
            take_action(16)  # ViewMonitor
            continue
        if step == 3:
            take_action(3)   # ExamineAirway
            continue

        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if events[4] > 0 or events[5] > 0:
            take_action(31)  # UseYankeurSucionCatheter
            continue
        if events[6] > 0:
            take_action(36)  # PerformHeadTiltChinLift
            continue
        if events[7] > 0:
            take_action(29)  # UseBagValveMask
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # BagDuringCPR
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()