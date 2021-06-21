def getDropOffReason(reason_type):
    if reason_type.lower() == "remote":
        return [
            "Lack of Equipment",
            "Unhappy About Remote Learning",
            "Feel alone",
            "Helpless when remote",
            "Prof not prepared"
        ]
    else:
        return [
            "Tuition Expensive",
            "Academically Unprepared",
            "Unhappy with The School",
            "Lack of Value",
            "Uncertainty About Future"
        ]