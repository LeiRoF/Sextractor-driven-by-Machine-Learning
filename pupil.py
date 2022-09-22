from numpy import *
from scipy.ndimage.interpolation import rotate

def create(N, radius, obstruction_radius=None, arms_count=None, arms_size=1, arms_angle=0):
    """Create a N*N matrix containing a picture of a pupil.
    0 mean that the pixel is situated on an opaque part.
    1 mean that the pixel is situated on a transparent part."""

    pupil = ones((N, N))

    X = ones(N).reshape((N, 1)).dot(arange(N).reshape((1, N)))
    Y = arange(N).reshape((N, 1)).dot(ones(N).reshape((1, N)))

    # # Create the main pupil
    pupil *= sqrt((X-N/2)**2 + (Y-N/2)**2) < radius

    # # Create the obstruction
    if obstruction_radius is not None:
        pupil *= sqrt((X-N/2)**2 + (Y-N/2)**2) > obstruction_radius

    # # Create the arms
    if arms_count is not None:
        angle = arms_angle
        for i in arange(arms_count):
            pupil *= abs((X - N/2)*cos(angle) + (Y - N/2)*sin(angle)) > arms_size
            pupil = rotate(pupil, 360/arms_count, reshape=False)

    return pupil
