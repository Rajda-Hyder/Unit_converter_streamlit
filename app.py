#imports

import streamlit as st

#Functions to convert units
def convert_units(value, from_unit, to_unit, unit_type):
    conversions = {
        "Length": {
            "Meters": 1,
            "Kilometers": 0.001,
            "Centimeters": 100,
            "Millimeters": 1000,
            "Miles": 0.000621371,
            "Yards": 1.09361,
            "Feet": 3.28084,
            "Inches": 39.3701,
         },
         "Weight": {
            "Kilograms": 1,
            "Grams": 1000,
            "Milligrams": 1000000,
            "Pounds": 2.20462,
            "Ounces": 35.274,
         },
        "Temperature": "Custom"
     }
     # Conditions to convert different units

    if unit_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # No conversion needed
    else:
        return value * conversions[unit_type][to_unit] / conversions[unit_type][from_unit]

# Streamlit UI
st.title("⏳ Unit Converter")
st.write("🔄 Convert Length, Weight, and Temperature units easily!")

# Select unit type
unit_type = st.selectbox("👇 Select Unit Type", ["Length", "Weight", "Temperature"])

# Define unit choices
if unit_type == "Length":
    units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"]
elif unit_type == "Weight":
    units = ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces"]
else:
    units = ["Celsius", "Fahrenheit", "Kelvin"]

# User input fields
value = st.number_input("Enter Value", value=0.0, step=0.1)
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

# Convert and display result
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, unit_type)
    st.success(f"{value} {from_unit} is equal to {result:.2f} {to_unit}")

