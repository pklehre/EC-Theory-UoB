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

![PDCoEA](/assets/img/pdcoea-pseudocode.png)
![RankDivCoEA](/assets/img/rankdivcoea-pseudocode.png)
![IPCA](/assets/img/ipca-pseudocode.png)


## Bilinear

<a href="{{ '/assets/plotly/pdcoea_animation.html' | relative_url }}" target="Bilinear">
  <button class="styled-button">PDCoEA</button>
</a>
<a href="{{ '/assets/plotly/rankdivcoea_animation.html' | relative_url }}" target="Bilinear">
  <button class="styled-button">RankDiv CoEA</button>
</a>
<a href="{{ '/assets/plotly/onecommalambdaavg.html' | relative_url }}" target="Bilinear">
  <button class="styled-button">(1,λ) CoEA with average fitness aggregation</button>
</a>
<a href="{{ '/assets/plotly/onecommalambdaworst.html' | relative_url }}" target="Bilinear">
  <button class="styled-button">(1,λ) CoEA with worst case fitness aggregation</button>
</a>
<a href="{{ '/assets/plotly/rlspd.html' | relative_url }}" target="Bilinear">
  <button class="styled-button">(1+1) RLS-PDCoEA</button>
</a>

<div class="l-page" style="display: flex; justify-content: center; align-items: center;">
  <iframe name="Bilinear" src="about:blank" frameborder='0' scrolling='no' height="550px" width="70%" style="border: 1px dashed grey;"></iframe>
</div>

## Diagonal

<a href="{{ '/assets/plotly/ipcadiagonal.html' | relative_url }}" target="Diagonal">
  <button class="styled-button">IPCA</button>
</a>
<a href="{{ '/assets/plotly/pdcoeadiagonal.html' | relative_url }}" target="Diagonal">
  <button class="styled-button">PDCoEA</button>
</a>
<a href="{{ '/assets/plotly/onecommalambdaavgdiagonal.html' | relative_url }}" target="Diagonal">
  <button class="styled-button">(1,λ) CoEA with average fitness aggregation</button>
</a>
<a href="{{ '/assets/plotly/rlspddiagonal.html' | relative_url }}" target="Diagonal">
  <button class="styled-button">(1+1) RLS-PDCoEA</button>
</a>

<div class="l-page" style="display: flex; justify-content: center; align-items: center;">
  <iframe name="Diagonal" src="about:blank" frameborder='0' scrolling='no' height="550px" width="70%" style="border: 1px dashed grey;"></iframe>
</div>


<style>
  .styled-button {
    background-color: #4CAF50; /* Green background */
    border: none;
    color: white; /* White text */
    padding: 10px 16px; /* Padding for button size */
    text-align: center; /* Center the text */
    text-decoration: none; /* No underline on the text */
    display: inline-block; /* Inline-block to keep button style */
    font-size: 16px; /* Font size */
    margin: 20px 10px; /* Some margin for spacing */
    cursor: pointer; /* Cursor changes to pointer on hover */
    border-radius: 6px; /* Rounded corners */
    transition: background-color 0.3s ease; /* Smooth transition effect */
  }
  
  .styled-button:hover {
    background-color: #45a049; /* Darker green on hover */
  }
</style>
