import streamlit as st
def calculate_bmi(weight_kg, height_m):
    """
    Calculate BMI (Body Mass Index) using weight in kilograms and height in meters.
    Formula: BMI = weight (kg) / (height (m) * height (m))
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret BMI values according to the World Health Organization (WHO) categories.
    """
    if bmi < 18.5:
        return "UNDERWEIGHT\nYou are underweight. Go eat a bit"
    elif 18.5 <= bmi < 24.9:
        return "HEALTHY\nYou are normal weight. You are in good shape"
    elif 25 <= bmi < 29.9:
        return "OVERWEIGHT\nUh! no, you're heavier than general norms. Please do check your lifestyle."
    else:
        return "OBESE\nSorry, you should try and reduce your weight "

def main():
    # Get user input for weight and height
    st.title("⚖️ BMI Calculator 🧮")
    st.markdown("---")
    st.caption("Body Mass Index (BMI) is a measure that assesses an individual's body weight in relation to their height. It is a widely used screening tool to categorize individuals into different weight status categories, providing a general indication of whether a person has a healthy body weight. The resulting BMI is a numerical value that falls into one of several categories: \n- **Underweight:** BMI less than 18.5 \n- **Normal weight:** BMI between 18.5 and 24.9 \n- **Overweight:** BMI between 25 and 29.9 \n- **Obese:** BMI of 30 or greater \nIt's important to note that while BMI is a useful screening tool, it doesn't directly measure body fat percentage or distribution. Some individuals with high muscle mass may have a higher BMI but lower body fat percentage, while others with lower muscle mass may have a lower BMI but higher body fat percentage. Therefore, BMI should be considered as part of a broader assessment of an individual's health and weight status, and it may not be suitable for everyone, such as athletes with high muscle mass. Consulting with a healthcare professional is advisable for a more comprehensive evaluation of an individual's health and weight.")
    weight_kg = float(st.number_input("Enter your weight in kilograms: "))
    height_m = float(st.number_input("Enter your height in meters: "))
    submit=st.button("submit")
    if submit:
        # Calculate BMI
        bmi = calculate_bmi(weight_kg, height_m)

        # Interpret BMI and display the result
        interpretation = interpret_bmi(bmi)
        st.write(f"Your BMI is: {bmi:.2f}")
        st.write(f"{interpretation}")

if __name__ == "__main__":
    main()
