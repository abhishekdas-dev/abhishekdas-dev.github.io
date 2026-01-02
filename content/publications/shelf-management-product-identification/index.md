---
title: 'System and Method for Identifying Products in a Shelf Management System'

# Hide author profile cards at bottom
profile: false

# Authors
authors:
  - Marios Savvides
  - Uzair Ahmed
  - Sreena Nallamothu
  - Magesh Kannan
  - me

# Author notes (optional)
author_notes:
  - ''
  - ''
  - ''
  - ''
  - ''

date: '2022-02-17T00:00:00Z'

# Schedule page publish date (NOT publication's date).
publishDate: '2022-02-17T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['patent']

# Publication name and optional abbreviated publication name.
publication: United States Patent Application US20220051179A1
publication_short: US Patent US20220051179A1

abstract: Disclosed herein is a system and method of identifying products on a retail shelf using a feature extractor trained to extract features from images of products on the shelf and output identifying information regarding the product in the product image. The extracted features are compared to extracted features in a feature gallery library and a best fit match is obtained. A product ID is then assigned to the image of the product and the assigned product ID is validated by matching the product ID with product identifying information extracted from a shelf label associated with the image of the product.

# Summary. An optional shortened abstract.
summary: A system and method for automated product identification on retail shelves using deep learning feature extraction and matching against a product gallery library.

tags:
  - Computer Vision
  - Deep Learning
  - Retail Automation
  - Patent

# Display this page in the Featured widget?
featured: true

# Custom links
links:
  - type: url
    name: Google Patents
    url: https://patents.google.com/patent/US20220051179A1/en

# Featured image
image:
  caption: 'Shelf Management Product Identification System'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
projects: []
---

## Overview

This patent describes an automated inventory monitoring system using autonomous robots with multiple cameras to navigate retail store aisles and identify products on shelves. The system uses deep learning-based feature extraction to match product images against a feature gallery library for accurate product identification.

## Key Innovations

- **Multi-layer Feature Extractor**: A deep learning model trained to extract discriminative features from product images for identification
- **Feature Gallery Library**: A database containing extracted features from product images with associated product IDs
- **Product-Label Association**: Logic to associate detected products with their corresponding shelf labels based on spatial positioning
- **Misplaced Product Detection**: Capability to identify plugs (misplaced products) and spreads (products encroaching on adjacent shelf space)
- **Autonomous Robot Platform**: Mobile robot with multiple cameras and sensors for continuous shelf monitoring

## Assignee

Carnegie Mellon University, Pittsburgh, Pennsylvania
