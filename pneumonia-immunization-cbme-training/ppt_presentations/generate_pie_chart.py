import plotly.express as px
import pandas as pd

# Pathogen Distribution Data for Community-Acquired Pneumonia (CAP)
pathogen_data = pd.DataFrame({
    'Pathogen': ['Streptococcus pneumoniae', 'Mycoplasma pneumoniae',
                'Chlamydophila pneumoniae', 'Haemophilus influenzae',
                'Legionella pneumophila', 'Respiratory Viruses',
                'Staphylococcus aureus', 'Others'],
    'Percentage': [32.5, 22.5, 12.5, 10, 6, 17.5, 3.5, 8],
    'Cases': ['25-40%', '15-30%', '10-15%', '5-15%', '2-10%',
             '15-20%', '2-5%', 'Rest']
})

# Create pie chart
fig = px.pie(pathogen_data,
             values='Percentage',
             names='Pathogen',
             title='CAP Pathogen Distribution',
             color_discrete_sequence=px.colors.qualitative.Set3)

# Customize layout
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(showlegend=False)

# Save as PNG
fig.write_image("pathogen_distribution_pie_chart.png")

print("Pie chart generated: pathogen_distribution_pie_chart.png")
