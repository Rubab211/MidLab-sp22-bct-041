from fastapi import FastAPI, HTTPException
from typing import List
from datetime import datetime
from Schema import User, UserCreate, UserUpdate, Flight, FlightCreate, FlightUpdate, Hotel, HotelCreate, HotelUpdate, \
    Booking, BookingCreate, BookingUpdate, Payment, PaymentCreate, PaymentUpdate

# ------------------ MOCK DATABASE ------------------
users_db = []
flights_db = []
hotels_db = []
bookings_db = []
payments_db = []

app = FastAPI()

@app.on_event("startup")
def on_startup():
    # Initialize the database, could be connecting to a real DB
    pass

# ------------------ USER ROUTES ------------------

@app.post("/users/", response_model=User)
def create_user(user: UserCreate):
    user_id = len(users_db) + 1
    new_user = User(user_id=user_id, **user.dict())
    users_db.append(new_user)
    return new_user

@app.get("/users/", response_model=List[User])
def get_users():
    return users_db

@app.get("/users/{user_id}", response_model=User)
def get_user(user_id: int):
    user = next((user for user in users_db if user.user_id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserUpdate):
    user = next((user for user in users_db if user.user_id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    updated_user = user.copy(update=user_update.dict(exclude_unset=True))
    users_db[users_db.index(user)] = updated_user
    return updated_user

@app.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int):
    user = next((user for user in users_db if user.user_id == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    users_db.remove(user)
    return user


# ------------------ FLIGHT ROUTES ------------------

@app.post("/flights/", response_model=Flight)
def create_flight(flight: FlightCreate):
    flight_id = len(flights_db) + 1
    new_flight = Flight(flight_id=flight_id, **flight.dict())
    flights_db.append(new_flight)
    return new_flight

@app.get("/flights/{flight_id}", response_model=Flight)
def get_flight(flight_id: int):
    flight = next((flight for flight in flights_db if flight.flight_id == flight_id), None)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

@app.put("/flights/{flight_id}", response_model=Flight)
def update_flight(flight_id: int, flight_update: FlightUpdate):
    flight = next((flight for flight in flights_db if flight.flight_id == flight_id), None)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")

    updated_flight = flight.copy(update=flight_update.dict(exclude_unset=True))
    flights_db[flights_db.index(flight)] = updated_flight
    return updated_flight

@app.delete("/flights/{flight_id}", response_model=Flight)
def delete_flight(flight_id: int):
    flight = next((flight for flight in flights_db if flight.flight_id == flight_id), None)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    flights_db.remove(flight)
    return flight


# ------------------ HOTEL ROUTES ------------------

@app.post("/hotels/", response_model=Hotel)
def create_hotel(hotel: HotelCreate):
    hotel_id = len(hotels_db) + 1
    new_hotel = Hotel(hotel_id=hotel_id, **hotel.dict())
    hotels_db.append(new_hotel)
    return new_hotel

@app.get("/hotels/{hotel_id}", response_model=Hotel)
def get_hotel(hotel_id: int):
    hotel = next((hotel for hotel in hotels_db if hotel.hotel_id == hotel_id), None)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    return hotel

@app.put("/hotels/{hotel_id}", response_model=Hotel)
def update_hotel(hotel_id: int, hotel_update: HotelUpdate):
    hotel = next((hotel for hotel in hotels_db if hotel.hotel_id == hotel_id), None)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")

    updated_hotel = hotel.copy(update=hotel_update.dict(exclude_unset=True))
    hotels_db[hotels_db.index(hotel)] = updated_hotel
    return updated_hotel

@app.delete("/hotels/{hotel_id}", response_model=Hotel)
def delete_hotel(hotel_id: int):
    hotel = next((hotel for hotel in hotels_db if hotel.hotel_id == hotel_id), None)
    if not hotel:
        raise HTTPException(status_code=404, detail="Hotel not found")
    hotels_db.remove(hotel)
    return hotel


# ------------------ BOOKING ROUTES ------------------

@app.post("/bookings/", response_model=Booking)
def create_booking(booking: BookingCreate):
    booking_id = len(bookings_db) + 1
    new_booking = Booking(booking_id=booking_id, **booking.dict())
    bookings_db.append(new_booking)
    return new_booking

@app.get("/bookings/{booking_id}", response_model=Booking)
def get_booking(booking_id: int):
    booking = next((booking for booking in bookings_db if booking.booking_id == booking_id), None)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@app.put("/bookings/{booking_id}", response_model=Booking)
def update_booking(booking_id: int, booking_update: BookingUpdate):
    booking = next((booking for booking in bookings_db if booking.booking_id == booking_id), None)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    updated_booking = booking.copy(update=booking_update.dict(exclude_unset=True))
    bookings_db[bookings_db.index(booking)] = updated_booking
    return updated_booking

@app.delete("/bookings/{booking_id}", response_model=Booking)
def delete_booking(booking_id: int):
    booking = next((booking for booking in bookings_db if booking.booking_id == booking_id), None)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    bookings_db.remove(booking)
    return booking


# ------------------ PAYMENT ROUTES ------------------

@app.post("/payments/", response_model=Payment)
def create_payment(payment: PaymentCreate):
    payment_id = len(payments_db) + 1
    new_payment = Payment(payment_id=payment_id, **payment.dict())
    payments_db.append(new_payment)
    return new_payment

@app.get("/payments/{payment_id}", response_model=Payment)
def get_payment(payment_id: int):
    payment = next((payment for payment in payments_db if payment.payment_id == payment_id), None)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@app.put("/payments/{payment_id}", response_model=Payment)
def update_payment(payment_id: int, payment_update: PaymentUpdate):
    payment = next((payment for payment in payments_db if payment.payment_id == payment_id), None)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")

    updated_payment = payment.copy(update=payment_update.dict(exclude_unset=True))
    payments_db[payments_db.index(payment)] = updated_payment
    return updated_payment

@app.delete("/payments/{payment_id}", response_model=Payment)
def delete_payment(payment_id: int):
    payment = next((payment for payment in payments_db if payment.payment_id == payment_id), None)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    payments_db.remove(payment)
    return payment
