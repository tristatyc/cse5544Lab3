# (C) Author: Yuechen Tang
# 
# 2022 Spring: For The Ohio State University, Intro. Data. Vis Lectures
# 
# import libraries
# Click the arrow in the upper left corner. You will get the line like this
# "Go to the following link in your browser" following by a blue link or a weblink.
# click that link, choose your google account to authorize, and accept to obtain
# an access code. Use the icon (like two squares) to copy the code and paste to the 
#  "Enter verification code:" - AND hit character return (from your keyboard)
# 
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt

# Import the Climate Data
data = pd.read_csv("https://raw.githubusercontent.com/tristatyc/cse5544lab3-data/main/ClimateData.csv")

# Set title
st.title('Visualizations of Climate Data')

# Set header for perspective 1
st.header("Perspective 1: Honest, Ethical, and Truthful")

# Set subheader
st.subheader("Heatmap Visualization")

# Create heatmap 1

# Prepare the data
p1_data = data.drop(columns = ['Non-OECD Economies'])
p1_data = p1_data.set_index('Country\year')

p1_data = p1_data.apply(pd.to_numeric, errors = 'coerce')
p1_data.rename(columns = {"Country\year": "country", "value":"emission"}, inplace = True)
p1_data = np.log(p1_data)

# Generate heatmap1
fig1, ax1 = plt.subplots(figsize = (16, 7), dpi = 50)
ax1 = sns.heatmap(p1_data.T, linewidth = 0.5, cmap = "inferno", cbar_kws = {'label': 'emission amount'})
ax1.set_label('Countries')
ylabel = ax1.set_ylabel('Years')
xaxis = plt.xticks(rotation = 90, ha = 'center', fontsize = 8)
yaxis = plt.yticks(fontsize = 8)
title = ax1.set_title("Heatmap of Emissions of Countries by Years")

st.pyplot(fig1)

# Summary
st.subheader("Summary")
st.write("This heatmap is clear in delivering information about emission by countries and years to audiences. Since the original data has extreme large and small values, which makes the colormap not so clear in color representation, I have used 'log' to normalize the emission values, and this makes this plot clearer in differentiating colors and  more beautiful. Audiences can easily have a direct understanding of how the trends of emissions in each countries have changed by reading the heatmap. Additionally, the labels of axes and title of the heatmap are all listed, which can help audiences understand the context and information better.")


# Set header for perspective 2
st.header("Perspective 2: Dishonest, Unethical, and Deceiving")

# Set subheader
st.subheader("Heatmap Visualization")

# Create heatmap 2

# Prepare the data
p2_data = data.drop(columns = ['Non-OECD Economies'])
p2_data = pd.melt(p2_data, id_vars = ['Country\year'], var_name = 'year')
p2_data['value'] = p2_data['value'].apply(pd.to_numeric, errors = 'coerce')
p2_data.rename(columns = {"Country\year": "country", "value":"emission"}, inplace = True)


# Generate heatmap2 using altair
heatmap_2 = alt.Chart(p2_data).mark_rect().encode(
    x = alt.X('country:N', title = 'Countries'),
    y = alt.Y('year:O', title = 'Years'),
    color = alt.Color('emission:Q', scale = alt.Scale(scheme = 'rainbow')),
    tooltip = ['country', 'year', 'emission']
).properties(
    title = 'Visualization of Increasing Emission Amount')

st.altair_chart(heatmap_2, use_container_width = True)

# Summary
st.subheader("Summary")
st.write("Both colormaps represent the visualization of emission of countries by years, but this second one is not so good as the first heatmap. From the choice of colors, we can find that 'rainbow' scale has no clear and consistent direction, and it would also create misperception of the magnitude of the data. The changes between colors can't effectively present the changes and trend of values. Additionally, the title of this plot is misleading; actually, some countries have increasing trend in emission amount, while other countries have various different trends. Using the current title would result in misperception of audiences about the emission amount trend.")
st.markdown("# ")
st.write("In conclusion, the first heatmap visualization is better than the second heatmap visualization in both color choices and title descriptions.")
