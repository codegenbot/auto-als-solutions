import sys

def main():
    has_used_sats_probe = False
    has_used_bp_cuff = False

    for _ in range(350):
        observations = list(map(float, input().split()))

        ResponseVerbal = observations[0]
        AirwayClear = observations[3]
        BreathingNone = observations[7]
        BreathingSnoring = observations[8]
        BreathingSeeSaw = observations[9]
        MeasuredRespRate = observations[39+1]
        MeasuredMAP = observations[39+4]
        MeasuredSats = observations[39+5]
        RespRate = observations[39+1+7]
        MAP = observations[39+4+7]
        Sats = observations[39+5+7]

        if BreathingNone > 0:
            print(35)
        elif AirwayClear == 0:
            print(3)
        elif MeasuredSats and Sats < 65:
            print(17)
        elif MeasuredMAP and MAP < 20:
            print(17)
        elif not has_used_sats_probe:
            has_used_sats_probe = True
            print(25)
        elif not has_used_bp_cuff:
            has_used_bp_cuff = True
            print(27)
        elif MeasuredRespRate == 0:
            print(4)
        elif MeasuredRespRate and RespRate < 8:
            print(29)
        elif MeasuredSats and Sats < 88:
            print(30)
        elif MeasuredMAP and MAP < 60:
            print(15)
        else:
            print(0)

    print(48)

if __name__ == "__main__":
    main()