import sys
import numpy as np


def stabilize():
    max_steps = 350

    def take_action(action):
        print(action)
        sys.stdout.flush()

    actions_taken = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        if len(observations) != 53:
            continue

        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "HR": vital_signs_values[0] if vital_signs_times[0] > 0 else None,
            "RR": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # StartChestCompression
            continue

        if vitals["HR"] and (vitals["HR"] < 60 or vitals["HR"] > 100):
            take_action(24)  # UseMonitorPads
            take_action(43)  # DefibrillatorPace
            continue

        if not all(v > 0 for v in vital_signs_times):
            if 27 not in actions_taken:  # UseBloodPressureCuff
                take_action(27)
                actions_taken.add(27)
                continue
            if 25 not in actions_taken:  # UseSatsProbe
                take_action(25)
                actions_taken.add(25)
                continue
            continue

        if any(events[3:7]):  # Check Airway events
            take_action(3)  # ExamineAirway
            if events[4] > 0 or events[5] > 0:
                take_action(31)  # UseYankeurSuctionCatheter
            elif events[6] > 0:
                take_action(32)  # UseGuedelAirway
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

        take_action(48)  # Finish
        break


if __name__ == "__main__":
    stabilize()