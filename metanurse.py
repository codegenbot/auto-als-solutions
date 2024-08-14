import sys

def stabilize():
    max_steps = 350
    actions_taken = set()
    done = False

    def take_action(action, break_action=True):
        nonlocal done
        actions_taken.add(action)
        print(action)
        if action == 48:
            done = True
        return break_action

    def need_measurements():
        return not all(x in actions_taken for x in {25, 27, 16, 3})

    def perform_aggressive_resuscitation(vitals, events):
        if events[4] > 0 or events[5] > 0:  # Vomit or Blood in Airway
            return take_action(31)  # UseSuction
        if events[6] > 0:  # Tongue Obstruction
            return take_action(36)  # HeadTiltChinLift
        if events[7] > 0:  # No Breathing
            return take_action(29)  # UseBagValveMask

        if any(events[i] > 0 for i in range(28, 33)):  # Unstable Tachyarrhythmia
            take_action(28)  # AttachDefibPads
            return take_action(40)  # DefibrillatorCharge

        if vitals["MAP"] is not None and vitals["MAP"] < 20:
            return take_action(17)  # StartChestCompression
        if vitals["Sats"] is not None and vitals["Sats"] < 65:
            return take_action(22)  # BagDuringCPR

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            return take_action(15)  # GiveFluids
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            return take_action(30)  # UseNonRebreatherMask
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            return take_action(29)  # UseBagValveMask
        
        return False

    for step in range(max_steps):
        if done:
            break

        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = observations[:33], observations[33:40], observations[40:]
        
        if need_measurements():
            if take_action({25, 27, 16, 3} - actions_taken.pop()):
                continue
        
        vitals = {
            "HeartRate": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if perform_aggressive_resuscitation(vitals, events):
            continue

        if actions_taken >= {25, 27, 16, 3}:
            if take_action(48, False):  # Finish after all measurements
                break

if __name__ == "__main__":
    stabilize()