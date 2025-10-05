import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Typical Pneumonia (Lobar consolidation)
axes[0].add_patch(Rectangle((0.1, 0.1), 0.8, 0.6, facecolor='blue', alpha=0.3,
                           linewidth=2, edgecolor='black'))
axes[0].text(0.5, 0.8, 'Lobar Consolidation', ha='center', fontsize=12, weight='bold')
axes[0].text(0.5, 0.5, 'Typical Pneumonia\n(S. pneumoniae)', ha='center',
            fontsize=10, wrap=True)
axes[0].set_title('Typical Pneumonia - X-ray', fontsize=14, weight='bold')
axes[0].axis('off')
axes[0].set_xlim(0, 1)
axes[0].set_ylim(0, 1)

# Atypical Pneumonia (Interstitial pattern)
axes[1].add_patch(Rectangle((0.1, 0.1), 0.8, 0.6, facecolor='red', alpha=0.2,
                           linewidth=2, edgecolor='black'))
axes[1].text(0.5, 0.8, 'Interstitial Pattern', ha='center', fontsize=12, weight='bold')
axes[1].text(0.5, 0.5, 'Atypical Pneumonia\n(Mycoplasma) ', ha='center',
            fontsize=10, wrap=True)
axes[1].set_title('Atypical Pneumonia - X-ray', fontsize=14, weight='bold')
axes[1].axis('off')
axes[1].set_xlim(0, 1)
axes[1].set_ylim(0, 1)

# Overall title
fig.suptitle('Pneumonia X-ray Comparison: Typical vs Atypical', fontsize=16, weight='bold')

# Note
fig.text(0.5, 0.02, 'Note: This is a simplified representation. '
       'Actual X-rays show specific lung patterns.', ha='center', fontsize=10,
       style='italic')

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.savefig('pneumonia_xray_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

print('X-ray comparison generated: pneumonia_xray_comparison.png')
