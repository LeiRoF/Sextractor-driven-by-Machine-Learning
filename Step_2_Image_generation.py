import numpy as np
import os
import Step_0_Config as config
from src.shot import Shot
from src.pupil import Pupil
from src.sky import Sky
<<<<<<< HEAD

if not os.path.exists(config.path):
    os.makedirs(config.path)
=======
>>>>>>> c2b87e0c12f0864061ca4daa02ace67056400dee

for i in range(config.number_of_images):
    print(f"⚙️ Generating image {i+1} of {config.number_of_images}")
    sky = Sky(N=config.N, nb_stars=config.nb_stars, fwhm=config.fwhm, mag=config.mag, mag_prob=config.mag_prob, noise_mag=config.noise_mag, noise_std=config.noise_std)
    pupil = Pupil(config.N, config.pupil_radius, config.obstruction_radius, config.arms_count, config.arms_size, config.arms_angle)
    shot = Shot(sky, pupil)
    shot.save_ai_ready(os.path.join(config.path, f"shot_{np.random.randint(999999):d}"))