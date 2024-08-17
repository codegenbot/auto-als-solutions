import sys

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
    "Finish": 48
}

def stabilize():
    def take_action(action):
        print(action)
        sys.stdout.flush()

    steps, examined = 350, set()
    for step in range(steps):
        try:
            observations = list(map(float, input().strip().split()))
        except:
            take_action(ACTIONS["Finish"])
            return

        if len(observations) != 53:
            take_action(ACTIONS["DoNothing"])
            continue
        
        events = observations[:33]
        measuring_times = observations[33:40]
        measurements = observations[46:]

        vitals = ["HeartRate", "RespRate", "Glucose", "Temp", "MAP", "Sats", "Resps"]
        vitals_dict = {vitals[i]: measurements[i] if measuring_times[i] > 0 else None for i in range(7)}

        if (vitals_dict["Sats"] is not None and vitals_dict["Sats"] < 65) or (vitals_dict["MAP"] is not None and vitals_dict["MAP"] < 20):
            take_action(ACTIONS["StartChestCompression"])
            continue
        
        if "Airway" not in examined:
            take_action(ACTIONS["ExamineAirway"])
            examined.add("Airway")
            continue
        
        if "Sats" not in examined and vitals_dict["Sats"] is None:
            take_action(ACTIONS["UseSatsProbe"])
            examined.add("Sats")
            continue
        
        if "MAP" not in examined and vitals_dict["MAP"] is None:
            take_action(ACTIONS["UseBloodPressureCuff"])
            examined.add("MAP")
            continue
        
        if "Breathing" not in examined:
            take_action(ACTIONS["ExamineBreathing"])
            examined.add("Breathing")
            continue
        
        if vitals_dict["Sats"] is not None and vitals_dict["Sats"] < 88:
            take_action(ACTIONS["UseNonRebreatherMask"])
            continue
        
        if vitals_dict["RespRate"] is not None and vitals_dict["RespRate"] < 8:
            take_action(ACTIONS["UseBagValveMask"])
            continue

        if vitals_dict["MAP"] is not None and vitals_dict["MAP"] < 60:
            take_action(ACTIONS["GiveFluids"])
            continue

        take_action(ACTIONS["Finish"])
        break
    else:
        take_action(ACTIONS["Finish"])

if __name__ == "__main__":
    stabilize()