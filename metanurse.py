import math


def parse_observations(obs):
    events = obs[:33]
    vital_signs_times = obs[33:40]
    vital_signs_values = obs[40:]
    return events, vital_signs_times, vital_signs_values


def get_action(events, vital_signs_times, vital_signs_values):
    # Check for cardiac arrest conditions
    if vital_signs_values[5] < 65 or vital_signs_values[4] < 20:
        return 47  # DefibrillatorSync

    # Prioritize stabilizing airway, breathing, and circulation
    if events[3] == 0:  # AirwayClear
        return 3  # ExamineAirway
    if events[7] == 0:  # BreathingNone
        return 4  # ExamineBreathing
    if events[16] == 0:  # RadialPulsePalpable
        return 5  # ExamineCirculation

    # Check vital signs
    if vital_signs_times[5] == 0:  # MeasuredSats
        if vital_signs_values[5] < 88:
            return 30  # UseNonRebreatherMask
    if vital_signs_times[4] == 0:  # MeasuredMAP
        if vital_signs_values[4] < 60:
            return 15  # GiveFluids
    if vital_signs_times[1] == 0:  # MeasuredRespRate
        if vital_signs_values[1] < 8:
            return 29  # UseBagValveMask

    # Default action if no specific condition is met
    return 0  # DoNothing


def main():
    max_steps = 350
    for _ in range(max_steps):
        obs = list(map(float, input().split()))
        events, vital_signs_times, vital_signs_values = parse_observations(obs)
        action = get_action(events, vital_signs_times, vital_signs_values)
        print(action)
        if action == 48:  # Finish
            break


if __name__ == "__main__":
    main()