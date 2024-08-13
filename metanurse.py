import sys

def stabilize():
    max_steps = 350

    def update_vitals(observations):
        events = observations[:33]
        vital_signs_times = observations[33:40]
        vital_signs_values = observations[40:]
        vitals = {}
        for idx, value in enumerate(vital_signs_values):
            if vital_signs_times[idx] > 0:
                vitals[idx] = value
        return events, vitals

    def perform_examinations(exams_done):
        examinations = [3, 4, 5, 6, 7, 8, 2]
        for exam in examinations:
            if exam not in exams_done:
                exams_done.add(exam)
                return exam
        return None

    def check_critical_conditions(vitals):
        if vitals.get(4) is not None and vitals[4] < 20:
            return 17
        if vitals.get(5) is not None and vitals[5] < 65:
            return 22
        return None

    actions_taken = set()
    exams_done = set()

    for step in range(max_steps):
        observations = list(map(float, input().strip().split()))
        events, vitals = update_vitals(observations)

        critical_action = check_critical_conditions(vitals)
        if critical_action:
            print(critical_action)
            return

        exam_action = perform_examinations(exams_done)
        if exam_action:
            print(exam_action)
            continue

        if events[29] > 0 or events[30] > 0:
            print(40)  # Charge defibrillator
            return

        if vitals.get(4) is not None and vitals[4] < 60:
            print(15)  # Give fluids
            return
        if vitals.get(5) is not None and vitals[5] < 88:
            print(30)  # Use non-rebreather mask
            return
        if vitals.get(1) is not None and vitals[1] < 8:
            print(29)  # Use bag-valve mask
            return

        if all(vitals.get(i) is not None and vitals[i] >= thresh for i, thresh in zip([5, 1, 4], [88, 8, 60])):
            print(48)  # Finish
            return

    print(48)  # Finish
    return

if __name__ == "__main__":
    stabilize()