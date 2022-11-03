import numpy as np
import matplotlib.pyplot as plt
from multiprocessing import Pool
from numba import njit

# ____________________________________________________________________________________________________
# Sky object 🌌

class Sky:
    def __init__(
        self,
        N         : int   = 100,
        nb_stars  : int   = None,
        fwhm      : float = None,
        mag       : list  = np.arange(0,5),
        mag_prob  : list  = np.ones(5),
        noise_mag : float = None,
        noise_std : float = None
    ):
        self.N = N
        self.nb_stars = nb_stars
        self.fwhm = fwhm
        self.mag = mag
        self.mag_prob = mag_prob
        self.noise_mag = noise_mag
        self.noise_std = noise_std
        self.picture, self.stars = create(N, nb_stars, fwhm, mag, mag_prob, noise_mag, noise_std)
    
    def add_star(self, x, y, mag):
        X, Y = np.meshgrid(np.arange(self.N),np.arange(self.N))
        self.picture += _create_star(self.N, x, y, mag_to_lum(mag), self.fwhm, X, Y)
        self.stars.append([x, y, mag])

    def _imshow(self):
        plt.figure(figsize=(10,10))
        plt.imshow(self.picture, cmap='inferno')
        plt.title("Sky")
        plt.colorbar()
    
    def show(self):
        self._imshow()
        plt.show()

    def save(self, path):
        self._imshow()
        plt.savefig(path)

# ____________________________________________________________________________________________________
# Conversions 📐

def mag_to_lum(mag):
    return 10**(-mag/2.5)

def lum_to_mag(lum):
    return -2.5*np.log10(lum)

# ____________________________________________________________________________________________________
# Create star ⭐

@njit(fastmath=True)
def _create_star(x:float, y:float, l:float, fwhm:float, X:np.ndarray, Y:np.ndarray):
    """
    Generating gaussian star at position (x,y) with luminosity L and full-weight at half max fwhm.
    X and Y are the coordinate grid of the image.
    """
    return l*np.exp(-((X-x)**2 + (Y-y)**2)/(fwhm**2))

# ____________________________________________________________________________________________________
# Create sky picture 🌌

def create(
        N         : int   = 100,
        nb_stars  : int   = None,
        fwhm      : float = None,
        mag       : list  = np.arange(0,5),
        mag_prob  : list  = np.ones(5),
        noise_mag : float = None,
        noise_std : float = None,
        mode     : str   = 'sequential'
    ) -> tuple[np.ndarray, list]:
    """
    Create a N*N matrix representing a picture of a sky that contain "nb_stars" stars.
    - "N" is the size of the picture
    - "nb_star" is the number of star. Default: N/2
    - "fwhm" is the full width at half maximum of the stars. Default: N/100
    - "mag" represent the list of possible values for the magnitude of the stars. Default: arange(0,5)
    - "mag_prob" represent the probability associated to each magnitude (must be the same dimension as "mag", will be automatically normalized). Default: ones(5)
    - "noise_mag" is the mean of the gaussian noise. Default: None (no noise)
    - "noise_std" is the standard deviation of the gaussian noise. Default: None (no noise)
    """

    # Defining default values
    if nb_stars is None:
        nb_stars = int(N/10)
    if fwhm is None:
        fwhm = N/100

    # Converting lists to numpy arrays 🚀
    mag = np.array(mag)
    mag_prob = np.array(mag_prob)

    # Defining coordinate grids 🧭
    X, Y = np.meshgrid(np.arange(N),np.arange(N))

    # Normalizing the probabilities 📊
    mag_prob = mag_prob/sum(mag_prob) # normalisation

    # Getting the luminosity for all stars 🔆
    mag_values = np.random.choice(mag, p=mag_prob, size=nb_stars)
    luminosities = mag_to_lum(mag_values)

    # Getting position of all stars 📍
    x = np.random.randint(N, size=nb_stars)
    y = np.random.randint(N, size=nb_stars)

    # Generating all stars (in parrallel) ✨
    with Pool() as p:
        stars = p.starmap(_create_star, zip(x, y, luminosities, [fwhm]*nb_stars, [X]*nb_stars, [Y]*nb_stars))

    # Superposing all stars on the same picture 🌌
    sky = np.sum(stars, axis=0)

    # Adding noise 🔉
    if None not in [noise_mag, noise_std]: 
        noise = np.random.normal(noise_mag, noise_std, (N,N))
        sky += mag_to_lum(noise)

    return sky, list(zip(x, y, mag_values))

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