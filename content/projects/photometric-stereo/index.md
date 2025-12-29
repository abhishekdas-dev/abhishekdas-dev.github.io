---
title: 'Photometric Stereo'
summary: Python, NumPy, Matplotlib, Scikit-image
tags:
  - Computer Vision
date: '2020-05-12T00:00:00Z'

image:
  caption: 'normals_enforced'
  focal_point: Smart

featured: true

gallery_item:
  - album: photometric-stereo
    image: albedoIm.png
    caption: Albedo Image, visualized with colormap 'gray'
  - album: photometric-stereo
    image: normalIm.png
    caption: Normal Image, visualized with colormap 'rainbow'
  - album: photometric-stereo
    image: depthmapuncalibone.png
    caption: Depthmap View 1, visualized with Axes3D object in Matplotlib
  - album: photometric-stereo
    image: depthmapuncalibtwo.png
    caption: Depthmap View 2, visualized with Axes3D object in Matplotlib
  - album: photometric-stereo
    image: depthmapuncalibthree.png
    caption: Depthmap View 3, visualized with Axes3D object in Matplotlib
  - album: photometric-stereo
    image: depthmapuncalibfour.png
    caption: Depthmap View 4, visualized with Axes3D object in Matplotlib
---

#### What we did
- Estimated Pseudonormals, and visualized the Albedo, Normal images and Shape of the face  
- Understanding and Rendering of n-dot-l Lighting

<br>

### Image gallery
{{< gallery album="photometric-stereo" >}}

<br>
<br>

#### Rendering n-dot-l lighting for a uniform fully reflective Lambertian sphere
{{< figure src="ndotl.png" title="Rendered images for 3 different light sources" >}}  

<br>
<br>

Acknowledgements - This project is done as a part of the course curriculum in 16-720:Computer Vision @ Carnegie Mellon University
