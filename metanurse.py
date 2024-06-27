import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step, state):
    sats = obs[46] if obs[39] > 0.5 else 0
    map_value = obs[46] if obs[42] > 0.5 else 0
    resp_rate = obs[47] if obs[43] > 0.5 else 0
    heart_rate = obs[44] if obs[37] > 0.5 else 0

    # Check for cardiac arrest
    if sats < 65 or map_value < 20:
        return 17, "CPR"  # StartChestCompression

    if state == "START":
        return 25, "CHECK_VITALS"  # UseSatsProbe

    if state == "CHECK_VITALS":
        if obs[39] < 0.5:  # If sats not measured
            return 25, "CHECK_VITALS"  # UseSatsProbe
        if obs[42] < 0.5:  # If MAP not measured
            return 27, "CHECK_VITALS"  # UseBloodPressureCuff
        if obs[37] < 0.5:  # If heart rate not measured
            return 26, "CHECK_VITALS"  # UseAline
        return 3, "AIRWAY"  # Start ABCDE assessment

    if state == "AIRWAY":
        if obs[3] < 0.5:  # If airway not checked
            return 3, "AIRWAY"  # ExamineAirway
        if obs[3] > 0.5 and obs[6] > 0.5:  # If airway obstructed
            return 35, "BREATHING"  # PerformAirwayManoeuvres
        return 4, "BREATHING"

    if state == "BREATHING":
        if obs[10] < 0.5:  # If breathing not checked
            return 4, "BREATHING"  # ExamineBreathing
        if sats < 88:
            return 30, "CIRCULATION"  # UseNonRebreatherMask
        return 5, "CIRCULATION"

    if state == "CIRCULATION":
        if obs[16] < 0.5:  # If circulation not checked
            return 5, "CIRCULATION"  # ExamineCirculation
        if map_value < 60:
            return 15, "DISABILITY"  # GiveFluids
        return 6, "DISABILITY"

    if state == "DISABILITY":
        if obs[20] < 0.5:  # If disability not checked
            return 6, "DISABILITY"  # ExamineDisability
        return 7, "EXPOSURE"

    if state == "EXPOSURE":
        if obs[26] < 0.5:  # If exposure not checked
            return 7, "EXPOSURE"  # ExamineExposure
        return 16, "MONITOR"  # ViewMonitor

    if state == "MONITOR":
        if sats >= 88 and map_value >= 60 and resp_rate >= 8:
            return 48, "FINISH"  # Finish
        return 0, "START"  # Restart assessment cycle

    return 48, "FINISH"  # Finish if we reach here (shouldn't happen)

def main():
    step = 0
    state = "START"
    while True:
        observations = input().strip()
        if not observations:
            break
        obs = parse_observations(observations)
        action, new_state = choose_action(obs, step, state)
        print(action)
        sys.stdout.flush()
        state = new_state
        step += 1

if __name__ == "__main__":
    main()