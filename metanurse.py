import sys

ACTIONS = {name: num for num, name in enumerate([
    "DoNothing", "CheckSignsOfLife", "CheckRhythm", "ExamineAirway", "ExamineBreathing", "ExamineCirculation", 
    "ExamineDisability", "ExamineExposure", "ExamineResponse",  "GiveAdenosine", "GiveAdrenaline", 
    "GiveAmiodarone", "GiveAtropine", "GiveMidazolam", "UseVenflonIVCatheter", "GiveFluids", "ViewMonitor", 
    "StartChestCompression", "OpenAirwayDrawer","OpenBreathingDrawer","OpenCirculationDrawer","OpenDrugsDrawer", 
    "BagDuringCPR", "ResumeCPR", "UseMonitorPads", "UseSatsProbe", "UseAline", "UseBloodPressureCuff", 
    "AttachDefibPads", "UseBagValveMask", "UseNonRebreatherMask", "UseYankeurSucionCatheter", "UseGuedelAirway", 
    "TakeBloodForArtherialBloodGas", "TakeRoutineBloods", "PerformAirwayManoeuvres", "PerformHeadTiltChinLift", 
    "PerformJawThrust", "TakeBloodPressure", "TurnOnDefibrillator", "DefibrillatorCharge", 
    "DefibrillatorCurrentUp", "DefibrillatorCurrentDown", "DefibrillatorPace", "DefibrillatorPacePause", 
    "DefibrillatorRateUp", "DefibrillatorRateDown", "DefibrillatorSync", "Finish"])}

SEQUENCE = [
    ACTIONS["UseSatsProbe"],
    ACTIONS["UseBloodPressureCuff"],
    ACTIONS["ViewMonitor"],
]

def stabilize_patient(observations):
    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None
    
    return events, heart_rate, resp_rate, map_value, sats

def get_critical_action(resp_rate, sats, map_value):
    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return ACTIONS["StartChestCompression"]
    if resp_rate is not None and resp_rate < 8:
        return ACTIONS["UseBagValveMask"]
    if sats is not None and sats < 88:
        return ACTIONS["UseNonRebreatherMask"]
    if map_value is not None and map_value < 60:
        return ACTIONS["GiveFluids"]
    return None

def get_action(observations, step):
    events, heart_rate, resp_rate, map_value, sats = stabilize_patient(observations)

    if step < len(SEQUENCE):
        return SEQUENCE[step]
    
    critical_action = get_critical_action(resp_rate, sats, map_value)
    if critical_action:
        return critical_action
    
    return ACTIONS["ViewMonitor"] if step % 10 < 3 else (ACTIONS["ExamineAirway"] if step % 10 < 6 else ACTIONS["ExamineBreathing"])

step = 0
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data, step)
    print(action)
    if action == ACTIONS["Finish"]:
        break
    step += 1