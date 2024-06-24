import sys

def get_action(observations):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    global step
    step += 1

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return 17  # StartChestCompression if vital signs are critically low

    # Perform initial measurements if not already measured
    if step == 1:
        return 25  # UseSatsProbe
    elif step == 2:
        return 27  # UseBloodPressureCuff
    elif step == 3:
        return 16  # ViewMonitor

    # Ensure we are actively evaluating all aspects of ABCDE during initial steps
    if step % 7 == 0:
        return 3  # ExamineAirway
    elif step % 7 == 1:
        return 4  # ExamineBreathing
    elif step % 7 == 2:
        return 5  # ExamineCirculation
    elif step % 7 == 3:
        if resp_rate is None:
            return 16  # ViewMonitor for missing Respiratory rate
        elif map_value is None:
            return 16  # ViewMonitor for missing MAP
    elif step % 7 == 4:
        return 6  # ExamineDisability
    elif step % 7 == 5:
        return 7  # ExamineExposure
    elif step % 7 == 6:
        return 1  # CheckSignsOfLife

    if (map_value is not None and map_value < 60):
        return 15  # GiveFluids if circulation is not stable

    if (resp_rate is not None and resp_rate < 8):
        return 30  # UseNonRebreatherMask if breathing is below threshold

    if (sats is not None and sats < 88):
        return 30  # UseNonRebreatherMask if oxygen saturation is low

    if (sats >= 88 and resp_rate >= 8 and map_value >= 60):
        return 48  # Finish if patient is stable

    return 1  # Continually CheckSignsOfLife as default action

global step
step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == 48:
        break