from pydantic import BaseModel, EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime

# ------------------ USER SCHEMAS ------------------

class UserRole(str, Enum):
    admin = "Admin"
    customer = "Customer"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: UserRole
    contact: Optional[str]

class UserCreate(UserBase):
    password_hash: str

class User(UserBase):
    user_id: int

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    role: Optional[UserRole]
    contact: Optional[str]
    password_hash: Optional[str]

    class Config:
        from_attributes = True

# ------------------ FLIGHT SCHEMAS ------------------

class FlightBase(BaseModel):
    flight_number: str
    departure_city: str
    arrival_city: str
    departure_time: datetime
    arrival_time: datetime
    airline: str
    price: float
    seats_available: int

class FlightCreate(FlightBase):
    pass

class Flight(FlightBase):
    flight_id: int

    class Config:
        from_attributes = True

class FlightUpdate(BaseModel):
    price: Optional[float]
    seats_available: Optional[int]

    class Config:
        from_attributes = True

# ------------------ HOTEL SCHEMAS ------------------

class HotelBase(BaseModel):
    name: str
    location: str
    available_rooms: int
    price_per_night: float
    rating: Optional[float] = None

class HotelCreate(HotelBase):
    pass

class Hotel(HotelBase):
    hotel_id: int

    class Config:
        from_attributes = True

class HotelUpdate(BaseModel):
    available_rooms: Optional[int]
    price_per_night: Optional[float]
    rating: Optional[float]

    class Config:
        from_attributes = True

# ------------------ BOOKING SCHEMAS ------------------

class BookingType(str, Enum):
    flight = "flight"
    hotel = "hotel"

class BookingBase(BaseModel):
    user_id: int
    booking_type: BookingType
    flight_id: Optional[int] = None
    hotel_id: Optional[int] = None
    check_in: Optional[datetime] = None
    check_out: Optional[datetime] = None
    booking_date: datetime
    total_amount: float

class BookingCreate(BookingBase):
    pass

class Booking(BookingBase):
    booking_id: int

    class Config:
        from_attributes = True

class BookingUpdate(BaseModel):
    check_in: Optional[datetime]
    check_out: Optional[datetime]
    total_amount: Optional[float]

    class Config:
        from_attributes = True

# ------------------ PAYMENT SCHEMAS ------------------

class PaymentMethod(str, Enum):
    credit_card = "credit_card"
    bank_transfer = "bank_transfer"
    cash = "cash"
    digital_wallet = "digital_wallet"

class PaymentStatus(str, Enum):
    successful = "successful"
    failed = "failed"
    pending = "pending"

class PaymentBase(BaseModel):
    booking_id: int
    payment_date: datetime
    amount: float
    method: PaymentMethod
    status: PaymentStatus = PaymentStatus.pending

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    payment_id: int

    class Config:
        from_attributes = True

class PaymentUpdate(BaseModel):
    status: Optional[PaymentStatus]
    amount: Optional[float]
    method: Optional[PaymentMethod]

    class Config:
        from_attributes = True
