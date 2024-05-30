#import os
#import json
import requests
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(page_title="Predict Landlside",
                   layout="wide",
                )

    
# getting the working directory of the main.py
#working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models


landslide_model = pickle.load(open('D:/landslide/Phase2/trained_model_alt.sav', 'rb'))



# sidebar for navigation
with st.sidebar:
    selected = option_menu('Main menu',

                           ['Home',
                            'Predict Landslide',
                            'About the Project'],
                          # menu_icon='',
                           #icons=['activity', 'heart', 'person'],
                           #default_index=0)
                          )

# Home Page
if selected == 'Home':

    # page title
    st.title('Welcome to Landslide Prediction System')
    
    #def load_lottiefile(filepath: str):
     #   with open(filepath, "r") as f:
      #      return json.load(f)


    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    

    #lottie_coding = load_lottiefile("lottiefile.json")  # replace link to local lottie file
    lottie_hello = load_lottieurl("https://lottie.host/ec5cc457-788d-489e-a793-0688a578b3cb/Z1iuPSAMdZ.json")

    st_lottie(
      lottie_hello,
      speed=1,
      reverse=False,
      loop=True,
      quality="low", # medium ; high
      #renderer="svg", # canvas
      height=500,
      width=None,
      key=None,
     )
    st.write("Note: Explore the side-bars for more options")
    

# Landslide Prediction Page
if selected == 'Predict Landslide':

    # page title
    st.title('Landslide Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        Aspect = st.text_input('Aspect value')

    with col2:
        Curvature = st.text_input('Curvature value')

    with col3:
        Earthquake = st.text_input('Earthquake value')
        
    with col1:
        Elevation = st.text_input('Elevation value')

    with col2:
        Flow = st.text_input('Flow value')

    with col3:
        Lithology = st.text_input('Lithology value')

    with col1:
        NDVI = st.text_input('Vegitation Index')

    with col2:
        NDWI = st.text_input('Wettness Index')

    with col3:
        Plan = st.text_input('Plan curvature value')

    with col1:
        Precipitation = st.text_input('Precipitation value')

    with col2:
        Profile = st.text_input('Profile curvature value')

    with col3:
        Slope = st.text_input('Slope value')


    # code for Prediction
    Predict = ''

    # creating a button for Prediction

    if st.button('Predict Result'):

        user_input = [Aspect, Curvature, Earthquake, Elevation, Flow, Lithology, NDVI, NDWI, Plan, Precipitation, Profile, Slope]

        user_input = [float(x) for x in user_input]

        landslide_prediction = landslide_model.predict([user_input])

        if landslide_prediction[0] == 0:
            Predict = 'Chances of landslide are low'
        else:
            Predict = 'There is a high possibility of landslide'

    st.success(Predict)
    
    
#About page

if selected == 'About the Project':

    # page title
    st.header('What is Landslide?')
    st.write(
        """
         - Landslides are the cataclysmic events due to mass movements of rock, debris, or earth down the slope under the influence of gravity, resulting in a geomorphic change of the earth’s surface. They co-occur with other natural disasters like flood, volcanoes and earthquakes, incurring more environmental damages and fatalities
         - Landslide may occur based on several triggering factors such as slope failure, high precipitation, road and other construction works etc
         - Many regions of western ghat such as Kodagu, Kerala and Himalayan regions of India have witnesses severe landslides causing fatalities and destructions all over the area
         - Between 1998-2017, landslides affected an estimated 4.8 million people and cause more than 18,000 deaths all over the world
        """
        )
    st.write("[Want to know more? >](https://en.wikipedia.org/wiki/Landslide)")
    
    st.header('Need of Landslide Prediction System')
    st.write(
        """
         - Landslide displacement prediction is important part of the monitoring and early warning systems. Effective prediction is instrumental in reducing the risk of landslide disaster
         - Detection, monitoring and prediction are fundamental to managing landslide risks and often rely on remote-sensing techniques that include the observation of Earth from space
         - Landslide Prediction System helps to predict the landslides that can occur based on several landslide triggering factors
         - Building a Landslide Prediction System not only helps to reduce fatalities, but also to make a proper urban planning and to take  the precautionary measures

        """
        )
    st.write("[reference >](https://www.mdpi.com/topics/44A4G7GEKB)")
    
    st.header('How this system works?')
    st.write(
        """
         - This system is based on machine learning approach. Because Machine learning algorithms can analyze vast amounts of data and finds hidden patterns and correlations that humans would not be able to detect
         - Different Machine learning algorithms such as K-nearest neighbor, decision tree, random forest, artificial neural network, convolution networks etc can be employed to predict the landslide prediction
         - This system uses random forest classifier as it's approach to predict the landslide
        """
        )
   

