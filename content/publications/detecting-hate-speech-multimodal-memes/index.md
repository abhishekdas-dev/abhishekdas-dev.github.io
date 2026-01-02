---
title: 'Detecting Hate Speech in Multi-modal Memes'

# Authors
authors:
  - me
  - Japsimar Singh Wahi
  - Siyao Li

date: '2022-01-01T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2022-01-01T00:00:00Z'

# Publication type.
publication_types: ['article']

# Publication name and optional abbreviated publication name.
publication: arXiv preprint arXiv:2012.14891
publication_short: arXiv 2012.14891

abstract: In the past few years, there has been a surge of interest in multi-modal problems, from image captioning to visual question answering and beyond. In this paper, we focus on hate speech detection in multi-modal memes wherein memes pose an interesting multi-modal fusion problem. We aim to solve the Facebook Meme Challenge which aims to solve a binary classification problem of predicting whether a meme is hateful or not. A crucial characteristic of the challenge is that it includes "benign confounders" to counter the possibility of models exploiting unimodal priors. We explore the visual modality using object detection and image captioning models to fetch the "actual caption" and then combine it with the multi-modal representation to perform binary classification. Another approach we experiment with is to improve the prediction with sentiment analysis.

# Summary. An optional shortened abstract.
summary: A multi-modal approach to detect hate speech in memes using object detection, image captioning, and sentiment analysis for the Facebook Hateful Memes Challenge.

tags:
  - Deep Learning
  - NLP
  - Computer Vision
  - Multimodal Learning

# Display this page in the Featured widget?
featured: true

# Custom links
links:
  - type: url
    name: arXiv
    url: https://arxiv.org/abs/2012.14891
  - type: url
    name: PDF
    url: https://arxiv.org/pdf/2012.14891

# Featured image
image:
  caption: 'Multimodal Hate Speech Detection'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
projects:
  - detecting-hate-speech-multimodal-memes
---

We focus on hate speech detection in multi-modal memes wherein memes pose an interesting multi-modal fusion problem. We aim to solve the Facebook Meme Challenge which aims to solve a binary classification problem of predicting whether a meme is hateful or not.

## Key Contributions

- Explored visual modality using object detection and image captioning models
- Combined "actual caption" with multi-modal representation for binary classification
- Tackled benign text confounders present in the dataset
- Enriched features using unimodal sentiment analysis
