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

        if event_observations[7] > 0:  # BreathingNone
            return print(actions.index("OpenAirwayDrawer"))

        if event_observations[3] < 1:  # AirwayClear
            return print(actions.index("ExamineAirway"))

        if min(vital_sign_values[5], 1) < 0.88:
            return print(actions.index("UseSatsProbe"))

        if min(vital_sign_values[6], 1) < 8:
            return print(actions.index("ExamineBreathing"))

        if event_observations[0] > 0 or event_observations[1] > 0 or event_observations[2] > 0:  # ResponseVerbal, ResponseGroan, ResponseNone
            return print(actions.index("CheckSignsOfLife"))

        if min(vital_sign_values[4], 1) < 60:
            return print(actions.index("ExamineCirculation"))

        if event_observations[20] > 0 or event_observations[21] > 0 or event_observations[22] > 0:  # AVPU_A, AVPU_U, AVPU_V
            return print(actions.index("ExamineDisability"))

        if event_observations[25] > 0 or event_observations[26] > 0 or event_observations[27] > 0:  # ExposureRash, ExposurePeripherallyShutdown,