# Bismillahir Rahmaanir Raheem
# Almadadh Ya Gause Radi Allahu Ta'alah Anh - Ameen
# Zakia Salod

# import NumPy as np # np mean, np random
import pandas as pd # read csv, df manipulation
import plotly.express as px # interactive charts
import streamlit as st # data web application development
from PIL import Image


st.set_page_config(
    page_title="Drug_Rec",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)


image = Image.open('drug_rec_logo.png')


col1, mid, col2 = st.columns([1,1,35])
with col1:
    st.image('drug_rec_logo.png', width=60)
with col2:
    st.title("Drug_Rec: Drug Recommendations")
    
    
st.markdown("Drug recommendations for different medical conditions based on patient review ratings.")


df = pd.read_excel('average_rating.xlsx')
# top-level filters
LIST_OF_MEDICAL_CONDITIONS = sorted(df["Medical Condition"].unique())


st.markdown("### Select medical condition:")
medical_condition_filter = st.selectbox ("", LIST_OF_MEDICAL_CONDITIONS)


# dataframe filter
df = df[df["Medical Condition"] == medical_condition_filter]

# st.markdown("### Detailed Data View")
# st.dataframe(df[["drug_name", "rating_mean"]])



count_row = len(df)

if count_row == 1:
   st.markdown("### The following drug is recommended for "+medical_condition_filter + ":")
else:
   st.markdown("### The following " + str(count_row) + " drugs are recommended for "+medical_condition_filter + ":")
  


height_len = 400
if count_row > 30:
    height_len = 1000 
#st.markdown(height_len)
fig=px.bar(df,x='Rating',y='Drug', orientation='h', color='Rating', color_continuous_scale=px.colors.sequential.Blues, height=height_len)
st.write(fig)
