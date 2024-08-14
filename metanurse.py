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

    def need_measurements():
        return 25 not in actions_taken or 27 not in actions_taken or 16 not in actions_taken or 3 not in actions_taken

    def need_measurement_action():
        if 25 not in actions_taken:
            return 25  # UseSatsProbe
        if 27 not in actions_taken:
            return 27  # UseBloodPressureCuff
        if 16 not in actions_taken:
            return 16  # ViewMonitor
        if 3 not in actions_taken:
            return 3  # ExamineAirway
        return None

    def update_vitals(times, values):
        return {
            "HeartRate": values[0] if times[0] else None,
            "RespRate": values[1] if times[1] else None,
            "MAP": values[4] if times[4] else None,
            "Sats": values[5] if times[5] else None,
        }

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, times, values = observations[:33], observations[33:40], observations[40:]

        if need_measurements():
            measurement_action = need_measurement_action()
            if measurement_action:
                take_action(measurement_action)
                continue

        vitals = update_vitals(times, values)

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            take_action(17)  # StartChestCompression
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            take_action(22)  # BagDuringCPR
            continue

        if events[4] > 0 or events[5] > 0:  # Vomit, Blood in Airway
            take_action(31)  # UseSuction
            continue

        if events[6] > 0:  # Tongue obstruction
            take_action(36)  # HeadTiltChinLift
            continue
        
        if events[7] > 0 or (vitals["RespRate"] is not None and vitals["RespRate"] < 8):  # No Breathing
            take_action(29)  # UseBagValveMask
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # GiveFluids
            continue

        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue

        if any(events[i] > 0 for i in range(28, 33)):  # Tachyarrhythmia events
            if 2 not in actions_taken:
                take_action(2)  # CheckRhythm
                continue
            if 28 not in actions_taken:
                take_action(28)  # AttachDefibPads
                continue
            if vitals["MAP"] is not None and vitals["MAP"] < 60:
                take_action(40)  # ChargeDefibrillator
                take_action(11)  # GiveAmiodarone
                continue
        
        if all([(vitals[key] is not None and vitals[key] >= min_val) for key, min_val in {
            "Sats": 88,
            "RespRate": 8,
            "MAP": 60
        }.items()]):
            take_action(48)  # Finish
            break
        
    if not done:
        take_action(48)  # Finish

if __name__ == "__main__":
    stabilize()