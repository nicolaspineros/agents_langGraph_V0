from langchain_core.tools import tool
import requests

@tool("book_appointment", description="Book a medical appointment")
def book_appointment(date: str, time: str, doctor: str, patient: str) -> str:
    """Book a medical appointment for a given date, time, doctor and patient"""
    ## TODO: Implement the logic to book an appointment
    return f"Appointment booked for {date} at {time} with {doctor} for {patient}"

@tool("get_appointment_availability", description="Get the availability of a medical appointment")
def get_appointment_availability(date: str, doctor: str) -> str:
    """Get the availability of a medical appointment for a given date and doctor"""
    ## TODO: Implement the logic to get the availability of an appointment
    return f"""Availability slots for the {doctor} are:
    - Monday: 10:00 - 11:00
    - Tuesday: 10:00 - 11:00
    - Wednesday: 10:00 - 11:00
    - Thursday: 10:00 - 11:00
    - Friday: 10:00 - 11:00
    - Saturday: 10:00 - 11:00
    - Sunday: 10:00 - 11:00
    """

tools = [book_appointment, get_appointment_availability]