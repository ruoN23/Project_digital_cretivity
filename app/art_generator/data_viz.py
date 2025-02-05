import matplotlib.pyplot as plt
import numpy as np

def generate_data_viz():
    # Données simulées
    x = np.linspace(0, 10, 100)
    y = np.sin(x) * np.cos(x)

    plt.plot(x, y, color="magenta", linewidth=3)
    plt.fill_between(x, y, color="cyan", alpha=0.3)
    plt.title("Sinusoidal Wave - Artistic Visualization")
    
    # Enregistrer l'image pour l'afficher dans la galerie
    plt.savefig("app/static/visualization.png")
    plt.close()
    return "visualization.png"
