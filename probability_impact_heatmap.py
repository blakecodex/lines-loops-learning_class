import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Define risks with probability and impact scores (1=Low,5=High)
data = {
    'Risk': [
        'Construction Delays', 'Cost Overruns',
        'Local Protests', 'Security Incidents', 'Severe Weather'
    ],
    'Probability': [5, 3, 3, 5, 4],
    'Impact':     [5, 4, 3, 5, 4]
}

df = pd.DataFrame(data).set_index('Risk')

# Create matrix
plt.figure(figsize=(6, 4))
sns.heatmap(df, annot=True, cmap='Reds', cbar=False, linewidths=0.5)
plt.title('Probability vs. Impact Matrix')
plt.tight_layout()
plt.savefig('risk_matrix.png', dpi=300)
plt.show()
