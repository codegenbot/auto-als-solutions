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

    if (obs[3] > 0.5 and  # AirwayClear
        obs[46] > 0.5 and obs[-1] >= 88 and  # Sats >= 88%
        obs[40] > 0.5 and obs[-7] >= 8 and  # RespRate >= 8
        obs[45] > 0.5 and obs[-2] >= 60):  # MAP >= 60
        return 48  # Finish

    return abcde_assessment(obs, last_action)

def cardiac_arrest_protocol(obs, last_action):
    if obs[24] < 0.5:  # MonitorPads not used
        return 24  # UseMonitorPads
    if obs[28] < 0.5:  # DefibPads not attached
        return 28  # AttachDefibPads
    if last_action != 2:
        return 2  # CheckRhythm
    if obs[38] > 0.5 or obs[32] > 0.5:  # VF or VT
        return 40  # DefibrillatorCharge
    if last_action == 40:
        return 41  # DefibrillatorCurrentUp
    if last_action == 41:
        return 17  # StartChestCompression
    if last_action == 17:
        return 29  # UseBagValveMask
    if last_action == 29:
        return 10  # GiveAdrenaline
    return 23  # ResumeCPR

def abcde_assessment(obs, last_action):
    airway_checked = max(obs[:7])
    breathing_checked = max(obs[7:16])
    circulation_checked = max(obs[16:21])
    disability_checked = max(obs[21:27])
    exposure_checked = max(obs[27:33])

    if airway_checked < 0.5:
        return 3  # ExamineAirway
    if breathing_checked < 0.5:
        return 4  # ExamineBreathing
    if circulation_checked < 0.5:
        return 5  # ExamineCirculation
    if disability_checked < 0.5:
        return 6  # ExamineDisability
    if exposure_checked < 0.5:
        return 7  # ExamineExposure

    return 16 if last_action != 16 else 0  # ViewMonitor or DoNothing

step_counter = 