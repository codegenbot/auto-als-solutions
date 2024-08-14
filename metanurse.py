import sys

def stabilize():
    def take_action(action):
        print(action)
        if action == 48:
            sys.exit()

    max_steps = 350
    actions_taken = set()
    focused_measurements = {"MAP": 27, "Sats": 25}

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33], observations[33:40], observations[40:]
        )

        vitals = {
            name: value if vital_signs_times[idx] > 0 else None
            for idx, name, value in zip(range(7), 
                ["HeartRate", "RespRate", "CapillaryGlucose", "Temperature", "MAP", "Sats", "Resps"], 
                vital_signs_values
            )
        }

        # Focus on obtaining necessary measurements 
        for measure, action in focused_measurements.items():
            if measure not in vitals or vitals[measure] is None:
                take_action(action)
                continue

        # Clear airway if obstructed
        if events[1] > 0 or events[2] > 0:
            take_action(31)  # UseYankeurSuctionCatheter
            continue
        if events[6] > 0:
            take_action(36)  # PerformHeadTiltChinLift
            continue

        # Address critical conditions first
        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
            continue
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # BagDuringCPR
            continue

        # Address tachyarrhythmia
        if any(events[i] > 0 for i in range(29, 36)):
            if 28 not in actions_taken:
                take_action(28)  # AttachDefibPads
                actions_taken.add(28)
                continue
            take_action(40)  # DefibrillatorCharge
            continue

        # Stabilize vital signs
        if vitals["MAP"] and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue
        if vitals["Sats"] and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        if vitals["RespRate"] and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue

        # If vitals seem fine, finish
        if step > 200 and all(
            v is not None and v >= t for v, t in zip(
                [vitals["Sats"], vitals["RespRate"], vitals["MAP"]], [88, 8, 60]
            )
        ):
            take_action(48)  # Finish
            break

        # Default to do nothing
        take_action(0)  # DoNothing

if __name__ == "__main__":
    stabilize()