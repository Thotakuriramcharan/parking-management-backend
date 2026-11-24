# Scope - Smart Parking Management System (Backend API)

## Actors

- **USER:** Books parking slots.
- **ADMIN:** Manages parking lots and parking slots.

## Features in Scope

- User registration and login using JWT authentication.
- Parking lot and parking slot management.
- Search for available parking slots.
- Create and manage bookings.
- Cancel bookings.
- Calculate parking fees.
- View booking history.

## Out of Scope

- Online payments.
- Frontend application.
- Notifications.
- Real-time parking sensors.
- Multiple currencies.

## Booking Rules (v1)

1. A booking must have `start_time < end_time`. Both times must be timezone-aware and stored in UTC.
2. `start_time` must not be in the past.
3. Maximum booking duration is 24 hours.
4. Minimum billed time is 1 hour.
5. Fee = `lot.hourly_rate × ceil(duration_in_minutes / 60)`.
6. Overlapping CONFIRMED bookings on one slot are rejected by the booking service.
7. Back-to-back bookings are allowed. For example, one booking ending at 10:00 and another starting at 10:00.
8. A user may cancel only before `start_time`.
9. Cancelling less than 60 minutes before the start keeps 50% of the fee.
10. Slot availability is derived from bookings; it is never stored as a duplicate availability flag.c