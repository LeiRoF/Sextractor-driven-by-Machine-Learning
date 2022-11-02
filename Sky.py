from numpy import *
from scipy.ndimage.interpolation import rotate

def create(
        N         : int   = 100,
        nb_stars  : int   = None,
        fwhm      : float = None,
        mag       : list  = arange(0,5),
        mag_prob  : list  = ones(5),
        noise_mag : float = None,
        noise_std : float = None
    ) -> tuple[ndarray, list]:
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

    if nb_stars is None: nb_stars = int(N/10)
    if fwhm is None: fwhm = N/100

    sky = zeros((N, N))

    X, Y = meshgrid(arange(N),arange(N))

    starList = []

    mag = array(mag)
    mag_prob = array(mag_prob)
    mag_prob = mag_prob/sum(mag_prob) # normalisation

    for i in range(nb_stars):

        # Getting the position
        x = random.randint(N)
        y = random.randint(N)

        # Getting the magnitude:
        mag_value = random.choice(mag, p=mag_prob)
        L = 10**(-mag_value/2.5)

        # Placing the star
        sky += L*exp(-((X-x)**2 + (Y-y)**2)/(fwhm**2))

        starList.append((x,y, mag))

    if noise_mag is not None and noise_std is not None: 
        noise = random.normal(noise_mag, noise_std, (N,N))
        sky += 10**(-noise/2.5)

    return sky, starList

if __name__ == "__main__":

    shot, starList = create(
        1000, # Image size
        nb_stars=100, # Number of stars
        fwhm=3, # fwhm of all stars
        mag=arange(0,30), # possible magnitudes of the stars
        mag_prob=arange(1,31)**2, # probability associated to each magnitude
        noise_mag=10, # mean of the gaussian noise
        noise_std=0.1 # standard deviation of the gaussian noise
    )