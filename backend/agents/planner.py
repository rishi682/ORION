def create_plan(goal: str):

    goal = goal.lower()

    if "internship" in goal:
        return [
            "Search internship websites",
            "Open listings",
            "Extract internship details",
            "Generate report"
        ]

    return [
        "Understand goal",
        "Search information",
        "Generate report"
    ]