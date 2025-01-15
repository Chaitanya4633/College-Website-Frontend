import matplotlib.pyplot as plt
import networkx as nx

# Create a mind map using NetworkX
mind_map_data = {
    "Redesigning Social Media Analytics": {
        "Goals": [
            "Increase user engagement",
            "Improve data visualization",
            "Enhance user satisfaction"
        ],
        "User Needs": [
            "Easy access to key metrics",
            "Clear and intuitive layout",
            "Customization options",
            "Real-time data updates"
        ],
        "Design Thinking Phases": {
            "Empathize": [
                "User interviews",
                "Surveys for feedback",
                "Observational studies"
            ],
            "Define": [
                "Identify pain points",
                "Analyze user personas"
            ],
            "Ideate": [
                "Brainstorming sessions",
                "Collaborate with stakeholders",
                "Create user journey maps"
            ],
            "Prototype": [
                "Low-fidelity wireframes",
                "High-fidelity mockups",
                "Interactive dashboards"
            ],
            "Test": [
                "A/B testing",
                "User feedback sessions",
                "Usability testing"
            ]
        },
        "Key Features": [
            "Dashboard customization",
            "Data filtering and sorting",
            "Visual analytics (charts, graphs)",
            "Alerts for significant changes"
        ],
        "Metrics to Measure Success": [
            "User engagement (logins, session duration)",
            "User satisfaction (NPS, feedback scores)",
            "Adoption rate of new features",
            "Changes in data interpretation accuracy"
        ],
        "Tools and Technologies": [
            "Analytics platforms (Google Analytics, Tableau)",
            "Design tools (Figma, Adobe XD)",
            "Prototyping tools (InVision, Marvel)"
        ]
    }
}

def add_nodes_edges(graph, data, parent=None):
    for key, value in data.items():
        graph.add_node(key)
        if parent:
            graph.add_edge(parent, key)
        if isinstance(value, list):
            for item in value:
                graph.add_node(item)
                graph.add_edge(key, item)
        elif isinstance(value, dict):
            add_nodes_edges(graph, value, key)

# Create a graph
G = nx.DiGraph()
add_nodes_edges(G, mind_map_data)

# Create a layout for the nodes
pos = nx.spring_layout(G, seed=42)

# Draw the mind map
plt.figure(figsize=(12, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold', edge_color='gray')
plt.title("Mind Map: Redesigning Social Media Analytics", size=15)
plt.tight_layout()

# Save the figure
mind_map_image_path = "/mnt/data/mind_map_social_media_analytics.png"
plt.savefig(mind_map_image_path)

# Show the plot
plt.show()

mind_map_image_path
