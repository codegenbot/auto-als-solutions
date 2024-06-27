import math

def advanced_life_support(observations):
    actions = [
        "DoNothing",
        "CheckSignsOfLife",
        "CheckRhythm",
        "ExamineAirway",
        "ExamineBreathing",
        "ExamineCirculation",
        "ExamineDisability",
        "ExamineExposure",
        "ExamineResponse",
        "GiveAdenosine",
        "GiveAdrenaline",
        "GiveAmiodarone",
        "GiveAtropine",
        "GiveMidazolam",
        "UseVenflonIVCatheter",
        "GiveFluids",
        "ViewMonitor",
        "StartChestCompression",
        "OpenAirwayDrawer",
        "OpenBreathingDrawer",
        "OpenCirculationDrawer",
        "OpenDrugsDrawer",
        "BagDuringCPR",
        "ResumeCPR",
        "UseMonitorPads",
        "UseSatsProbe",
        "UseAline",
        "UseBloodPressureCuff",
        "AttachDefibPads",
        "UseBagValveMask",
        "UseNonRebreatherMask",
        "UseYankeurSucionCatheter",
        "UseGuedelAirway",
        "TakeBloodForArtherialBloodGas",
        "TakeRoutineBloods",
        "PerformAirwayManoeuvres",
        "PerformHeadTiltChinLift",
        "PerformJawThrust",
        "TakeBloodPressure",
        "TurnOnDefibrillator",
        "DefibrillatorCharge",
        "DefibrillatorCurrentUp",
        "DefibrillatorCurrentDown",
        "DefibrillatorPace",
        "DefibrillatorPacePause",
        "DefibrillatorRateUp",
        "DefibrillatorRateDown",
        "DefibrillatorSync",
        "Finish"
    ]

    observations = [float(x) for x in observations.split()]
    event_observations = observations[:33]
    vital_sign_observations = observations[33:40]
    vital_sign_values = observations[40:]

    step = 0
    while step < 350:
        if max(vital_sign_observations[5], 0) < 0.65 or max(vital_sign_observations[6], 0) < 20:
            return print(actions.index("StartChestCompression"))

        if min(vital_sign_values[5], 1) < 0.88 or min(vital_sign_values[6], 1) < 8:
            if event_observations[3] > 0:  # AirwayClear
                return print(actions.index("ExamineBreathing"))
            else:
                return print(actions.index("ExamineAirway"))

        if event_observations[7] > 0:  # BreathingNone
            return print(actions.index("ExamineResponse"))

        if event_observations[0] > 0:  # ResponseVerbal
            return print(actions.index("CheckSignsOfLife"))

        if event_observations[1] > 0:  # ResponseGroan
            return print(actions.index("CheckSignsOfLife"))

        if event_observations[2] > 0:  # ResponseNone
            return print(actions.index("CheckSignsOfLife"))

        if min(vital_sign_values[4], 1) < 60:
            return print(actions.index("ExamineCirculation"))

        step += 1

    return print(actions.index("Finish"))

while True:
    observations = input()
    advanced_life_support(observations)