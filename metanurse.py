import math


def parse_observations(obs_str):
    return list(map(float, obs_str.split()))


def select_action(observations):
    event_relevance = observations[:33]
    vital_signs_relevance = observations[33:40]
    vital_signs_measurements = observations[40:47]

    if vital_signs_measurements[5] < 65 or vital_signs_measurements[4] < 20:
        return 47

    if max(event_relevance[:3]) > 0:
        return 8
    if max(event_relevance[3:7]) > 0:
        return 3
    if max(event_relevance[7:16]) > 0:
        return 4
    if max(event_relevance[16:24]) > 0:
        return 5
    if max(event_relevance[24:33]) > 0:
        return 6
    if max(event_relevance[33:]) > 0:
        return 7

    if vital_signs_relevance[0] == 0:
        return 27
    if vital_signs_relevance[1] == 0:
        return 25
    if vital_signs_relevance[4] == 0:
        return 27
    if vital_signs_relevance[5] == 0:
        return 25

    if vital_signs_measurements[5] < 88:
        return 30
    if vital_signs_measurements[1] < 8:
        return 29
    if vital_signs_measurements[4] < 60:
        return 15

    return 0


def main():
    steps = 0
    while steps < 350:
        observations = input()
        action = select_action(parse_observations(observations))
        print(action)
        if action == 48:
            break
        steps += 1


if __name__ == "__main__":
    main()