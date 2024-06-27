import sys

input = sys.stdin.read
data = input().split()

# Extract observations
observations = list(map(float, data))

# Constants for indices in the observations array
MEASURED_MAP = 43  # Index for measured MAP relevance
MEASURED_SATS = 44  # Index for measured oxygen saturation relevance
MEASURED_RESPS = 45  # Index for measured respiratory rate relevance

VALUE_MAP = 46  # Index for actual MAP value
VALUE_SATS = 47  # Index for actual oxygen saturation value
VALUE_RESPS = 48  # Index for actual respiratory rate value

# Constants for action codes
FINISH = 48
EXAMINE_AIRWAY = 3
EXAMINE_BREATHING = 4
EXAMINE_CIRCULATION = 5
USE_NON_REBREATHER_MASK = 30
USE_BLOOD_PRESSURE_CUFF = 27
USE_SATS_PROBE = 25

# Check patient's vitals and decide on actions
if observations[MEASURED_MAP] > 0:
    if observations[VALUE_MAP] < 20:
        print(FINISH)  # Critical low MAP, finish for intervention
    elif observations[VALUE_MAP] < 60:
        print(USE_BLOOD_PRESSURE_CUFF)  # Use cuff to monitor and stabilize MAP
    else:
        print(EXAMINE_CIRCULATION)
else:
    print(USE_BLOOD_PRESSURE_CUFF)  # No recent MAP data, attach cuff to measure

if observations[MEASURED_SATS] > 0:
    if observations[VALUE_SATS] < 65:
        print(FINISH)  # Critical low sats, finish for immediate intervention
    elif observations[VALUE_SATS] < 88:
        print(USE_NON_REBREATHER_MASK)  # Provide high-flow oxygen
else:
    print(USE_SATS_PROBE)  # No recent sats data, use probe to measure

if observations[MEASURED_RESPS] > 0:
    if observations[VALUE_RESPS] < 8:
        print(
            USE_NON_REBREATHER_MASK
        )  # Insufficient respiratory rate, assist breathing
    else:
        print(EXAMINE_BREATHING)
else:
    print(EXAMINE_BREATHING)  # No recent respiration data, examine breathing

# If no critical interventions are needed beyond simple checks
print(FINISH)