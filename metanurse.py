import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step_count):
    # Initialize variables to track patient state
    airway_checked = breathing_checked = circulation_checked = disability_checked = exposure_checked = False
    sats = map = resp_rate = 0
    
    # Check if vital signs have been measured recently
    recent_sats = obs[39] > 0.5
    recent_map = obs[42] > 0.5
    recent_resp = obs[40] > 0.5
    
    if recent_sats:
        sats = obs[46]
    if recent_map:
        map = obs[46]
    if recent_resp:
        resp_rate = obs[47]
    
    # ABCDE assessment
    if not airway_checked:
        airway_checked = True
        return 3  # ExamineAirway
    elif not breathing_checked:
        breathing_checked = True
        return 4  # ExamineBreathing
    elif not circulation_checked:
        circulation_checked = True
        return 5  # ExamineCirculation
    elif not disability_checked:
        disability_checked = True
        return 6  # ExamineDisability
    elif not exposure_checked:
        exposure_checked = True
        return 7  # ExamineExposure
    
    # Check vital signs
    if not recent_sats:
        return 25  # UseSatsProbe
    if not recent_map:
        return 27  # UseBloodPressureCuff
    if not recent_resp:
        return 38  # TakeBloodPressure (to measure respiratory rate)
    
    # Stabilization actions
    if sats < 88:
        return 30  # UseNonRebreatherMask
    if map < 60:
        return 15  # GiveFluids
    if resp_rate < 8:
        return 29  # UseBagValveMask
    
    # Check if patient is stabilized
    if sats >= 88 and map >= 60 and resp_rate >= 8:
        return 48  # Finish
    
    # Check for cardiac arrest conditions
    if sats < 65 or map < 20:
        return 17  # StartChestCompression
    
    # Default action
    return 0  # DoNothing

def main():
    step_count = 0
    while step_count < 350:
        observations = input().strip()
        if not observations:
            break
        obs = parse_observations(observations)
        action = choose_action(obs, step_count)
        print(action)
        sys.stdout.flush()
        step_count += 1
        if action == 48:  # Finish
            break

if __name__ == "__main__":
    main()