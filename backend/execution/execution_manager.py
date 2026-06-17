def execute_plan(plan):

    logs = []

    for step in plan:
        log = f"Executing: {step}"
        print(log)
        logs.append(log)

    return logs