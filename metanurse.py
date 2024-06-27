import math

def advanced_life_support():
    observations = input().split()
    observations = [float(x) for x in observations]
    
    for _ in range(350):
        # Airway
        if observations[3] == 0 and observations[4] == 0 and observations[5] == 0 and observations[6] == 0:
            print(3)  # ExamineAirway
        elif observations[7] > 0 or observations[8] > 0 or observations[9] > 0:
            print(35)  # PerformAirwayManoeuvres
            print(36)  # PerformHeadTiltChinLift
            print(37)  # PerformJawThrust
            print(31)  # UseYankeurSucionCatheter
            print(32)  # UseGuedelAirway
        
        # Breathing
        elif observations[10] == 0 and observations[11] == 0 and observations[12] == 0 and observations[13] == 0 and observations[14] == 0 and observations[15] == 0:
            print(4)  # ExamineBreathing
        elif observations[49] < 8:
            print(29)  # UseBagValveMask
            print(22)  # BagDuringCPR
        elif observations[48] < 88:
            print(30)  # UseNonRebreatherMask
        
        # Circulation
        elif observations[16] == 0 and observations[17] > 0 or observations[18] > 0 or observations[19] == 0 or observations[20] > 0 or observations[21] > 0 or observations[22] > 0 or observations[23] > 0 or observations[24] == 0 or observations[25] > 0 or observations[26] > 0 or observations[27] > 0 or observations[28] > 0 or observations[29] > 0 or observations[30] > 0 or observations[31] > 0 or observations[32] > 0 or observations[33] > 0 or observations[34] > 0 or observations[35] > 0 or observations[36] > 0:
            print(5)  # ExamineCirculation
        elif observations[50] < 60:
            print(14)  # UseVenflonIVCatheter
            print(15)  # GiveFluids
        elif observations[51] < 65 or observations[50] < 20:
            print(17)  # StartChestCompression
            print(10)  # GiveAdrenaline
        
        # Disability
        elif observations[21] == 0 and observations[22] > 0 and observations[23] == 0:
            print(6)  # ExamineDisability
        elif observations[47] == 0:
            print(33)  # TakeBloodForArtherialBloodGas
        
        # Exposure
        elif observations[25] > 0 or observations[26] > 0 or observations[27] > 0:
            print(7)  # ExamineExposure
        
        # Rhythm
        elif observations[28] > 0 or observations[29] > 0 or observations[30] > 0 or observations[31] > 0 or observations[32] > 0 or observations[33] > 0 or observations[34] > 0 or observations[35] > 0 or observations[36] > 0 or observations[37] > 0:
            print(2)  # CheckRhythm
            if observations[29] > 0:
                print(9)  # GiveAdenosine
            elif observations[30] > 0 or observations[31] > 0:
                print(11)  # GiveAmiodarone
            elif observations[32] > 0:
                print(12)  # GiveAtropine
            elif observations[37] > 0:
                print(13)  # GiveMidazolam
        
        # Response
        elif observations[