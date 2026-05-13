def get_status(score):
    return "excellent" if score >= 90 else "good" if score >= 70 else "average" if score > 55 else "fail" if score < 55 else "unknown"


def is_valid_age(age):
    if not isinstance(age, int):
        return  False
    return 0 < age < 120


def get_greeting(hour):
    return "Good morning" if 5 <= hour < 12 else "Good afternoon" if 12 <= hour < 17 else "Geed evening" if 17 <= hour < 21 else "Good night"
