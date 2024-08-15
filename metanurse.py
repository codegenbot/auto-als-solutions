import sys

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()
    for step in range(350):
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
            vitals["MAP"] is not None and vitals["MAP"] < 20
        ):
            take_action(17)  # StartChestCompression
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

        if events[3] == 0:  # AirwayClear not confirmed
            take_action(3)  # ExamineAirway
            continue
        if events[7] == 0:  # BreathingNone not examined
            take_action(4)  # ExamineBreathing
            continue
        if events[15] == 0:  # RadialPulsePalpable not examined
            take_action(5)  # ExamineCirculation
            continue
        if events[20] == 0:  # AVPU_A not examined
            take_action(6)  # ExamineDisability
            continue
        if events[26] == 0:  # ExposureRash not examined
            take_action(7)  # ExamineExposure
            continue
        
        # Perform final checks and reassess, then finish if all criteria are met
        if vitals["Sats"] is not None and vitals["Sats"] >= 88 and \
            vitals["RR"] is not None and vitals["RR"] >= 8 and \
            vitals["MAP"] is not None and vitals["MAP"] >= 60 and \
            events[3] > 0:
            take_action(48)  # Finish
            break

        take_action(0)  # DoNothing to await further assessment

if __name__ == "__main__":
    stabilize()