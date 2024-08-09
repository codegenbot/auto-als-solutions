import math


def parse_observations(obs_str):
    return list(map(float, obs_str.split()))


def select_action(observations):
    # Extract event relevance and vital signs measurements
    event_relevance = observations[:33]
    vital_signs_relevance = observations[33:40]
    vital_signs_measurements = observations[40:47]

    # Check for critical conditions
    if vital_signs_measurements[5] < 65 or vital_signs_measurements[4] < 20:
        return 47  # Finish if in cardiac arrest

    # Prioritize actions based on observations
    if max(event_relevance[:3]) > 0:  # Response events
        return 8  # ExamineResponse
    if max(event_relevance[3:7]) > 0:  # Airway events
        return 3  # ExamineAirway
    if max(event_relevance[7:16]) > 0:  # Breathing events
        return 4  # ExamineBreathing
    if max(event_relevance[16:24]) > 0:  # Circulation events
        return 5  # ExamineCirculation
    if max(event_relevance[24:33]) > 0:  # Heart rhythm events
        return 6  # ExamineDisability
    if max(event_relevance[33:]) > 0:  # Exposure events
        return 7  # ExamineExposure

    # Check vital signs if not recently checked
    if vital_signs_relevance[0] == 0:  # Heart rate not measured
        return 27  # UseBloodPressureCuff
    if vital_signs_relevance[1] == 0:  # Resp rate not measured
        return 25  # UseSatsProbe
    if vital_signs_relevance[4] == 0:  # MAP not measured
        return 27  # UseBloodPressureCuff
    if vital_signs_relevance[5] == 0:  # Sats not measured
        return 25  # UseSatsProbe

    # Default action if no specific action is needed
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