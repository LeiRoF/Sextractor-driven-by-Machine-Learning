from numpy import *
from scipy.ndimage.interpolation import rotate
from numba import njit, jit

@jit(nopython=True, cache=True, parrallel=True)
def create(N, radius, obstruction_radius=None, arms_count=None, arms_size=1, arms_angle=0):
    """Create a N*N matrix containing a picture of a pupil.
    0 mean that the pixel is situated on an opaque part.
    1 mean that the pixel is situated on a transparent part."""

    pupil = ones((N, N))

    X, Y = meshgrid(arange(N),arange(N))

    # Create the main pupil
    pupil *= sqrt((X-N/2)**2 + (Y-N/2)**2) < radius

    # Create the obstruction
    if obstruction_radius is not None:
        pupil *= sqrt((X-N/2)**2 + (Y-N/2)**2) > obstruction_radius

    # Create the arms
    if arms_count is not None:
        angle = arms_angle
        for i in arange(arms_count):
            pupil *= abs(Y - N/2) > arms_size
            pupil = rotate(pupil, 360/arms_count, reshape=False)

    return pupil