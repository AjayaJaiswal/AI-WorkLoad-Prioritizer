def calculate_score(task):
    deadline = task["deadline"]
    time_needed = task["time"]
    difficulty = task["difficulty"]
    weight = task["weight"]

    if deadline == 0:
        urgency = 10
    elif deadline == 1:
        urgency = 9
    elif deadline <= 3:
        urgency = 7
    elif deadline <= 7:
        urgency = 5
    else:
        urgency = 2

    workload = min(time_needed, 10)

    overload_penalty = 0
    if deadline <= 2 and time_needed >= 5:
        overload_penalty = 5

    score = (
        (urgency * 4)
        + (weight * 3)
        + (difficulty * 2)
        + (workload * 2)
        + overload_penalty
    )
    return score


def calculate_risk(task):
    score = task["score"]
    deadline = task["deadline"]
    time_needed = task["time"]

    if deadline <= 1 and time_needed >= 4:
        return "HIGH"
    if score >= 75:
        return "HIGH"
    if score >= 50:
        return "MEDIUM"
    return "LOW"


def get_recommendation(risk):
    if risk == "HIGH":
        return "Start immediately"
    if risk == "MEDIUM":
        return "Work soon"
    return "Work later"


def get_reason(task):
    if task["deadline"] <= 1:
        return "Very close deadline"
    if task["time"] >= 5:
        return "Heavy workload"
    if task["weight"] >= 8:
        return "High academic importance"
    if task["difficulty"] >= 8:
        return "High difficulty"
    return "Balanced workload"