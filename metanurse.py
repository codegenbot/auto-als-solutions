import math


def parse_observations(obs_str):
    return list(map(float, obs_str.split()))


def select_action(observations):
    event_relevance = observations[:33]
    vital_signs_relevance = observations[33:40]
    vital_signs_measurements = observations[40:47]

    if vital_signs_measurements[5] < 65 or vital_signs_measurements[4] < 20:
        return 47  # Finish if in cardiac arrest

    if event_relevance[7] > 0:  # BreathingNone
        return 29  # UseBagValveMask

    if vital_signs_measurements[5] < 88:  # Low Sats
        return 30  # UseNonRebreatherMask

    if vital_signs_measurements[4] < 60:  # Low MAP
        return 27  # UseBloodPressureCuff

    if vital_signs_relevance[1] == 0:  # Resp rate not measured
        return 25  # UseSatsProbe

    if vital_signs_relevance[4] == 0:  # MAP not measured
        return 27  # UseBloodPressureCuff

    if vital_signs_relevance[5] == 0:  # Sats not measured
        return 25  # UseSatsProbe

    return 0  # DoNothing


def main():
    steps = 0
    while steps < 350:
        observations = input()
        action = select_action(parse_observations(observations))
        print(action)
        if action == 48:  # Finish
            break
        steps += 1


if __name__ == "__main__":
    main()