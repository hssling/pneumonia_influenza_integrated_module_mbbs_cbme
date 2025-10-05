import plotly.express as px
import pandas as pd

# World Pneumonia Burden Map
# Synthetic data based on high burden countries (per 1000 children under 5 deaths)
world_data = pd.DataFrame({
    'country': ['India', 'Pakistan', 'Bangladesh', 'Indonesia', 'Nigeria',
               'Ethiopia', 'Democratic Republic of the Congo', 'Philippines', 'China',
               'Afghanistan', 'Angola', 'Burkina Faso'],
    'iso_alpha': ['IND', 'PAK', 'BGD', 'IDN', 'NGA',
                  'ETH', 'COD', 'PHL', 'CHN',
                  'AFG', 'AGO', 'BFA'],
    'pneumonia_deaths_per_1000': [50, 40, 35, 32, 30,
                                45, 40, 28, 15,
                                42, 48, 38]
})

fig = px.choropleth(world_data,
                    locations='iso_alpha',
                    color='pneumonia_deaths_per_1000',
                    hover_name='country',
                    color_continuous_scale='Reds',
                    title='Global Pneumonia Burden - Deaths per 1000 Under-5 Children')
fig.update_layout(geo=dict(showframe=False, showcoastlines=True))

# Save as PNG
fig.write_image("world_pneumonia_burden_map.png")

# India State Pneumonia Burden Visualization (Bar Chart Map Style)
# Synthetic data based on reported high burden states
india_data = pd.DataFrame({
    'state': ['Uttar Pradesh', 'Bihar', 'Rajasthan', 'Madhya Pradesh',
             'Maharashtra', 'Gujarat', 'Tamil Nadu', 'West Bengal',
             'Karnataka', 'Andhra Pradesh'],
    'pneumonia_cases_per_1000': [250, 230, 240, 210,
                                 180, 170, 160, 175,
                                 155, 165]
})

# Create horizontal bar chart representing state burden
fig2 = px.bar(india_data,
              y='state',
              x='pneumonia_cases_per_1000',
              orientation='h',
              color='pneumonia_cases_per_1000',
              color_continuous_scale='Oranges',
              title='Indian Pneumonia Burden - State-wise Cases per 1000 Population',
              labels={'pneumonia_cases_per_1000': 'Cases per 1000 People',
                     'state': 'State'})

# Save as PNG
fig2.write_image("india_pneumonia_burden_map.png")

print("Maps generated: world_pneumonia_burden_map.png and india_pneumonia_burden_map.png")
