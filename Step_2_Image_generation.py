import numpy as np
import os
import Step_0_Config as config
from src.shot import Shot
from src.pupil import Pupil
from src.sky import Sky
from LRFutils import progress

if not os.path.exists(config.path):
    os.makedirs(config.path)

bar = progress.Bar(config.number_of_images, "⚙️ Generating images")

for i in range(config.number_of_images):

    r = np.random.rand()
    if r < config.train_fraction:
        mode = "train"
        path = os.path.join(config.path, "train")
    elif r < config.train_fraction + config.validation_fraction:
        mode = "validation"
        path = os.path.join(config.path, "validation")
    else:
        mode = "test"
        path = os.path.join(config.path, "test")

    if not os.path.isdir(path):
        os.makedirs(path)

    bar(i+1, prefix=f"⚙️ Generating images ({mode})")
    sky = Sky(N=config.N, nb_stars=config.nb_stars, fwhm=config.fwhm, mag=config.mag, mag_prob=config.mag_prob, noise_mag=config.noise_mag, noise_std=config.noise_std)
    pupil = Pupil(config.N, config.pupil_radius, config.obstruction_radius, config.arms_count, config.arms_size, config.arms_angle)
    shot = Shot(sky, pupil)
    shot.save_ai_ready(os.path.join(path, f"shot_{np.random.randint(999999):d}"))