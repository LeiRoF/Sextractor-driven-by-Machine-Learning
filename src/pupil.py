import numpy as np
from scipy.ndimage.interpolation import rotate
import matplotlib.pyplot as plt

# ____________________________________________________________________________________________________
# Pupil object 🔭

class Pupil:
    def __init__(
        self,
        N                  :int,
        radius             :float,
        obstruction_radius :float  = 0,
        arms_count         :int    = 0,
        arms_size          :float  = 1,
        arms_angle         :float  = 0
    ):
        self.N = N
        self.radius = radius
        self.obstruction_radius = obstruction_radius
        self.arms_count = arms_count
        self.arms_size = arms_size
        self.arms_angle = arms_angle
        self.picture = create(N, radius, obstruction_radius, arms_count, arms_size, arms_angle)
        self.diffraction_profile = diffraction_profile(self.picture)

    def _imshow(self):
        plt.figure(figsize=(10,10))
        plt.imshow(self.picture, cmap='gray')
        plt.title("Pupil")
        plt.colorbar()

    def _imshow_diffraction_profile(self):
        plt.figure(figsize=(10,10))
        plt.imshow(np.log(abs(self.diffraction_profile)), cmap='gray')
        plt.title("Pupil diffraction profile")
        plt.colorbar()

    def show(self):
        self._imshow()
        plt.show()

    def show_diffraction_profile(self):
        self._imshow_diffraction_profile()
        plt.show()

    def save(self, path):
        self._imshow()
        plt.savefig(path)
    
    def save_diffraction_profile(self, path):
        self._imshow_diffraction_profile()
        plt.savefig(path)

# ____________________________________________________________________________________________________
# Generating pupil image 🔭

def create(
    N                  :int,
    radius             :float,
    obstruction_radius :float  = 0,
    arms_count         :int    = 0,
    arms_size          :float  = 1,
    arms_angle         :float  = 0
) -> np.ndarray:
    """
    Create a N*N matrix containing a picture of a pupil.
    0 mean that the pixel is situated on an opaque part.
    1 mean that the pixel is situated on a transparent part.
    """

    # Init frame 🖼
    pupil = np.ones((N, N))

    # Creating coordinate grids 🧭
    X, Y = np.meshgrid(np.arange(N), np.arange(N))

    # Create the main pupil (= primary mirror shape) ⬜
    pupil *= np.sqrt((X-N/2)**2 + (Y-N/2)**2) < radius

    # Create the central obstruction 🔳
    pupil *= np.sqrt((X-N/2)**2 + (Y-N/2)**2) > obstruction_radius

    # Create spider's arms 🕷️
    for i in np.arange(arms_count):
        pupil *= rotate(
            ((abs(Y - N/2) > arms_size) + (X - N/2 < 0)).astype(int), # Generating horizontal arm with constrained height and defined in X positive
            arms_angle + i/arms_count*360, # Then rotating the arm
            reshape=False
        )

    return pupil

# ____________________________________________________________________________________________________
# Diffraction profile 〰️

def diffraction_profile(pupil_picture):
    """
    Compute the diffraction profile of a pupil.
    """
    N = pupil_picture.shape[0]
    diffraction_profile = np.roll(np.fft.fft2(pupil_picture), (N//2, N//2), (0,1))
    return diffraction_profile

# ____________________________________________________________________________________________________
# Test zone 🧪

if __name__ == "__main__":

    # Generating pupil 🔭
    pupil = Pupil(
        N = 1001,
        radius = 400,
        obstruction_radius = 200,
        arms_count = 3,
        arms_size = 50,
        arms_angle = 90
    )

    # Showing picture 📸
    pupil.show()