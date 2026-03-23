# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 03:26:39 2026

@author: Depre
"""

# Projet : Transformations d'images avec NumPy et Matplotlib
# Auteur  : [Ryan Depret]
# Date    : 23 Mars 2026

import numpy as np
import matplotlib.pyplot as plt

# --- Chargement de l'image ---
image = plt.imread('Loup.jpg')

# --- Transformations ---

#Création d'une image au format vintage depuis l'image de départ
# Principe : moyenne des 3 canaux RGB pour chaque pixel.
image_gris = np.mean(image, axis=2).astype(np.uint8)

# Zoom sur la zone centrale
# On isole le quart central de l'image avec du slicing NumPy
h, l = image.shape[0], image.shape[1]
image_zoom = image[h//4 : h*3//4, l//4 : l*3//4]

# Inversion des couleurs pour la vision nocturne et la chaleur thermique du loup
# Chaque valeur de pixel est soustraite à 255
image_inverse = 255 - image

# --- Affichage ---
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

axes[0].imshow(image)
axes[0].set_title("Originale")
axes[0].axis('off')

axes[1].imshow(image_gris, cmap='gray')
axes[1].set_title("Niveaux de gris")
axes[1].axis('off')

axes[2].imshow(image_zoom)
axes[2].set_title("Zoom central")
axes[2].axis('off')

axes[3].imshow(image_inverse)
axes[3].set_title("Couleurs inversées")
axes[3].axis('off')

plt.suptitle("Transformations d'images avec NumPy", fontsize=14)
plt.tight_layout()
plt.show()