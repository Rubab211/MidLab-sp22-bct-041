from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM
from datetime import datetime
from enum import Enum
from .database import Base

# ------------------ USER MODEL ------------------

class UserRole(str, Enum):
    admin = "Admin"
    customer = "Customer"

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(ENUM(UserRole), nullable=False)
    contact = Column(String, nullable=True)
    password_hash = Column(String, nullable=False)

    bookings = relationship("Booking", back_populates="user")


# ------------------ FLIGHT MODEL ------------------

class Flight(Base):
    __tablename__ = "flights"

    flight_id = Column(Integer, primary_key=True, autoincrement=True)
    flight_number = Column(String, nullable=False)
    departure_city = Column(String, nullable=False)
    arrival_city = Column(String, nullable=False)
    departure_time = Column(DateTime, nullable=False)
    arrival_time = Column(DateTime, nullable=False)
    airline = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    seats_available = Column(Integer, nullable=False)

    bookings = relationship("Booking", back_populates="flight")


# ------------------ HOTEL MODEL ------------------

class Hotel(Base):
    __tablename__ = "hotels"

    hotel_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    available_rooms = Column(Integer, nullable=False)
    price_per_night = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)

    bookings = relationship("Booking", back_populates="hotel")


# ------------------ BOOKING MODEL ------------------

class BookingType(str, Enum):
    flight = "flight"
    hotel = "hotel"

class Booking(Base):
    __tablename__ = "bookings"

    booking_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    booking_type = Column(ENUM(BookingType), nullable=False)
    flight_id = Column(Integer, ForeignKey("flights.flight_id"), nullable=True)
    hotel_id = Column(Integer, ForeignKey("hotels.hotel_id"), nullable=True)
    check_in = Column(DateTime, nullable=True)
    check_out = Column(DateTime, nullable=True)
    booking_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    total_amount = Column(Float, nullable=False)

    user = relationship("User", back_populates="bookings")
    flight = relationship("Flight", back_populates="bookings")
    hotel = relationship("Hotel", back_populates="bookings")
    payment = relationship("Payment", back_populates="booking", uselist=False)


# ------------------ PAYMENT MODEL ------------------

class PaymentMethod(str, Enum):
    credit_card = "credit_card"
    bank_transfer = "bank_transfer"
    cash = "cash"
    digital_wallet = "digital_wallet"

class PaymentStatus(str, Enum):
    successful = "successful"
    failed = "failed"
    pending = "pending"

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    booking_id = Column(Integer, ForeignKey("bookings.booking_id"), nullable=False)
    payment_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    amount = Column(Float, nullable=False)
    method = Column(ENUM(PaymentMethod), nullable=False)
    status = Column(ENUM(PaymentStatus), default=PaymentStatus.pending)

    booking = relationship("Booking", back_populates="payment")
