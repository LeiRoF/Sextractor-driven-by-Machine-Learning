import os
import numpy as np
from PIL import Image

def format_star_to_xml(star, fwhm):
    base =\
"""
        <name>star</name>
            <pose>Unspecified</pose>
            <truncated>Unspecified</truncated>    
            <difficult>Unspecified</difficult>
            <bndbox>
                <xmin>{x1}</xmin>
                <ymin>{y1}</ymin>
                <xmax>{x2}</xmax>
                <ymax>{y2}</ymax>
            </bndbox>
"""
    return base.format(x1=star[0]-fwhm, y1=star[1]-fwhm, x2=star[2]+fwhm, y2=star[3]+fwhm)



def format_image_to_xml(path, stars, fwhm, size=None):
    
    base =\
"""
<annotation>
    <folder>{folder}</folder>
    <filename>{filename}</filename>
    <path>{path}</path>
    <source>
        <database>Unknown</database>
    </source>
    <size>
        <width>{width}</width>
        <height>{height}</height>
        <depth>1</depth>
    </size>
    <object>
{objects}
    </object>
</annotation>
"""
    
    if size is None:
        im = Image.open('data/src/lena.jpg')
        width, height = im.size 
        im.close()
    else:
        width, height = size

    return base.format(
        folder=os.path.split(path)[0],
        filename=os.path.split(path)[1],
        path=path,
        width=width,
        height=height,
        objects= "\n".join([format_star_to_xml(star, fwhm) for star in stars])
    )

def format_filename(filename, config):
    return filename.format(
        i=config.i,
        N=config.N,
        n=config.nb_stars,
        f=config.fwhm,
        s=config.noise_mag,
        M=np.max(config.mag),
        m=np.min(config.mag)
    )