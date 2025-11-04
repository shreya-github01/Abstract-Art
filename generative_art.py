import matplotlib.pyplot as plt
import numpy as np

def generate_abstract_art(num_circles=50):
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_facecolor('#f4f8fb')
    plt.axis('off')

    for _ in range(num_circles):
        # Random circle parameters
        x, y = np.random.rand(2)
        radius = np.random.uniform(0.05, 0.15)
        color = np.random.choice(['#005eb6', '#0077cc', '#00aaff', '#66ccff', '#99ddff'])
        circle = plt.Circle((x, y), radius, color=color, alpha=0.6)
        ax.add_patch(circle)

    plt.title('Generative Colorful Circles', fontsize=18, color='#005eb6', pad=20)
    plt.tight_layout()
    plt.savefig('generative_art.png')
    plt.show()

if __name__ == "__main__":
    generate_abstract_art()
