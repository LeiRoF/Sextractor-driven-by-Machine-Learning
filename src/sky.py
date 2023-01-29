import os
import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
from numba import njit
import json
import imageio
from typing import Callable

# ____________________________________________________________________________________________________
# Sky object 🌌

class Sky:
    def __init__(
            self,
            N : int = 100,
            nb_stars : int = None,
            fwhm : float = None,
            intensity_prob : Callable[[float],float] = lambda x: 1,
            noise_intensity : float = None,
            noise_std : float = None
        ):
        self.N = N
        self.nb_stars = nb_stars
        self.fwhm = fwhm
        self.intensity_prob = intensity_prob
        self.noise_intensity = noise_intensity
        self.noise_std = noise_std
        self.picture, self.stars = create(N, nb_stars, fwhm, intensity_prob, noise_intensity, noise_std)
    
    def add_star(self, x, y, mag):
        X, Y = np.meshgrid(np.arange(self.N),np.arange(self.N))
        self.picture += _create_star(self.N, x, y, mag_to_lum(mag), self.fwhm, X, Y)
        self.stars.append([x, y, mag])

    def _imshow(self):
        plt.figure(figsize=(10,10))
        plt.imshow(self.picture, cmap='gray')
        plt.title("Sky")
        plt.colorbar()
    
    def show(self):
        self._imshow()
        plt.show()

    def save(self, path):
        self._imshow()
        if not os.path.isdir(dir := os.path.split(path)[0]):
            os.makedirs(dir)
        plt.savefig(path + ".png")
        self.save_stars(path)
    
    def save_stars(self, path):
        json.dump(self.stars, open(path + ".json", "w"))

    def save_ai_ready(self, path):
        imageio.imwrite(path+".png", (self.picture * 255 / np.max(self.picture)).astype(np.uint8))
        # np.savez_compressed(path, picture=self.picture)
        plt.savefig(path + ".png")
        self.save_stars_ai_ready(path)
    
    def save_stars_ai_ready(self, path):
        with open(path + ".txt", "w") as f:
            # format: class x_center y_center width height
            # with normalized values
            for star in self.stars:
                f.write(f"{0}\t{star[0]/self.N}\t{star[1]/self.N}\t{self.fwhm*2/self.N}\t{self.fwhm*2/self.N}\n")

# ____________________________________________________________________________________________________
# Conversions 📐

def mag_to_lum(mag):
    return 10**(-mag/2.5)

def lum_to_mag(lum):
    return -2.5*np.log10(lum)

# ____________________________________________________________________________________________________
# Create star ⭐

# @njit(fastmath=True)
def _create_star(x:float, y:float, l:float, fwhm:float, X:np.ndarray, Y:np.ndarray):
    """
    Generating gaussian star at position (x,y) with luminosity L and full-weight at half max fwhm.
    X and Y are the coordinate grid of the image.
    """
    return l*np.exp(-((X-x)**2 + (Y-y)**2)/(fwhm**2))

# ____________________________________________________________________________________________________
# Create sky picture 🌌

def create(
        N               : int   = 100,
        nb_stars        : int   = None,
        fwhm            : float = None,
        intensity_prob  = lambda x: 1, # 0*x allow to work with array
        noise_intensity : float = None,
        noise_std       : float = None,
    ) -> tuple[np.ndarray, list]:
    """
    Create a N*N matrix representing a picture of a sky that contain "nb_stars" stars with a luminosity between 0 and 1 (no photon to sensor saturation).
    - "N" is the size of the picture
    - "nb_star" is the number of star. Default: N/2
    - "fwhm" is the full width at half maximum of the stars. Default: N/100
    - "intensity_prob" function f(x) that return the probability p (in [0,1]) of having a star at mag at mag x, with x in [0,1]. Default: lambda x: 1
    - "noise_intensity" is the mean intensity of the gaussian noise. Default: None (no noise)
    - "noise_std" is the standard deviation of the gaussian noise. Default: None (no noise)
    """

    # Defining default values
    if nb_stars is None:
        nb_stars = int(N/10)
    if fwhm is None:
        fwhm = 10

    # Defining coordinate grids 🧭
    X, Y = np.meshgrid(np.arange(N),np.arange(N))

    # Getting position of all stars 📍
    x = np.random.randint(N, size=nb_stars)
    y = np.random.randint(N, size=nb_stars)

    stars = []
    intensities = []
    for i in range(nb_stars):
        intensity = np.random.rand()
        while np.random.rand() > intensity_prob(intensity):
            intensity = np.random.rand()
        stars.append(_create_star(x[i], y[i], intensity, fwhm, X, Y))
        intensities.append(intensity)

    # Superposing all stars on the same picture 🌌
    sky = np.sum(np.array(stars), axis=0)

    # Adding noise 🔉
    if None not in [noise_intensity, noise_std]: 
        noise = np.random.normal(noise_intensity, noise_std, (N,N))
        sky += mag_to_lum(noise)

    return sky, np.array(list(zip(x, y, intensities))).astype(int).tolist()

# ____________________________________________________________________________________________________
# Test zone 🧪

if __name__ == "__main__":

    N = 1000

    # Generating sky picture 🌌
    sky = Sky(
        N, # Image size
        nb_stars=100, # Number of stars
        fwhm=3, # fwhm of all stars
        mag=np.arange(0,6), # possible magnitudes of the stars
        mag_prob=np.arange(1,7)**2, # probability associated to each magnitude
        noise_mag=4, # mean of the gaussian noise
        noise_std=0.1, # standard deviation of the gaussian noise
    )

    # Sorting starList by magnitude ⚖️
    sky.stars.sort(key=lambda x: x[2])

    # Printing the list of stars 📜
    print(f"Stars:")
    for s in sky.stars:
        print(f" - x={s[0]}, y={s[1]}, mag={s[2]}")
    
    # Showing the picture 📷
    sky.show()