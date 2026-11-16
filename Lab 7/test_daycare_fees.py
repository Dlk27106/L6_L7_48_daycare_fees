
import math
from hypothesis import given, strategies as st

from daycare_fees import (
    parse_enrolment,
    hours_average,
    payable_fee
)


# Test 1: Enrolment parser
@given(
    st.sampled_from(["Toddler", "Infant", "Preschool"]),
    st.floats(min_value=0.01, max_value=168,
              allow_nan=False, allow_infinity=False)
)
def test_parse_enrolment_valid(age, hours):
    result = parse_enrolment(f"{age}:{hours}")
    assert result[0] == age.title()
    assert result[1] == hours


@given(st.text() | st.none())
def test_parse_enrolment_handles_invalid_input(s):
    try:
        result = parse_enrolment(s)
        assert isinstance(result, tuple)
    except ValueError:
        pass


# Test 2: Weekly hours average
@given(st.lists(
    st.integers(min_value=0, max_value=168),
    min_size=1
))
def test_hours_average_valid(values):
    csv = ",".join(map(str, values))
    expected = sum(values) // len(values)
    assert hours_average(csv) == expected


@given(st.text() | st.none())
def test_hours_average_handles_invalid_input(s):
    try:
        result = hours_average(s)
        assert isinstance(result, int)
    except ValueError:
        pass


# Test 3: Payable fee
@given(
    st.floats(min_value=0, max_value=100000,
              allow_nan=False, allow_infinity=False),
    st.floats(min_value=0, max_value=100000,
              allow_nan=False, allow_infinity=False)
)
def test_payable_fee_valid(fee, discount):
    result = payable_fee(f"{fee}|{discount}")
    assert result == max(fee * 1.18 - discount, 0)


@given(st.text() | st.none())
def test_payable_fee_handles_invalid_input(s):
    try:
        result = payable_fee(s)
        assert isinstance(result, float)
        assert math.isfinite(result)
    except ValueError:
        pass
