import urllib3
import json
import os
from dotenv import load_dotenv

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px
x = np.array(list(range(10)))
y = x**2

df = pd.DataFrame({'x': x, 'y':y})
fig = px.line(data_frame = df, 
             x = 'x' ,
              y = 'y', title = 'y = x^2')

st.plotly_chart(fig)
