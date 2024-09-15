---
layout: distill
title: Coevolutionary algorithms (simulations on two benchmark problems)
description: Simulations of several coevolutionary algorithms on two benchmark problems
giscus_comments: false
date: 2024-09-14

authors:
  - name: Mario A. Hevia Fajardo
    url: "https://mhevia.com"
    affiliations:
      name: University of Birmingham, Birmingham
  - name: Per Kristian Lehre
    url: https://www.cs.bham.ac.uk/~lehrepk/
    affiliations:
      name: University of Birmingham, Birmingham

# bibliography: 2018-12-22-distill.bib

# Optionally, you can add a table of contents to your post.
# NOTES:
#   - make sure that TOC names match the actual section names
#     for hyperlinks within the post to work correctly.
#   - we may want to automate TOC generation in the future using
#     jekyll-toc plugin (https://github.com/toshimaru/jekyll-toc).
toc:
  - name: Bilinear
      # - name: PDCoEA
      # - name: RankDiv CoEA
      # - name: (1,λ) CoEA with worst case fitness aggregation
      # - name: (1,λ) CoEA with average fitness aggregation
      # - name: (1+1) RLS CoEA
  - name: Diagonal
      # - name: (1,λ) CoEA with average fitness aggregation
      # - name: (1+1) RLS CoEA
      # - name: IPCA

# Below is an example of injecting additional post-specific styles.
# If you use this post as a template, delete this _styles block.
_styles: >
  .fake-img {
    background: #bbb;
    border: 1px solid rgba(0, 0, 0, 0.1);
    box-shadow: 0 0px 4px rgba(0, 0, 0, 0.1);
    margin-bottom: 12px;
  }
  .fake-img p {
    font-family: monospace;
    color: white;
    text-align: left;
    margin: 12px 0;
    text-align: center;
    font-size: 16px;
  }

---

*** 

## Bilinear

### PDCoEA


<div class="l-page" style="display: flex; justify-content: center; align-items: center;">
  <iframe src="{{ '/assets/plotly/pdcoea_animation.html' | relative_url }}" frameborder='0' scrolling='no' height="550px" width="70%" style="border: 1px dashed grey;"></iframe>
</div>

### RankDiv CoEA

<div class="l-page" style="display: flex; justify-content: center; align-items: center;">
  <iframe src="{{ '/assets/plotly/rankdivcoea_animation.html' | relative_url }}" frameborder='0' scrolling='no' height="550px" width="70%" style="border: 1px dashed grey;"></iframe>
</div>

### (1,λ) CoEA with average fitness aggregation

<div class="l-page" style="display: flex; justify-content: center; align-items: center;">
  <iframe src="{{ '/assets/plotly/onecommalambdaavg.html' | relative_url }}" frameborder='0' scrolling='no' height="550px" width="70%" style="border: 1px dashed grey;"></iframe>
</div>

### (1,λ) CoEA with worst case fitness aggregation

<div class="l-page" style="display: flex; justify-content: center; align-items: center;">
  <iframe src="{{ '/assets/plotly/onecommalambdaworst.html' | relative_url }}" frameborder='0' scrolling='no' height="550px" width="70%" style="border: 1px dashed grey;"></iframe>
</div>

### (1+1) RLS-PDCoEA 

<div class="l-page" style="display: flex; justify-content: center; align-items: center;">
  <iframe src="{{ '/assets/plotly/rlspd.html' | relative_url }}" frameborder='0' scrolling='no' height="550px" width="70%" style="border: 1px dashed grey;"></iframe>
</div>

## Diagonal

### IPCA

<div class="l-page" style="display: flex; justify-content: center; align-items: center;">
  <iframe src="{{ '/assets/plotly/ipcadiagonal.html' | relative_url }}" frameborder='0' scrolling='no' height="550px" width="70%" style="border: 1px dashed grey;"></iframe>
</div>

### (1,λ) CoEA with average fitness aggregation

<div class="l-page" style="display: flex; justify-content: center; align-items: center;">
  <iframe src="{{ '/assets/plotly/onecommalambdaavgdiagonal.html' | relative_url }}" frameborder='0' scrolling='no' height="550px" width="70%" style="border: 1px dashed grey;"></iframe>
</div>

### (1+1) RLS-PDCoEA 

<div class="l-page" style="display: flex; justify-content: center; align-items: center;">
  <iframe src="{{ '/assets/plotly/rlspddiagonal.html' | relative_url }}" frameborder='0' scrolling='no' height="550px" width="70%" style="border: 1px dashed grey;"></iframe>
</div>