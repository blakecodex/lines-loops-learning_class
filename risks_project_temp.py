import os
import graphviz

# If needed, add Graphviz bin to PATH (Windows)
# os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

# Create a diagram for stakeholder risk tolerances
dot = graphviz.Digraph(format='png')

# Add a title
dot.attr(label='Olympics Stakeholder Risk Tolerances', labelloc='t', fontsize='20', fontname='Helvetica')

# Define stakeholders with colors by tolerance
dot.node('Government', 'Halifax City Government', shape='box', style='filled', fillcolor='lightcoral')
dot.node('Committee', 'Concordia Olympic Committee', shape='box', style='filled', fillcolor='gold')
dot.node('Business', 'Local Business Owners', shape='box', style='filled', fillcolor='lightgreen')
dot.node('Contractors', 'Construction Contractors', shape='box', style='filled', fillcolor='lightgreen')
dot.node('Residents', 'Neighborhood Residents', shape='box', style='filled', fillcolor='gold')

# Legend entries
dot.node('Seeker', 'Risk Seeker', shape='plaintext', fontcolor='lightcoral')
dot.node('Neutral', 'Risk Neutral', shape='plaintext', fontcolor='gold')
dot.node('Averse', 'Risk Averse', shape='plaintext', fontcolor='lightgreen')

# Invisible edges to keep legend grouped
dot.edge('Seeker', 'Committee', style='invis')
dot.edge('Neutral', 'Business', style='invis')
dot.edge('Averse', 'Government', style='invis')

# Define output filename
diagram_path = 'olympics_stakeholder_tolerance'

# Render and save diagram
dot.render(diagram_path)

print(f'Diagram saved as {diagram_path}.png')
