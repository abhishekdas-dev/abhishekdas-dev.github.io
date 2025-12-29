---
title: "Research Ideas for the Facebook Hateful Memes Challenge"

event: "Hateful Memes Challenge session @ NeurIPS - Contributed Talks"
event_url: https://ai.facebook.com/blog/hateful-memes-challenge-and-data-set/

location: Virtual

summary: "We present Object Detection based Image Captioning, and Sentiment Analysis as our two research ideas to enhance performance against the adversarial examples introduced in the Hateful Meme challenge dataset."
abstract: |
  We propose two research ideas which when integrated into a Multimodal model, aims to learn the context behind the combination of text and captions used. Our first idea is to use Image Captioning as a medium for introducing outside world knowledge to our model. The highly confident error cases of the multimodal baselines show that the models tend to focus more on the text modality for predictions. Our focus in using this approach is to find a deeper relationship between the text and the image modalities by bringing the visual modality and finding its "actual caption" and parallelly sending the image representation along with the pre-extracted caption representation for the concatenation step. Moreover, comparing the "actual caption" with the "pre-extracted caption" of the meme will help in understanding whether both are aligned or not because in many cases a hateful image is turned benign just by declaring what is happening in the image. Our second approach is to use sentiment analysis on both Image and Text modalities. Instead of only using multimodal representations obtained from pre-trained neural networks, we also include the unimodal sentiment to enrich the features. The intuition for this idea is that current pre-trained representations, like VisualBERT and ViLBERT, have the objective of predicting the semantic correlation between image and text, but semantic information is difficult to capture and may not be enough for solving our task. We try to include high-level features like text and image sentiments because sentiment analysis is a related but relatively simple task.

# Talk start and end times.
date: '2020-12-11T18:00:00Z'
all_day: false

publishDate: '2017-01-01T00:00:00Z'

authors:
  - me
  - Japsimar Singh Wahi

tags:
  - Deep Learning
  - NLP
  - Computer Vision
  - Multimodal Learning

featured: true

image:
  caption: 'Hateful Memes Challenge @ NeurIPS 2020'
  focal_point: Smart

links:
  - icon: brands/github
    name: Code
    url: https://github.com/Abhishek0697/Detection-of-Hate-Speech-in-Multimodal-Memes
  - icon: file-pdf
    name: Paper
    url: https://arxiv.org/pdf/2012.14891.pdf

projects:
  - detecting-hate-speech-multimodal-memes
---

## Talk Overview

This talk was presented at the **Hateful Memes Challenge session @ NeurIPS 2020** as a contributed talk.

### Key Research Ideas

1. **Object Detection based Image Captioning**: Using image captioning to introduce outside world knowledge and find deeper relationships between text and image modalities.

2. **Sentiment Analysis on Both Modalities**: Including high-level features like text and image sentiments to enrich the multimodal representations.

### Related Project

This talk is based on our project [Detecting Hate Speech in Multi-modal Memes](/projects/detecting-hate-speech-multimodal-memes/).
