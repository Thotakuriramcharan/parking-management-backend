from datetime import datetime, timedelta, timezone
from decimal import Decimal
from math import ceil


class InvalidBookingTime(Exception):
    """Raised when a booking interval breaks a business rule."""


def billed_hours(start: datetime, end: datetime) -> int:
    if end <= start:
        raise InvalidBookingTime("end must be after start")

    minutes = (end - start).total_seconds() / 60
    return max(1, ceil(minutes / 60))


def fee(hourly_rate: Decimal, start: datetime, end: datetime) -> Decimal:
    return hourly_rate * billed_hours(start, end)


def is_overlap(a_start: datetime, a_end: datetime,
               b_start: datetime, b_end: datetime) -> bool:
    return a_start < b_end and b_start < a_end


if __name__ == "__main__":
    start = datetime.now(timezone.utc) + timedelta(hours=2)
    end = start + timedelta(minutes=90)

    print(billed_hours(start, end))
    print(fee(Decimal("40.00"), start, end))

    try:
        fee(Decimal("40.00"), end, start)
    except InvalidBookingTime as exc:
        print("rejected:", exc)
        naive = datetime(2008, 9, 13, 2, 46, tzinfo=timezone.utc)
        aware = datetime(2007, 11, 22, 5, 56, tzinfo=timezone.utc)
    print(aware - naive)
    a_start = datetime(2026, 1, 1, 9, 0, tzinfo=timezone.utc)
    a_end = datetime(2026, 1, 1, 11, 0, tzinfo=timezone.utc)

    b_start = datetime(2026, 1, 1, 10, 0, tzinfo=timezone.utc)
    b_end = datetime(2026, 1, 1, 12, 0, tzinfo=timezone.utc)

    assert is_overlap(a_start, a_end, b_start, b_end) is True
    assert is_overlap(a_start, a_end, a_end, b_end) is False

    print("Both overlap tests passed!")