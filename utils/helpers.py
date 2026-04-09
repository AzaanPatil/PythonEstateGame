def format_currency(amount):
    return f"${amount:,}"


def clamp(value, minimum, maximum):
    return max(minimum, min(maximum, value))
