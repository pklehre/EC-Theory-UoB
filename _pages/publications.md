---
layout: page
permalink: /publications/
title: Publications
description: Publications in reversed chronological order.
nav: true
nav_order: 3
---
<!-- _pages/publications.md -->
<div class="publications">

{%- assign start_year = 2000 %}
{%- assign end_year = 2500 %}

{%- for y in (start_year..end_year) reversed %}

  {%- capture bib_entries %}
    {% bibliography -f {{ site.scholar.bibliography }} -q @*[year={{ y }}]* %}
  {%- endcapture %}
  {%- if bib_entries.size > 35 %}
    <h2 class="year">{{ y }}</h2>
    {% bibliography -f {{ site.scholar.bibliography }} -q @*[year={{ y }}]* %}
  {%- endif %}
{%- endfor %}

</div>