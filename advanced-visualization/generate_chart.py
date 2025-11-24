import pandas as pd
import matplotlib.pyplot as plt
import circlify
import random

# Set seed for reproducibility
random.seed(42)

# 1. Generate Data
data = [
    {"sector": "Technology", "asset": "Microsoft", "investment": 10156734},
    {"sector": "Technology", "asset": "Apple", "investment": 9500000},
    {"sector": "Technology", "asset": "NVIDIA", "investment": 8200000},
    {"sector": "Technology", "asset": "Google", "investment": 7800000},
    {"sector": "Technology", "asset": "Amazon", "investment": 7500000},
    {"sector": "Finance", "asset": "JPMorgan", "investment": 3292047},
    {"sector": "Finance", "asset": "Visa", "investment": 2900000},
    {"sector": "Finance", "asset": "Mastercard", "investment": 2700000},
    {"sector": "Finance", "asset": "Bank of America", "investment": 2100000},
    {"sector": "Energy", "asset": "ExxonMobil", "investment": 4100000},
    {"sector": "Energy", "asset": "Chevron", "investment": 3920917},
    {"sector": "Energy", "asset": "Shell", "investment": 3500000},
    {"sector": "Healthcare", "asset": "UnitedHealth", "investment": 4500000},
    {"sector": "Healthcare", "asset": "J&J", "investment": 4200000},
    {"sector": "Healthcare", "asset": "Pfizer", "investment": 2800000},
    {"sector": "Consumer", "asset": "Walmart", "investment": 5100000},
    {"sector": "Consumer", "asset": "P&G", "investment": 3800000},
    {"sector": "Consumer", "asset": "Coca-Cola", "investment": 3200000}
]

df = pd.DataFrame(data)

# 2. Prepare Data for Circlify
# Group by sector
sectors = df.groupby('sector')
circles_data = []

for sector_name, group in sectors:
    children = []
    for _, row in group.iterrows():
        children.append({'id': row['asset'], 'datum': row['investment']})
    circles_data.append({'id': sector_name, 'datum': group['investment'].sum(), 'children': children})

# 3. Compute Circle Positions
circles = circlify.circlify(
    circles_data, 
    show_enclosure=False, 
    target_enclosure=circlify.Circle(x=0, y=0, r=1)
)

# 4. Plot
fig, ax = plt.subplots(figsize=(8, 8), dpi=64) # 512x512 pixels

# Define colors for sectors
sector_colors = {
    'Technology': '#66c2a5',
    'Finance': '#fc8d62',
    'Energy': '#8da0cb',
    'Healthcare': '#e78ac3',
    'Consumer': '#a6d854'
}

# Find max depth to distinguish sectors from assets
max_depth = max(circle.level for circle in circles)

# Draw circles
for circle in circles:
    if circle.level == 1: # Sector level
        label = circle.ex['id']
        color = sector_colors.get(label, '#cccccc')
        alpha = 0.3
        linewidth = 2
        
        # Draw sector circle
        ax.add_patch(plt.Circle((circle.x, circle.y), circle.r, alpha=alpha, linewidth=linewidth, color=color, fill=True))
        ax.add_patch(plt.Circle((circle.x, circle.y), circle.r, alpha=1.0, linewidth=linewidth, color=color, fill=False))
        
        # Label sector at top of circle if large enough
        if circle.r > 0.3:
            plt.text(circle.x, circle.y + circle.r - 0.1, label, ha='center', va='bottom', fontsize=14, fontweight='bold', color='#333')

    elif circle.level == 2: # Asset level
        parent_label = circle.ex['id'] # Actually this might be the asset ID
        # To get sector color, we need to know the parent. 
        # But circlify structure is a bit flat in output list, let's just use a default or lookup if possible.
        # Actually, circle.ex['id'] is the asset name.
        
        # Draw asset circle
        ax.add_patch(plt.Circle((circle.x, circle.y), circle.r, alpha=0.8, linewidth=1, color='#ffffff', fill=True))
        ax.add_patch(plt.Circle((circle.x, circle.y), circle.r, alpha=1.0, linewidth=1, color='#666666', fill=False))
        
        # Label asset
        if circle.r > 0.05:
            plt.text(circle.x, circle.y, circle.ex['id'], ha='center', va='center', fontsize=9, color='black')

# Clean up plot
ax.axis('off')
ax.set_title('Investment Portfolio Allocation\n(Circle Packing)', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()

# Save
plt.savefig('chart.png', dpi=64)
print("Circle packing chart generated: chart.png")
