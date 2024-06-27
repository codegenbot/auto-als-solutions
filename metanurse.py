import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step):
    sats = obs[46] if obs[39] > 0.5 else 0
    map = obs[46] if obs[42] > 0.5 else 0
    resp_rate = obs[47] if obs[40] > 0.5 else 0
    
    if obs[7] > 0.5:  # BreathingNone
        return 29  # UseBagValveMask
    
    if step == 0:
        return 18  # OpenAirwayDrawer
    elif step == 1:
        return 19  # OpenBreathingDrawer
    elif step == 2:
        return 20  # OpenCirculationDrawer
    elif step == 3:
        return 21  # OpenDrugsDrawer
    elif step == 4:
        return 3  # ExamineAirway
    elif step == 5:
        return 4  # ExamineBreathing
    elif step == 6:
        return 5  # ExamineCirculation
    elif step == 7:
        return 6  # ExamineDisability
    elif step == 8:
        return 7  # ExamineExposure
    
    if obs[39] <= 0.5:
        return 25  # UseSatsProbe
    if obs[42] <= 0.5:
        return 27  # UseBloodPressureCuff
    if obs[40] <= 0.5:
        return 38  # TakeBloodPressure
    
    if sats < 88:
        return 30  # UseNonRebreatherMask
    if map < 60:
        return 15  # GiveFluids
    if resp_rate < 8:
        return 29  # UseBagValveMask
    
    if sats >= 88 and map >= 60 and resp_rate >= 8:
        return 48  # Finish
    
    if step >= 349:
        return 48  # Finish
    
    return 16  # ViewMonitor

def main():
    step = 0
    while True:
        observations = input().strip()
        if not observations:
            break
        obs = parse_observations(observations)
        action = choose_action(obs, step)
        print(action)
        sys.stdout.flush()
        step += 1

if __name__ == "__main__":
    main()