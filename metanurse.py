import sys

def stabilize():
    max_steps = 350
    actions_taken = set()

    def take_action(action):
        print(action)
        actions_taken.add(action)
    
    def measure_and_examine():
        measurement_actions = [24, 25, 27]  # Monitor, SatsProbe, BP Cuff
        for action in measurement_actions:
            if action not in actions_taken:
                take_action(action)
                return True
        return False

    def next_action_based_on_events(events):
        if events[8] > 0 or events[5] > 0 or events[6] > 0:  # ResponseNone or Airway issues
            take_action(3)  # ExamineAirway
            if events[5] > 0 or events[6] > 0:  # Vomit or Blood
                take_action(31)  # UseYankeurSuctionCatheter
            elif events[8] > 0:  # None
                take_action(32)  # UseGuedelAirway
        elif events[7] > 0:  # BreathingNone
            take_action(4)  # ExamineBreathing
            take_action(29)  # UseBagValveMask
        elif events[17] == 0 or events[18] > 0:  # No Radial Pulse or Non-palpable Pulse
            take_action(5)  # ExamineCirculation
            take_action(15)  # GiveFluids
        else:
            return False
        return True

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:]
        )
        
        if measure_and_examine():
            continue
        
        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None
        }
        
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (vitals["Sats"] is not None and vitals["Sats"] < 65):
            take_action(17)  # StartChestCompression
            continue
        
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            if any(events[i] > 0 for i in [29, 30, 31, 34, 37]):  # Unstable Tachyarrhythmia
                take_action(24)  # UseMonitorPads
                take_action(40)  # DefibrillatorCharge
                take_action(47)  # DefibrillatorSync
            else:
                take_action(15)  # GiveFluids
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        
        if vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # UseBagValveMask
            continue
        
        if next_action_based_on_events(events):  # Perform assessment or interventions based on events
            continue

        if step > 300:  # Avoid infinite loop, ensure to finalize decision
            take_action(48)  # Finish
            break

    take_action(48)  # Finish if max_steps reached

if __name__ == "__main__":
    stabilize()