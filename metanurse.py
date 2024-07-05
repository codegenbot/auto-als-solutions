import sys

def parse_observations(observations):
    return list(map(float, observations.split()))

def choose_action(obs, step_counter, last_action):
    if step_counter >= 350:
        return 48  # Finish if 350 steps reached

    if obs[17] > 0.5:  # RadialPulseNonPalpable
        return cardiac_arrest_protocol(obs, last_action)

    if obs[25] < 0.5:  # UseSatsProbe not used
        return 19 if last_action != 19 else 25  # OpenBreathingDrawer or UseSatsProbe

    if obs[27] < 0.5:  # UseBloodPressureCuff not used
        return 20 if last_action != 20 else 27  # OpenCirculationDrawer or UseBloodPressureCuff

    if obs[46] > 0.5 and obs[-1] < 88:  # If sats measured and < 88%
        return 30  # UseNonRebreatherMask

    if obs[45] > 0.5 and obs[-2] < 60:  # If MAP measured and < 60
        return 15  # GiveFluids

    if obs[40] > 0.5 and obs[-7] < 8:  # If resp rate measured and < 8
        return 29  # UseBagValveMask

    if obs[39] > 0.5 and obs[-8] > 150:  # If heart rate measured and > 150
        return 9  # GiveAdenosine

    if not all(obs[i] > 0.5 for i in [3, 46, 40, 45]):  # If any assessment not done
        return next((i for i in [3, 4, 5, 6, 7] if obs[i] < 0.5), 16)  # Examine or ViewMonitor

    if (obs[3] > 0.5 and  # AirwayClear
        obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
        obs[40] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
        obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
        return 48  # Finish

    return 16 if last_action != 16 else 0  # ViewMonitor or DoNothing

def cardiac_arrest_protocol(obs, last_action):
    if obs[24] < 0.5:  # MonitorPads not used
        return 24  # UseMonitorPads
    if obs[28] < 0.5:  # DefibPads not attached
        return 28  # AttachDefibPads
    if last_action != 2:  # If we haven't just checked rhythm
        return 2  # CheckRhythm
    if obs[38] > 0.5:  # VF rhythm
        return 40 if last_action != 40 else 41  # DefibrillatorCharge or DefibrillatorSync
    if last_action != 17:  # If we're not already doing chest compressions
        return 17  # StartChestCompression
    if last_action != 10:  # If we haven't just given Adrenaline
        return 10  # GiveAdrenaline
    return 29  # UseBagValveMask

step_counter = 0
last_action = None
for line in sys.stdin:
    observations = parse_observations(line)
    action = choose_action(observations, step_counter, last_action)
    print(action)
    sys.stdout.flush()
    last_action = action
    step_counter += 1
    if action == 48:  # Finish
        break