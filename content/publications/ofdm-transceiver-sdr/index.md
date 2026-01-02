---
title: 'Study of Performance of an OFDM Transceiver Using SDR Platform'

# Hide author profile cards at bottom
profile: false

# Authors
# If you created a profile for a user (e.g. the default `me` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - me
  - V. Venkataramanan

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

date: '2019-11-17T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2019-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of International Conference on Wireless Communication, (ICWiCOM 2019)*
publication_short: In *ICWiCOM 2019*

abstract: One of the most extensively used modulation scheme in digital communication is orthogonal frequency-division multiplexing (OFDM) in which the data to be transmitted is encoded on multiple carrier frequencies. Fast Fourier transform is used in OFDM due to which the subcarriers can overlap with each other and transmit, without loss in information. The performance using OFDM systems is good in multipath environments due to the fact that the subcarriers are transmitted at a lower data rate. The peak-to-average power ratio (PAPR) for an OFDM signal is large, which is a disadvantage in the current OFDM technology. The signal at the transmitter can be clipped before amplifying in order to reduce the effect of PAPR. In addition to this, OFDM also suffers with the problems of channel fading, phase noise, phase distortion, and image rejection. In this study of OFDM transreceivers, with the help of GNU Radio Companion and SDR, we have made an attempt to create a simulation environment similar to real-time channel conditions, by considering the parameters such as bit error rate, channel fading losses, and Doppler spread, and analysed the performance of OFDM transreceiver system.

# Summary. An optional shortened abstract.
summary: In this study of OFDM transreceivers, with the help of GNU Radio Companion and SDR, we have made an attempt to create a simulation environment similar to real-time channel conditions.

tags:
  - Wireless Communication
  - SDR
  - OFDM

# Display this page in the Featured widget?
featured: false

# Custom links
links:
  - type: url
    name: Springer Chapter
    url: https://link.springer.com/chapter/10.1007/978-981-15-1002-1_38

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: ''
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
projects: []
---

One of the most extensively used modulation scheme in digital communication is orthogonal frequency-division multiplexing (OFDM) in which the data to be transmitted is encoded on multiple carrier frequencies.

## Key Contributions

- Created a simulation environment using GNU Radio Companion and SDR
- Analyzed performance considering bit error rate, channel fading losses, and Doppler spread
- Investigated solutions for PAPR reduction in OFDM systems
