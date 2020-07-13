import streamlit as st

def print_insight_info():
    st.info("This section will give you an insight into the data, \
             how it looks, how is the data structured, what are the columns \
             what is the useful information etc")

def intro_info():
    st.info("This section will give a brief insight to the problem statement \
             and a brief outline for our approach, so that the audience is caught up to the project before \
            diving deeper into the analytics and model.")

def intro_model():
    st.info("This section will deal with trying different machine learning models for the \
                clasification task at hand which to predict whether the tool being used \
                in the CNC process is worn or not. We will be using multiple machin learning \
                models for our predictions and compare their performance to finally \
                present our results in the next section")