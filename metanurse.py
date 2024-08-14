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

    def read_observations():
        observations = list(map(float, input().strip().split()))
        events, vital_sign_times, vital_sign_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )
        vitals = {
            name: value if vital_sign_times[idx] > 0 else None
            for idx, (name, value) in enumerate(
                zip(
                    ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature",
                     "MAP", "Sats", "Resps"], vital_sign_values
                )
            )
        }
        return events, vitals

    for step in range(max_steps):
        if done:
            break

        events, vitals = read_observations()

        if 25 not in actions_taken:
            take_action(25)  # UseSatsProbe
            continue
        if 27 not in actions_taken:
            take_action(27)  # UseBloodPressureCuff
            continue
        if 16 not in actions_taken:
            take_action(16)  # ViewMonitor
            continue
        if 3 not in actions_taken:
            take_action(3)   # ExamineAirway
            continue

        if events[4] > 0 or events[5] > 0:
            take_action(31)  # UseYankeurSuctionCatheter
            continue

        if events[6] > 0:
            take_action(36)  # PerformHeadTiltChinLift
            continue

        if any(events[i] > 0 for i in [29, 30, 31, 32]):
            if 28 not in actions_taken:
                take_action(28)  # AttachDefibPads
                continue
            take_action(40)  # DefibrillatorCharge
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # BagDuringCPR
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
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