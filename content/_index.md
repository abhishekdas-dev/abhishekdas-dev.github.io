---
# Leave the homepage title empty to use the site title
title: ''
summary: ''
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: '6rem'

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: me
      text: ''
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
      headings:
        about: 'About'
        education: ''
        interests: ''
        bio: ''
    design:
      # Use the new Gradient Mesh which automatically adapts to the selected theme colors
      background:
        gradient_mesh:
          enable: true

      # Name heading sizing to accommodate long or short names
      name:
        size: md # Options: xs, sm, md, lg (default), xl

      # Avatar customization
      avatar:
        size: medium # Options: small (150px), medium (200px, default), large (320px), xl (400px), xxl (500px)
        shape: circle # Options: circle (default), square, rounded
  - block: collection
    id: papers
    content:
      title: Featured Work (Publications & Patents)
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: article-grid
      columns: 2
  - block: collection
    id: talks
    content:
      title: Talks
      filters:
        folders:
          - events
    design:
      view: card
  - block: collection
    id: news
    content:
      title: Selected Writings
      subtitle: ''
      text: ''
      # Page type to display. E.g. post, talk, publication...
      page_type: blog
      # Choose how many pages you would like to display (0 = all pages)
      count: 10
      # Filter on criteria
      filters:
        author: ''
        category: ''
        tag: ''
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ''
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: article-grid
      columns: 3
  - block: collection
    id: all-publications
    content:
      title: All Publications, Patents & Writing
      text: |
        [![Google Scholar Citations](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fabhishekdas-dev%2Fabhishekdas-dev.github.io%2Fmain%2Fscholar.json&query=%24.citations&label=Citations&color=1a73e8&logo=googlescholar&logoColor=white&style=flat-square&cacheSeconds=1800)](https://scholar.google.com/citations?user=e3bDokMAAAAJ&hl=en) [![h-index](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Fabhishekdas-dev%2Fabhishekdas-dev.github.io%2Fmain%2Fscholar.json&query=%24.hindex&label=h-index&color=1a73e8&logo=googlescholar&logoColor=white&style=flat-square&cacheSeconds=1800)](https://scholar.google.com/citations?user=e3bDokMAAAAJ&hl=en)
      count: 0
      filters:
        folders:
          - publications
        exclude_featured: false
    design:
      view: citation
---
