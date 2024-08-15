import sys


def stabilize():
    max_steps = 350
    actions_taken = []

    def take_action(action):
        print(action)
        actions_taken.append(action)

    def needed_measurements(observations):
        if observations[33] <= 0:
            take_action(24)  # UseMonitorPads
        if observations[34] <= 0:
            take_action(25)  # UseSatsProbe
        if observations[35] <= 0:
            take_action(27)  # UseBloodPressureCuff

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vital_signs_times, vital_signs_values = (
            observations[:33],
            observations[33:40],
            observations[40:],
        )

        vitals = {
            "RespRate": vital_signs_values[1] if vital_signs_times[1] > 0 else None,
            "MAP": vital_signs_values[4] if vital_signs_times[4] > 0 else None,
            "Sats": vital_signs_values[5] if vital_signs_times[5] > 0 else None,
        }

        # Cardiac arrest condition
        if (vitals["MAP"] is not None and vitals["MAP"] < 20) or (
            vitals["Sats"] is not None and vitals["Sats"] < 65
        ):
            take_action(17)  # Start chest compression
            continue

        # Ensure measurements are taken
        needed_measurements(observations)

        # Airway assessment and intervention
        if any(events[i] > 0 for i in [4, 5, 6]):
            take_action(3)  # ExamineAirway
            if events[5] > 0:  # AirwayVomit
                take_action(31)  # Use Yankeur Suction Catheter
            elif events[6] > 0:  # AirwayTongue
                take_action(36)  # Perform Head-Tilt Chin-Lift
            continue

        # Breathing assessment and intervention
        if vitals["Sats"] is not None and vitals["Sats"] < 88:
            take_action(30)  # Use non-rebreather mask
            continue
        elif vitals["RespRate"] is not None and vitals["RespRate"] < 8:
            take_action(29)  # Use bag-valve mask
            continue

        if any(events[i] > 0 for i in [7, 10, 11, 12, 13, 14]):
            take_action(4)  # ExamineBreathing
            if events[7] > 0:  # BreathingNone
                take_action(29)  # Use bag-valve mask
            continue

        # Circulation assessment and intervention
        if vitals["MAP"] is not None and vitals["MAP"] < 60:
            take_action(15)  # Give IV Fluids
            continue

        if any(events[i] > 0 for i in range(21, 24)):  # AVPU
            take_action(8)  # ExamineResponse
            continue

        take_action(48)  # Finish if no appropriate action found


if __name__ == "__main__":
    stabilize()