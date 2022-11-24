from src.sky import Sky
from src.pupil import Pupil
from src.shot import Shot
config = __import__("0-Config")

for i in range(config.number_of_images):
    sky = Sky(N=config.N, nb_stars=config.nb_stars, fwhm=config.fwhm, mag=config.mag, mag_prob=config.mag_prob, noise_mag=config.noise_mag, noise_std=config.noise_std)
    pupil = Pupil(config.N, config.pupil_radius, config.obstruction_radius, config.arms_count, config.arms_size, config.arms_angle)
    shot = Shot(sky, pupil)