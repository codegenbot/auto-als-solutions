import math


def solve(observations):
    airway_events = observations[:33]
    vital_signs_events = observations[33:40]
    vital_signs_values = observations[40:]

    measured_sats = vital_signs_events[5] > 0 and vital_signs_values[5] or 0
    measured_map = vital_signs_events[4] > 0 and vital_signs_values[4] or 0
    if measured_sats < 65 or measured_map < 20:
        return 17

    airway_clear = airway_events[3] > 0
    airway_vomit = airway_events[4] > 0
    airway_blood = airway_events[5] > 0
    airway_tongue = airway_events[6] > 0
    if not airway_clear:
        if airway_vomit or airway_blood:
            return 31
        elif airway_tongue:
            return 32
        else:
            return 3

    breathing_none = airway_events[7] > 0
    breathing_snoring = airway_events[8] > 0
    breathing_seesaw = airway_events[9] > 0
    breathing_pneumothorax_symptoms = airway_events[14] > 0
    if breathing_none or breathing_seesaw or breathing_pneumothorax_symptoms:
        return 29
    elif breathing_snoring:
        return 36

    radial_pulse_palpable = airway_events[16] > 0
    radial_pulse_nonpalpable = airway_events[17] > 0
    if radial_pulse_nonpalpable:
        return 14

    exposure_stained_underwear = airway_events[27] > 0
    if exposure_stained_underwear:
        return 7

    measured_resp_rate = vital_signs_events[1] > 0 and vital_signs_values[1] or 0
    if measured_sats >= 88 and measured_resp_rate >= 8 and measured_map >= 60:
        return 48

    return 0