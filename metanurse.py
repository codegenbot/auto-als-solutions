import sys

def main():
    for _ in range(350):
        observations = list(map(float, input().split()))

        # Extracting the relevant measurements and events
        ResponseVerbal         = observations[0]
        AirwayClear            = observations[3]
        BreathingNone          = observations[7]
        BreathingSnoring       = observations[8]
        BreathingSeeSaw        = observations[9]
        MeasuredRespRate       = observations[39+1]
        MeasuredMAP            = observations[39+4]
        MeasuredSats           = observations[39+5]
        RespRate               = observations[39+1+7]
        MAP                    = observations[39+4+7]
        Sats                   = observations[39+5+7]

        if BreathingNone > 0:  # If the patient has stopped breathing, clear airway first
            print(35)  # PerformAirwayManoeuvres
        elif AirwayClear == 0:  # Ensure airway is clear
            print(3)  # ExamineAirway
        elif MeasuredSats and Sats < 65:  # Critical Sats
            print(17)  # StartChestCompression
        elif MeasuredMAP and MAP < 20:  # Critical MAP
            print(17)  # StartChestCompression
        elif MeasuredSats == 0:  # Attach Sats Probe if not used
            print(25)  # UseSatsProbe
        elif MeasuredMAP == 0:  # Attach Blood Pressure Cuff if not used
            print(27)  # UseBloodPressureCuff
        elif MeasuredRespRate == 0:  # Examine Breathing if RespRate not measured
            print(4)  # ExamineBreathing
        elif MeasuredRespRate and RespRate < 8:  # Use BVM if RespRate low
            print(29)  # UseBagValveMask
        elif MeasuredSats and Sats < 88:  # Use Non-rebreather mask if Sats low
            print(30)  # UseNonRebreatherMask
        elif MeasuredMAP and MAP < 60:  # Give fluids if MAP is low
            print(15)  # GiveFluids
        else:
            print(0)  # DoNothing

    print(48)  # Finish

if __name__ == "__main__":
    main()