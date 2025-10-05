import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, 12)
ax.set_ylim(0, 8)
ax.axis('off')

steps = [
    {'text': '1. Colonization\nPathogen adheres', 'x': 1, 'y': 6,
     'col': 'lightblue'},
    {'text': '2. Invasion\nBacterial multiplication', 'x': 4, 'y': 6,
     'col': 'lightgreen'},
    {'text': '3. Inflammation\nCytokine release', 'x': 7, 'y': 6,
     'col': 'salmon'},
    {'text': '4. Consolidation\nImpaired gas exchange', 'x': 10, 'y': 6,
     'col': 'coral'}
]

# Draw boxes
for step in steps:
    bbox = FancyBboxPatch((step['x']-1.5, step['y']-1.5), 3, 3,
                         boxstyle='round,pad=0.1',
                         facecolor=step['col'], edgecolor='black', linewidth=2)
    ax.add_patch(bbox)
    ax.text(step['x'], step['y'], step['text'], ha='center', va='center',
           fontsize=10, fontweight='bold')

# Draw arrows
for i in range(len(steps)-1):
    start = (steps[i]['x'] + 1.5, steps[i]['y'])
    end = (steps[i+1]['x'] - 1.5, steps[i+1]['y'])
    arrow = FancyArrowPatch(start, end, arrowstyle='->', mutation_scale=20,
                           color='black', linewidth=2)
    ax.add_patch(arrow)

# Title
ax.text(6, 7.5, 'Pathogenesis Sequence of Pneumonia', ha='center',
       fontsize=18, fontweight='bold')

# Subtitle for animation note
ax.text(6, 0.5, 'Note: This diagram can be animated step-by-step in PowerPoint\n'
       'by adding entrance animations (fade in, fly in from left)', ha='center',
       fontsize=10, style='italic')

# Save as PNG
plt.savefig('pneumonia_pathogenesis_diagram.png', dpi=300, bbox_inches='tight')
plt.close()

print('Pathogenesis diagram generated: pneumonia_pathogenesis_diagram.png')
