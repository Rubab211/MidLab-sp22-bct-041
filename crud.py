from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
from . import models, Schema

# ------------------ USER CRUD ------------------

def create_user(db: Session, user: Schema.UserCreate):
    db_user = models.User(
        name=user.name,
        email=user.email,
        role=user.role,
        contact=user.contact,
        password_hash=user.password_hash,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: int) -> Optional[models.User]:
    return db.query(models.User).filter(models.User.user_id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[models.User]:
    return db.query(models.User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user: Schema.UserUpdate) -> Optional[models.User]:
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user:
        if user.name:
            db_user.name = user.name
        if user.email:
            db_user.email = user.email
        if user.role:
            db_user.role = user.role
        if user.contact:
            db_user.contact = user.contact
        if user.password_hash:
            db_user.password_hash = user.password_hash
        db.commit()
        db.refresh(db_user)
        return db_user
    return None


def delete_user(db: Session, user_id: int) -> Optional[models.User]:
    db_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None


# ------------------ FLIGHT CRUD ------------------

def create_flight(db: Session, flight: Schema.FlightCreate):
    db_flight = models.Flight(
        flight_number=flight.flight_number,
        departure_time=flight.departure_time,
        arrival_time=flight.arrival_time,
        departure_city=flight.departure_city,
        arrival_city=flight.arrival_city,
        price=flight.price,
    )
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight


def get_flight(db: Session, flight_id: int) -> Optional[models.Flight]:
    return db.query(models.Flight).filter(models.Flight.flight_id == flight_id).first()


def get_flights(db: Session, skip: int = 0, limit: int = 100) -> List[models.Flight]:
    return db.query(models.Flight).offset(skip).limit(limit).all()


def update_flight(db: Session, flight_id: int, flight: Schema.FlightUpdate) -> Optional[models.Flight]:
    db_flight = db.query(models.Flight).filter(models.Flight.flight_id == flight_id).first()
    if db_flight:
        if flight.departure_time:
            db_flight.departure_time = flight.departure_time
        if flight.arrival_time:
            db_flight.arrival_time = flight.arrival_time
        if flight.price is not None:
            db_flight.price = flight.price
        db.commit()
        db.refresh(db_flight)
        return db_flight
    return None


def delete_flight(db: Session, flight_id: int) -> Optional[models.Flight]:
    db_flight = db.query(models.Flight).filter(models.Flight.flight_id == flight_id).first()
    if db_flight:
        db.delete(db_flight)
        db.commit()
        return db_flight
    return None


# ------------------ HOTEL CRUD ------------------

def create_hotel(db: Session, hotel: Schema.HotelCreate):
    db_hotel = models.Hotel(
        hotel_name=hotel.hotel_name,
        location=hotel.location,
        price_per_night=hotel.price_per_night,
        available_rooms=hotel.available_rooms,
    )
    db.add(db_hotel)
    db.commit()
    db.refresh(db_hotel)
    return db_hotel


def get_hotel(db: Session, hotel_id: int) -> Optional[models.Hotel]:
    return db.query(models.Hotel).filter(models.Hotel.hotel_id == hotel_id).first()


def get_hotels(db: Session, skip: int = 0, limit: int = 100) -> List[models.Hotel]:
    return db.query(models.Hotel).offset(skip).limit(limit).all()


def update_hotel(db: Session, hotel_id: int, hotel: Schema.HotelUpdate) -> Optional[models.Hotel]:
    db_hotel = db.query(models.Hotel).filter(models.Hotel.hotel_id == hotel_id).first()
    if db_hotel:
        if hotel.price_per_night is not None:
            db_hotel.price_per_night = hotel.price_per_night
        if hotel.available_rooms is not None:
            db_hotel.available_rooms = hotel.available_rooms
        db.commit()
        db.refresh(db_hotel)
        return db_hotel
    return None


def delete_hotel(db: Session, hotel_id: int) -> Optional[models.Hotel]:
    db_hotel = db.query(models.Hotel).filter(models.Hotel.hotel_id == hotel_id).first()
    if db_hotel:
        db.delete(db_hotel)
        db.commit()
        return db_hotel
    return None


# ------------------ BOOKING CRUD ------------------

def create_booking(db: Session, booking: Schema.BookingCreate):
    db_booking = models.Booking(
        user_id=booking.user_id,
        flight_id=booking.flight_id,
        hotel_id=booking.hotel_id,
        booking_date=booking.booking_date,
        total_amount=booking.total_amount,
    )
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return db_booking


def get_booking(db: Session, booking_id: int) -> Optional[models.Booking]:
    return db.query(models.Booking).filter(models.Booking.booking_id == booking_id).first()


def get_bookings(db: Session, skip: int = 0, limit: int = 100) -> List[models.Booking]:
    return db.query(models.Booking).offset(skip).limit(limit).all()


def update_booking(db: Session, booking_id: int, booking: Schema.BookingUpdate) -> Optional[models.Booking]:
    db_booking = db.query(models.Booking).filter(models.Booking.booking_id == booking_id).first()
    if db_booking:
        if booking.total_amount is not None:
            db_booking.total_amount = booking.total_amount
        db.commit()
        db.refresh(db_booking)
        return db_booking
    return None


def delete_booking(db: Session, booking_id: int) -> Optional[models.Booking]:
    db_booking = db.query(models.Booking).filter(models.Booking.booking_id == booking_id).first()
    if db_booking:
        db.delete(db_booking)
        db.commit()
        return db_booking
    return None


# ------------------ PAYMENT CRUD ------------------

def create_payment(db: Session, payment: Schema.PaymentCreate):
    db_payment = models.Payment(
        order_id=payment.order_id,
        payment_date=payment.payment_date,
        amount=payment.amount,
        method=payment.method,
        status=payment.status or models.PaymentStatus.pending,
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment


def get_payment(db: Session, payment_id: int) -> Optional[models.Payment]:
    return db.query(models.Payment).filter(models.Payment.payment_id == payment_id).first()


def get_payments(db: Session, skip: int = 0, limit: int = 100) -> List[models.Payment]:
    return db.query(models.Payment).offset(skip).limit(limit).all()


def update_payment(db: Session, payment_id: int, payment: Schema.PaymentUpdate) -> Optional[models.Payment]:
    db_payment = db.query(models.Payment).filter(models.Payment.payment_id == payment_id).first()
    if db_payment:
        if payment.status:
            db_payment.status = payment.status
        if payment.amount is not None:
            db_payment.amount = payment.amount
        if payment.method:
            db_payment.method = payment.method
        db.commit()
        db.refresh(db_payment)
        return db_payment
    return None


def delete_payment(db: Session, payment_id: int) -> Optional[models.Payment]:
    db_payment = db.query(models.Payment).filter(models.Payment.payment_id == payment_id).first()
    if db_payment:
        db.delete(db_payment)
        db.commit()
        return db_payment
    return None
