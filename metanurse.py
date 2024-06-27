import math

def solve(observations):
    airway_events = observations[:33]
    vital_signs_events = observations[33:40]
    vital_signs_values = observations[40:]
    
    airway_clear = airway_events[3] > 0
    airway_vomit = airway_events[4] > 0
    airway_blood = airway_events[5] > 0
    airway_tongue = airway_events[6] > 0
    
    breathing_none = airway_events[7] > 0
    breathing_snoring = airway_events[8] > 0
    breathing_seesaw = airway_events[9] > 0
    breathing_equal_expansion = airway_events[10] > 0
    breathing_bibasal_crepitations = airway_events[11] > 0
    breathing_wheeze = airway_events[12] > 0
    breathing_coarse_crepitations = airway_events[13] > 0
    breathing_pneumothorax_symptoms = airway_events[14] > 0
    
    ventilation_resistance = airway_events[15] > 0
    
    radial_pulse_palpable = airway_events[16] > 0
    radial_pulse_nonpalpable = airway_events[17] > 0
    
    heart_sounds_muffled = airway_events[18] > 0
    heart_sounds_normal = airway_events[19] > 0
    
    avpu_a = airway_events[20] > 0
    avpu_u = airway_events[21] > 0
    avpu_v = airway_events[22] > 0
    
    pupils_pinpoint = airway_events[23] > 0
    pupils_normal = airway_events[24] > 0
    
    exposure_rash = airway_events[25] > 0
    exposure_peripherally_shutdown = airway_events[26] > 0
    exposure_stained_underwear = airway_events[27] > 0
    
    heart_rhythm_nsr = airway_events[28] > 0
    heart_rhythm_svt = airway_events[29] > 0
    heart_rhythm_af = airway_events[30] > 0
    heart_rhythm_atrial_flutter = airway_events[31] > 0
    heart_rhythm_vt = airway_events[32] > 0
    
    measured_heart_rate = vital_signs_events[0] > 0 and vital_signs_values[0] or 0
    measured_resp_rate = vital_signs_events[1] > 0 and vital_signs_values[1] or 0
    measured_capillary_glucose = vital_signs_events[2] > 0 and vital_signs_values[2] or 0
    measured_temperature = vital_signs_events[3] > 0 and vital_signs_values[3] or 0
    measured_map = vital_signs_events[4] > 0 and vital_signs_values[4] or 0
    measured_sats = vital_signs_events[5] > 0 and vital_signs_values[5] or 0
    measured_resps = vital_signs_events[6] > 0 and vital_signs_values[6] or 0
    
    if measured_sats < 65 or measured_map < 20:
        return 17 # StartChestCompression
    
    if not airway_clear:
        if airway_vomit:
            return 31 # UseYankeurSucionCatheter
        if airway_blood:
            return 31 # UseYankeurSucionCatheter
        if airway_tongue:
            return 32 # UseGuedelAirway
        return 3 # ExamineAirway
    
    if breathing_none or breathing_seesaw or breathing_pneumothorax_symptoms:
        return 29 # UseBagValveMask
    
    if breathing_snoring:
        return 36 #