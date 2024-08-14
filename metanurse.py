import sys

def stabilize():
    max_steps = 350
    taken_actions = set()

    def take_action(action):
        print(action)

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events = observations[:33]
        vital_times = observations[33:40]
        vitals = observations[40:]

        measurements = {
            "RespRate": vitals[1] if vital_times[1] > 0 else None,
            "MAP": vitals[4] if vital_times[4] > 0 else None,
            "Sats": vitals[5] if vital_times[5] > 0 else None,
        }

        if 25 not in taken_actions:
            take_action(25)  # UseSatsProbe
            taken_actions.add(25)
            continue
        if 27 not in taken_actions:
            take_action(27)  # UseBloodPressureCuff
            taken_actions.add(27)
            continue
        if 16 not in taken_actions:
            take_action(16)  # ViewMonitor
            taken_actions.add(16)
            continue
        if 3 not in taken_actions:
            take_action(3)  # ExamineAirway
            taken_actions.add(3)
            continue

        if measurements["MAP"] is not None and measurements["MAP"] < 20 or measurements["Sats"] is not None and measurements["Sats"] < 65:
            take_action(17)  # StartChestCompression
            continue

        if measurements["MAP"] is not None and measurements["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if measurements["Sats"] is not None and measurements["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if measurements["RespRate"] is not None and measurements["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        if any(events[i] > 0 for i in [4, 5]):
            take_action(31)  # UseYankeurSucionCatheter
            continue
        
        if events[6] > 0:
            take_action(36)  # PerformHeadTiltChinLift
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(29)  # UseBagValveMask
            continue

        take_action(48)  # Finish
        break
    
if __name__ == "__main__":
    stabilize()