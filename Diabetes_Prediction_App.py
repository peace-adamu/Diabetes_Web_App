import streamlit as st
import joblib
import numpy as np

# Load the saved model
rfc_model = joblib.load(open('rfc_model.joblib', 'rb'))

# Function for prediction
def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data, dtype=float)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = rfc_model.predict(input_data_reshaped)
    return prediction[0]  # Return the first element of the prediction array

# Main function
def main():
    st.title('Diabetes Prediction Web App')

    st.markdown(
        """
        ## Welcome to the Diabetes Prediction App!  
        This tool helps predict the likelihood of diabetes based on key health indicators.  
        Please enter the required medical details below to proceed with the prediction.  
        """
    )

    st.subheader("Enter Patient Details")

    # Use Streamlit's form to prevent rerunning on every input change
    with st.form(key="prediction_form"):
        No_Pation = st.text_input('Number of patient')
        Age = st.text_input('Age of patient')
        Urea = st.text_input('Urea count')
        Cr = st.text_input('Creatinine count')
        HbAlc = st.text_input('HbAlc count')
        Chol = st.text_input('Cholesterol count')
        TG = st.text_input('TG count')
        HDL = st.text_input('HDL count')
        LDL = st.text_input('LDL count')
        VLDL = st.text_input('VLDL count')
        BMI = st.text_input('Body Mass Index value')

        Gender = st.selectbox('Gender', ['Female', 'Male'])
        Gender = 0 if Gender == 'Female' else 1

        # Submit button inside the form
        submitted = st.form_submit_button('Get Diabetes Test Result')

    if submitted:
        try:
            # Convert inputs to float
            input_data = [
                float(No_Pation), float(Age), float(Urea), float(Cr), float(HbAlc),
                float(Chol), float(TG), float(HDL), float(LDL), float(VLDL), float(BMI), int(Gender)
            ]

            diagnosis = diabetes_prediction(input_data)

            st.subheader("Prediction Result:")
            if diagnosis == 0:
                st.success('The person is not diabetic')
            elif diagnosis == 1:
                st.warning('The person is diabetic')
            elif diagnosis == 2:
                st.warning('Predicted diabetic')
            else:
                st.info('Mixed prediction')

        except Exception as e:
            st.error(f"An error occurred: {e}")

    # Retry button (clears session & reruns app)
    if st.button('Retry'):
        st.session_state.clear()
        st.rerun()

if __name__ == '__main__':
    main()
