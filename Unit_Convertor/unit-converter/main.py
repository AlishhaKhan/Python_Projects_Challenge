import streamlit as st

# --- Conversion logic ---
def convert_units(value, from_unit, to_unit):
    conversions = {
        "meter_kilometer": 0.001,   # 1 meter = 0.001 kilometers
        "kilometer_meter": 1000,    # 1 kilometer = 1000 meters
        "gram_kilogram": 0.001,     # 1 gram = 0.001 kilograms
        "kilogram_gram": 1000,      # 1 kilogram = 1000 grams
    }

    key = f"{from_unit}_{to_unit}"
    if key in conversions:
        return value * conversions[key]
    else:
        return "Conversion not supported."

# --- Streamlit UI ---
st.set_page_config("Unit Converter", page_icon="🔁")
st.title("🔁 Unit Converter")

value = st.number_input("Enter the value to convert:", min_value=1.0, step=0.1)

unit_from = st.selectbox("Convert from:", ["meter", "kilometer", "gram", "kilogram"])
unit_to = st.selectbox("Convert to:", ["meter", "kilometer", "gram", "kilogram"])

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.success(f"Converted value: {result}")
