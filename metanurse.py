import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs):
    # Initialize variables to track patient state
    airway_checked = breathing_checked = circulation_checked = disability_checked = exposure_checked = False
    sats = map = 0
    
    # Check if vital signs have been measured recently
    recent_sats = obs[39] > 0.5
    recent_map = obs[42] > 0.5
    
    if recent_sats:
        sats = obs[46]
    if recent_map:
        map = obs[46]
    
    # ABCDE assessment
    if not airway_checked:
        return 3  # ExamineAirway
    elif not breathing_checked:
        return 4  # ExamineBreathing
    elif not circulation_checked:
        return 5  # ExamineCirculation
    elif not disability_checked:
        return 6  # ExamineDisability
    elif not exposure_checked:
        return 7  # ExamineExposure
    
    # Check vital signs
    if not recent_sats:
        return 25  # UseSatsProbe
    if not recent_map:
        return 27  # UseBloodPressureCuff
    
    # Stabilization actions
    if sats < 88:
        return 30  # UseNonRebreatherMask
    if map < 60:
        return 15  # GiveFluids
    
    # Check if patient is stabilized
    if sats >= 88 and map >= 60:
        return 48  # Finish
    
    # Default action
    return 0  # DoNothing

def main():
    while True:
        observations = input().strip()
        if not observations:
            break
        obs = parse_observations(observations)
        action = choose_action(obs)
        print(action)
        sys.stdout.flush()

if __name__ == "__main__":
    main()