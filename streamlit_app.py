import streamlit as st
import pickle
import streamlit_authenticator as stauth
from pathlib import Path


st.set_page_config(
    page_title="",
    page_icon="door-arrow-right",
    layout='wide'
)

# --- USER AUTHENTICATION ---
names = ['Visitor', 'Admin']
usernames = ['user', 'admin']

# Load hashed passwords
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
                                    'churn_app', 'abcdefg', cookie_expiry_days=10)


# --- LANDING PAGE ---
col1,col2 = st.columns(2)
with col2:
    name, authentication_status, username = authenticator.login('Login','main')
    st.session_state['name'] = name
    st.session_state['authentication_status'] = authentication_status
    st.session_state['username'] = username

    if authentication_status == None:
        st.info('Please Log in to continue')
        st.markdown('### **Demo credentials**')
        st.write('Username: user')
        st.write('Password: abc123')
        st.markdown('''
                    <style>
                    [data-testid="stSidebar"] {
                        visibility: hidden;
                    }
                    </style>
                    ''', unsafe_allow_html=True)
            
with col1:
    if authentication_status == None:
        st.title('THIS IS OUR CHURN PREDICTION APP\n'
                'WE HAVE LEVARAGED MACHINE LEARNING AND DEEP LEARNING TECHNIQUES TO MAKE A STATE OF THE ART PREDICTION APP \n\n')
        st.write('SUPPORT US\n\n'
                'See something I can improve on or help you out with?\n\n'
                'WE ARE THRILED TO PRESENT THIS BEFORE YOU:\n\n\n'
                )
        

# -- Main app section --
if authentication_status == False:
    with col1:
        st.title('This is a binary classification model for Churn Predition\n'
                'It has been developed with care....... \n\n')
        st.write('There is always room for improvements\n\n'
                'we will be waiting for your recomendations\n\n'
                'This app is far from perfect and we are still trying to make it better!!!\n\n\n'
                )
    with col2:
        st.error('Wrong username / password')
        st.info('Please try again with the credentials below')
        st.markdown('### **Demo credentials**')
        st.write('Username: user')
        st.write('Password: abc123')
        st.markdown('''
        <style>
        [data-testid="stSidebar"] {
            visibility: hidden;
        }
        </style>
        ''', unsafe_allow_html=True)


# --- HOME PAGE ---
if authentication_status:
    st.button(f'{st.session_state["name"]} logged in')
    st.title(f'Welcome {st.session_state["username"]} to the Customer Churn Prediction App')
    st.write('''

<br>
</div>
<div style="background-color:#800000;padding:15px;border-radius:15px">
<h1 style="color:#ff6347;text-align:center">Customer Churn Prediction: LEVERAGING MACHINE LEARNING AND DEEP LEARNING TO CREATE A ROBUST SYSTEM</h1>
<p style="color:#f5f5f5;font-size:18px">Our app empowers businesses to stay ahead by predicting customer churn, enabling proactive retention strategies.</p>
<p style="color:#f5f5f5;font-size:18px">Use the latest advancements in machine learning and deep learning models to understand customer behavior and reduce churn.</p>

<br>
<div style="background-color:#b22222;padding:15px;border-radius:15px">
<h1 style="color:#ff6347;text-align:center">Data-Driven Decision Making</h1>
<p style="color:#ffffff;font-size:18px">Leverage cutting-edge algorithms, including Logistic Regression and LSTM models, to get accurate predictions.</p>
<p style="color:#ffffff;font-size:18px">Understand past behaviors and predict future trends effortlessly with our user-friendly platform.</p>
<p style="color:#ffffff;font-size:18px">Simply upload your customer data, choose your preferred model, and receive real-time predictions for customer churn.</p>

<h2 style="color:#ff6347">Key Features</h2>
<ul>
    <li style="color:#ff7f7f"><b>Hybrid Models:</b> Choose from Logistic Regression or LSTM-based models, designed for accuracy and speed.</li>
    <li style="color:#f5f5f5"><b>Efficient Workflows:</b> Streamlined processes to get results with just a few clicks.</li>
    <li style="color:#ff7f7f"><b>Data History:</b> Keep track of predictions in the "history.csv" file for further analysis.</li>
    <li style="color:#f5f5f5"><b>Interactive Visualizations:</b> Dive deep into predictions with easy-to-understand visual insights.</li>
</ul>

<h2 style="color:#ff6347">Maximizing Impact with Data</h2>
<p style="color:#ffffff;font-size:18px">Our app helps you transform data into actionable insights. Make informed decisions, reduce churn, and boost customer loyalty.</p>
<p style="color:#ffffff;font-size:18px">This is more than just a prediction tool – it's a partner in your business growth journey.</p>

<br>

<div style="background-color:#ff6347;padding:15px;border-radius:15px">
<h1 style="color:#000;text-align:center">Start Your Journey Today</h1>
<p style="color:#000;text-align:center">Experience the power of predictive analytics with our intuitive and efficient churn prediction app.</p>
</div>
''', unsafe_allow_html=True)


    st.markdown('### HEY!!! DO NOT GO....WE LIKE HAVING YOU WITH US....SADFACE ')

    authenticator.logout('Logout','main')
    
    