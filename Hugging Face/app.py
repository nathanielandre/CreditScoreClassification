# Libraries
import streamlit as st

import eda
import prediction

# navigation
navigation = st.sidebar.selectbox('Pilih Halaman:',('Predictor','EDA'))

# pilih page
if navigation == 'Predictor':
    prediction.run()
else :
    eda.run()