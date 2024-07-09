import numpy as np
import matplotlib.pyplot as plt
# Redefining the hands for positions
positions = ['Early', 'Middle', 'Late']

# Defining the hands for each position
early_hands = ["AA", "KK", "QQ", "JJ", "AKs", "AQs"]
middle_hands = early_hands + ["TT", "99", "AJs", "KQs", "ATs", "AQo"]
late_hands = middle_hands + ["88", "77", "66", "A9s", "A8s", "KTs", "QTs", "JTs", "KQo", "QJo", "JTo"]

# Creating a matrix for the hands
hands = sorted(set(early_hands + middle_hands + late_hands))
hand_freq = np.zeros((len(hands), len(positions)))

# Populating the matrix
for i, hand in enumerate(hands):
    if hand in early_hands:
        hand_freq[i, 0] = 1
    if hand in middle_hands:
        hand_freq[i, 1] = 1
    if hand in late_hands:
        hand_freq[i, 2] = 1

# Plotting the graph
fig, ax = plt.subplots(figsize=(12, 8))
cax = ax.matshow(hand_freq, cmap='Blues')

# Setting the labels
ax.set_xticks(np.arange(len(positions)))
ax.set_yticks(np.arange(len(hands)))
ax.set_xticklabels(positions)
ax.set_yticklabels(hands)

# Rotating the x-axis labels
plt.xticks(rotation=45)

# Adding values in cells
for i in range(len(hands)):
    for j in range(len(positions)):
        if hand_freq[i, j] > 0:
            ax.text(j, i, 'X', ha='center', va='center', color='black')

# Adding color bar
plt.colorbar(cax)

# Adjusting layout
plt.title('Recommended Hands to Play by Position')
plt.xlabel('Position')
plt.ylabel('Hands')
plt.tight_layout()

# Saving the plot to a file
plt.savefig('C:/Users/João Vitor/Desktop/recommended_hands_by_position.png')

# Displaying the plot
plt.show()
