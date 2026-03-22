def calculate_score(task):
    # --- Extract task attributes ---
    deadline = task["deadline"]
    time_needed = task["time"]
    difficulty = task["difficulty"]
    weight = task["weight"]

    # --- Convert deadline into urgency score ---
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

    # --- Cap workload to avoid extreme values ---
    workload = min(time_needed, 10)

    # --- Penalize tasks with tight deadline + heavy workload ---
    overload_penalty = 0
    if deadline <= 2 and time_needed >= 5:
        overload_penalty = 5

    # --- Final weighted scoring formula ---
    score = (
        (urgency * 4)      # most important factor
        + (weight * 3)     # importance
        + (difficulty * 2) # effort level
        + (workload * 2)   # time required
        + overload_penalty # extra risk factor
    )

    return score


def calculate_risk(task):
    # --- Use score + conditions to classify risk ---
    score = task["score"]
    deadline = task["deadline"]
    time_needed = task["time"]

    # Immediate danger condition
    if deadline <= 1 and time_needed >= 4:
        return "HIGH"

    # Score-based thresholds
    if score >= 75:
        return "HIGH"
    if score >= 50:
        return "MEDIUM"

    return "LOW"


def get_recommendation(risk):
    # --- Map risk level to action ---
    if risk == "HIGH":
        return "Start immediately"
    if risk == "MEDIUM":
        return "Work soon"
    return "Work later"


def get_reason(task):
    # --- Explain why task is prioritized ---
    if task["deadline"] <= 1:
        return "Very close deadline"
    if task["time"] >= 5:
        return "Heavy workload"
    if task["weight"] >= 8:
        return "High academic importance"
    if task["difficulty"] >= 8:
        return "High difficulty"

    return "Balanced workload"