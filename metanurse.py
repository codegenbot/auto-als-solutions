import sys

# Define constants for actions
ACTIONS = {
    "DoNothing": 0,
    "CheckSignsOfLife": 1,
    "CheckRhythm": 2,
    "ExamineAirway": 3,
    "ExamineBreathing": 4,
    "ExamineCirculation": 5,
    "ExamineDisability": 6,
    "ExamineExposure": 7,
    "ExamineResponse": 8,
    "GiveAdenosine": 9,
    "GiveAdrenaline": 10,
    "GiveAmiodarone": 11,
    "GiveAtropine": 12,
    "GiveMidazolam": 13,
    "UseVenflonIVCatheter": 14,
    "GiveFluids": 15,
    "ViewMonitor": 16,
    "StartChestCompression": 17,
    "OpenAirwayDrawer": 18,
    "OpenBreathingDrawer": 19,
    "OpenCirculationDrawer": 20,
    "OpenDrugsDrawer": 21,
    "BagDuringCPR": 22,
    "ResumeCPR": 23,
    "UseMonitorPads": 24,
    "UseSatsProbe": 25,
    "UseAline": 26,
    "UseBloodPressureCuff": 27,
    "AttachDefibPads": 28,
    "UseBagValveMask": 29,
    "UseNonRebreatherMask": 30,
    "UseYankeurSucionCatheter": 31,
    "UseGuedelAirway": 32,
    "TakeBloodForArtherialBloodGas": 33,
    "TakeRoutineBloods": 34,
    "PerformAirwayManoeuvres": 35,
    "PerformHeadTiltChinLift": 36,
    "PerformJawThrust": 37,
    "TakeBloodPressure": 38,
    "TurnOnDefibrillator": 39,
    "DefibrillatorCharge": 40,
    "DefibrillatorCurrentUp": 41,
    "DefibrillatorCurrentDown": 42,
    "DefibrillatorPace": 43,
    "DefibrillatorPacePause": 44,
    "DefibrillatorRateUp": 45,
    "DefibrillatorRateDown": 46,
    "DefibrillatorSync": 47,
    "Finish": 48,
}


def get_action(observations):
    global step, evaluations
    step += 1

    events = observations[:33]
    vital_signs_time = observations[33:40]
    vital_signs_values = observations[40:]

    heart_rate = vital_signs_values[0] if vital_signs_time[0] > 0 else None
    resp_rate = vital_signs_values[1] if vital_signs_time[1] > 0 else None
    map_value = vital_signs_values[4] if vital_signs_time[4] > 0 else None
    sats = vital_signs_values[5] if vital_signs_time[5] > 0 else None

    if step == 1:
        return ACTIONS["UseSatsProbe"]
    if step == 2:
        return ACTIONS["UseBloodPressureCuff"]
    if step == 3:
        return ACTIONS["ViewMonitor"]

    if (sats is not None and sats < 65) or (map_value is not None and map_value < 20):
        return ACTIONS["StartChestCompression"]

    if step < 10:
        for eval in evaluations:
            if eval == "A" and events[3] == 0:
                evaluations.remove("A")
                return ACTIONS["ExamineAirway"]
            elif eval == "B" and (resp_rate is None or resp_rate < 8):
                evaluations.remove("B")
                if resp_rate is None:
                    return ACTIONS["ExamineBreathing"]
                return ACTIONS["UseBagValveMask"]
            elif eval == "C" and (map_value is None or map_value < 60):
                evaluations.remove("C")
                if map_value is None:
                    return ACTIONS["ViewMonitor"]
                return ACTIONS["GiveFluids"]

    if resp_rate is None or map_value is None or sats is None:
        if resp_rate is None:
            return ACTIONS["ExamineBreathing"]
        if map_value is None:
            return ACTIONS["UseBloodPressureCuff"]
        if sats is None:
            return ACTIONS["UseSatsProbe"]

    if map_value >= 60 and resp_rate >= 8 and sats >= 88:
        return ACTIONS["Finish"]

    return ACTIONS["DoNothing"]


global step, evaluations
step = 0
evaluations = ["A", "B", "C", "D", "E"]
for _ in range(350):
    input_data = list(map(float, input().strip().split()))
    action = get_action(input_data)
    print(action)
    if action == ACTIONS["Finish"]:
        break