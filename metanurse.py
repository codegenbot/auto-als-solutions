import sys

def stabilize():
    max_steps = 350

    def take_action(action):
        print(action)
        sys.stdout.flush()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue
        
        events, vitals_time, vitals_value = observations[:33], observations[33:40], observations[40:]
        
        HR = vitals_value[0] if vitals_time[0] > 0 else None
        RR = vitals_value[1] if vitals_time[1] > 0 else None
        MAP = vitals_value[4] if vitals_time[4] > 0 else None
        Sats = vitals_value[5] if vitals_time[5] > 0 else None

        if (MAP is not None and MAP < 20) or (Sats is not None and Sats < 65):
            take_action(17)  # StartChestCompression
            take_action(23)  # ResumeCPR
            continue
        
        if Sats and Sats < 88:
            take_action(30)  # UseNonRebreatherMask
            continue
        
        if RR and RR < 8:
            take_action(29)  # UseBagValveMask
            continue
        
        if MAP and MAP < 60:
            take_action(15)  # GiveFluids
            continue
        
        if events[3] > 0 or events[4] > 0 or events[5] > 0 or events[6] > 0:
            take_action(3)  # ExamineAirway
            continue
        
        if events[7] > 0 or any(events[8:15]):
            take_action(4)  # ExamineBreathing
            continue
        
        if events[15] > 0 or any(events[16:20]):
            take_action(5)  # ExamineCirculation
            continue
        
        if events[20] > 0 or any(events[21:26]):
            take_action(6)  # ExamineDisability
            continue
        
        if any(events[26:33]):
            take_action(7)  # ExamineExposure
            continue
        
        take_action(48)  # Finish
        break

if __name__ == "__main__":
    stabilize()