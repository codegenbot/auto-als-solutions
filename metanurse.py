import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    step_count = 0

    def perform_abcde(vitals, actions_taken):
        if "airway" not in actions_taken:
            take_action(3)
            actions_taken.add("airway")
            return True
        if vitals["RR"] is None and "asked_breathing" not in actions_taken:
            take_action(4)
            actions_taken.add("asked_breathing")
            return True
        if vitals["MAP"] is None and "asked_circulation" not in actions_taken:
            take_action(5)
            actions_taken.add("asked_circulation")
            return True
        if vitals["Sats"] is None and "asked_sats" not in actions_taken:
            take_action(25)
            actions_taken.add("asked_sats")
            return True
        return False
    
    while step_count < 350:
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            take_action(0)
            continue

        events = observations[:33]
        times = observations[33:40]
        values = observations[40:]

        vitals = {
            "HR": values[0] if times[0] > 0 else None,
            "RR": values[1] if times[1] > 0 else None,
            "MAP": values[4] if times[4] > 0 else None,
            "Sats": values[5] if times[5] > 0 else None,
        }

        if (vitals["Sats"] is not None and vitals["Sats"] < 65) or (
            vitals["MAP"] is not None and vitals["MAP"] < 20):
            take_action(17)
            continue
        
        if perform_abcde(vitals, actions_taken):
            continue
        
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)
            continue

        if vitals["RR"] is not None and vitals["RR"] < 8:
            take_action(29)
            continue

        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)
            continue

        take_action(48)
        break

        step_count += 1

if __name__ == "__main__":
    stabilize()