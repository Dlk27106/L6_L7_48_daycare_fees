
from daycare_fees import (
    extra_hours_fee,
    enrolment_allowed,
    pickup_status
)


# EXTRA HOURS FEE - BRANCH TESTS

def test_unknown_age_group():
    try:
        extra_hours_fee("school", 30, False)
        assert False
    except ValueError:
        assert True


def test_negative_hours():
    try:
        extra_hours_fee("toddler", -5, False)
        assert False
    except ValueError:
        assert True


def test_no_extra_hours():
    assert extra_hours_fee("toddler", 20, False) == 0


def test_infant_normal_extra_hours():
    assert extra_hours_fee("infant", 25, False) == 70


def test_toddler_normal_extra_hours():
    assert extra_hours_fee("toddler", 30, False) == 45


def test_infant_high_extra_hours():
    assert extra_hours_fee("infant", 45, False) == 550


def test_toddler_high_extra_hours():
    assert extra_hours_fee("toddler", 50, False) == 350


def test_toddler_sibling_hours():
    assert extra_hours_fee("toddler", 30, True) == 0


def test_infant_with_sibling():
    assert extra_hours_fee("infant", 25, True) == 70


# ENROLMENT - BRANCH TESTS

def test_immunisation_pending_age_allowed():
    assert enrolment_allowed(12, 0, True) is True


def test_immunisation_pending_age_not_allowed():
    assert enrolment_allowed(10, 2, True) is False


def test_age_below_six():
    assert enrolment_allowed(5, 2, False) is False


def test_age_at_least_six_with_vacancy():
    assert enrolment_allowed(24, 2, False) is True


def test_age_at_least_six_without_vacancy():
    assert enrolment_allowed(24, 0, False) is False


# PICKUP STATUS - BRANCH TESTS

def test_regular_pickup_on_time():
    assert pickup_status(10, False, False) == "on_time"


def test_regular_pickup_late():
    assert pickup_status(5, False, False) == "late"


def test_regular_pickup_overdue():
    assert pickup_status(-6, False, False) == "overdue"


def test_aftercare_pickup_on_time():
    assert pickup_status(20, True, False) == "on_time"


def test_aftercare_pickup_late():
    assert pickup_status(10, True, False) == "late"


def test_friday_pickup_on_time():
    assert pickup_status(30, False, True) == "on_time"


def test_friday_pickup_late():
    assert pickup_status(15, False, True) == "late"
