import sys

ACTIONS = {0: "DoNothing", 1: "CheckSignsOfLife", 2: "CheckRhythm", 3: "ExamineAirway", 4: "ExamineBreathing", 5: "ExamineCirculation", 
           6: "ExamineDisability", 7: "ExamineExposure", 8: "ExamineResponse", 9: "GiveAdenosine", 10: "GiveAdrenaline", 11: "GiveAmiodarone",
           12: "GiveAtropine", 13: "GiveMidazolam", 14: "UseVenflonIVCatheter", 15: "GiveFluids", 16: "ViewMonitor", 17: "StartChestCompression",
           18: "OpenAirwayDrawer", 19: "OpenBreathingDrawer", 20: "OpenCirculationDrawer", 21: "OpenDrugsDrawer", 22: "BagDuringCPR", 
           23: "ResumeCPR", 24: "UseMonitorPads", 25: "UseSatsProbe", 26: "UseAline", 27: "UseBloodPressureCuff", 28: "AttachDefibPads", 
           29: "UseBagValveMask", 30: "UseNonRebreatherMask", 31: "UseYankeurSucionCatheter", 32: "UseGuedelAirway", 33: "TakeBloodForArterialBloodGas", 
           34: "TakeRoutineBloods", 35: "PerformAirwayManoeuvres", 36: "PerformHeadTiltChinLift", 37: "PerformJawThrust", 38: "TakeBloodPressure", 
           39: "TurnOnDefibrillator", 40: "DefibrillatorCharge", 41: "DefibrillatorCurrentUp", 42: "DefibrillatorCurrentDown", 43: "DefibrillatorPace",
           44: "DefibrillatorPacePause", 45: "DefibrillatorRateUp", 46: "DefibrillatorRateDown", 47: "DefibrillatorSync", 48: "Finish"}

SEQUENCE = [25, 27, 16, 3, 4, 5]

def get_vital_signs(observations):
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    return heart_rate, resp_rate, map_value, sats

def stabilize_patient(observations):
    events, heart_rate, resp_rate, map_value, sats = observations[:33], *get_vital_signs(observations)
    critical_action = None

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return ACTIONS[17]

    if events[3] == 0:  # Airway not clear
        if events[4]:  # Airway vomit
            return ACTIONS[31]
        if events[5] or events[6]:  # Airway blood or tongue obstruction
            return ACTIONS[37]
        return ACTIONS[3]

    if resp_rate is not None:
        if resp_rate < 8:
            return ACTIONS[29]
    if sats is not None:
        if sats < 88:
            return ACTIONS[30]
        if map_value is not None and map_value < 60:
            return ACTIONS[15]

    if map_value is not None and resp_rate is not None and sats is not None and map_value >= 60 and resp_rate >= 8 and sats >= 88:
        return ACTIONS[48]

    return ACTIONS[0]

step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    if step < len(SEQUENCE):
        action = SEQUENCE[step]
    else:
        action = stabilize_patient(input_data)
    print(action)
    if action == ACTIONS[48]:
        break
    step += 1