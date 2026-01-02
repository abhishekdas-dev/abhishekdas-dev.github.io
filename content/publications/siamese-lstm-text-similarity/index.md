---
title: 'Siamese Manhattan LSTM Implementation for Predicting Text Similarity and Grading of Student Test Papers'

# Hide author profile cards at bottom
profile: false

# Authors
# If you created a profile for a user (e.g. the default `me` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - me
  - Wallace Dalmet
  - Vivek Dhuri
  - Moinuddin Khaja
  - Sunil H. Karamchandani

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'
  - 'Equal contribution'
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

abstract: This paper presents a method to grade answer papers written by the students by assessing the semantic similarity between the written answers and the actual answers and grading them accordingly based on the amount of semantic similarity between the two. There is a need for automatic grading of answers for faster checking of papers and to reduce the work of the teachers, also the method of text similarity can be used in search engines to find a particular document on the Internet or by question-answer sites such as Quora to determine similar questions. We have implemented this by using Manhattan LSTM (Long short-term memory) which is a Siamese deep neural network. This method uses word embedding vectors to create embedded matrices which are fed to LSTM and similarity function to get the result of the similarity between answers and then scaled to the appropriate grade.

# Summary. An optional shortened abstract.
summary: This paper presents a method to grade answer papers written by the students by assessing the semantic similarity between the written answers and the actual answers and grading them accordingly based on the amount of semantic similarity between the two.

tags:
  - Deep Learning
  - NLP
  - LSTM

# Display this page in the Featured widget?
featured: true

# Custom links
links:
  - type: url
    name: Springer Chapter
    url: https://link.springer.com/chapter/10.1007/978-981-15-1002-1_60

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Siamese Deep Neural Network Architecture'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
projects: []
---

This paper presents a method to grade answer papers written by the students by assessing the semantic similarity between the written answers and the actual answers and grading them accordingly based on the amount of semantic similarity between the two.

## Key Contributions

- Implemented Manhattan LSTM (Long short-term memory) which is a Siamese deep neural network
- Used word embedding vectors to create embedded matrices for semantic comparison
- Demonstrated practical applications for automatic grading and question-answer similarity detection
