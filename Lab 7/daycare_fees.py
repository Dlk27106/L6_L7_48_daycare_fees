
import math


def parse_enrolment(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    if text.count(":") != 1:
        raise ValueError("Use age_group:hours format")

    age_group, hours = text.split(":")
    age_group = age_group.strip()

    if not age_group:
        raise ValueError("Age group cannot be empty")

    try:
        hours = float(hours)
    except ValueError:
        raise ValueError("Hours must be a number")

    if not math.isfinite(hours) or not 0 < hours <= 168:
        raise ValueError("Hours must be greater than 0 and at most 168")

    return age_group.title(), hours


def hours_average(hours_csv):
    if not isinstance(hours_csv, str):
        raise ValueError("Input must be a string")

    if not hours_csv.strip():
        raise ValueError("Hours list cannot be empty")

    try:
        values = [int(x.strip()) for x in hours_csv.split(",")]
    except ValueError:
        raise ValueError("Hours must contain valid integers")

    if any(x < 0 or x > 168 for x in values):
        raise ValueError("Hours must be between 0 and 168")

    return sum(values) // len(values)


def payable_fee(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string")

    if text.count("|") != 1:
        raise ValueError("Use fee|discount format")

    fee, discount = text.split("|")

    try:
        fee = float(fee)
        discount = float(discount)
    except ValueError:
        raise ValueError("Fee and discount must be numbers")

    if not math.isfinite(fee) or not math.isfinite(discount):
        raise ValueError("Fee and discount must be finite numbers")

    if fee < 0 or discount < 0:
        raise ValueError("Fee and discount cannot be negative")

    total = fee * 1.18 - discount
    return max(total, 0)


def main():
    print("==== Running parse_enrolment ====")
    user_input = input("Enter age group:hours (e.g. toddler:25): ")
    try:
        print("Age Group and Hours:", parse_enrolment(user_input))
    except ValueError as e:
        print("Invalid enrolment:", e)

    print("\n==== Running hours_average ====")
    user_input = input("Enter weekly hours as CSV (e.g. 20,25,30): ")
    try:
        print("Average Hours:", hours_average(user_input))
    except ValueError as e:
        print("Invalid hours:", e)

    print("\n==== Running payable_fee ====")
    user_input = input("Enter fee|discount (e.g. 3000|250): ")
    try:
        print("Payable Fee:", payable_fee(user_input))
    except ValueError as e:
        print("Invalid fee:", e)


if __name__ == "__main__":
    main()
