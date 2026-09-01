---
layout: page
title: Complex Landscapes
description: Tutorial on Theory of Evolutionary Algorithms on Complex Landscapes
permalink: /ComplexLandscapesTutorial/
news: false  # includes a list of news items
latest_posts: false  # includes a list of the newest posts
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false  # includes social icons at the bottom of the page
---

(Presented at PPSN 2026 in Trento, Italy.)

**Authors**

 - Per Kristian Lehre and Duc-Cuong Dang

**Resources**

 - [Slides](../assets/pdf/ppsn2026-tutorial.pdf)


**Some References**

 - [Algorithmica SLO paper](https://link.springer.com/article/10.1007/s00453-025-01359-z)
 - [TELO MOEA paper](https://dl.acm.org/doi/10.1145/3732793)
 - [Algorithmica paper on MOEA black box](https://link.springer.com/article/10.1007/s00453-026-01403-6)

**Acknowledgements**

Research supported by UKRI/EPSRC
through a [Turing AI Acceleration
Fellowship](https://www.gov.uk/government/publications/turing-artificial-intelligence-fellowships/turing-artificial-intelligence-fellowships).


<div class="d-flex flex-wrap align-content-stretch justify-content-center m-n2 pt-5 no-gutters">
    {% for member in members %}
        {% assign colsMod6 = forloop.length | modulo: 6 %}
        {% assign colIdMod4 = forloop.index | modulo: 4 %}
        {% if colsMod6 == 1 and colIdMod4 == 1 %}<div class="col-md-2 w-100"></div>{% endif %}
        <div class="col-6 col-sm-3 col-md-2 mb-3">
            {% if member.profile.website %}<a href="{{ member.profile.website }}" class="no-decoration">{% endif %}
                <div class="card hoverable h-100 m-2">
                    <img src="{{ '/assets/img/' | append: member.profile.image | relative_url }}" class="card-img-top" alt="{{ member.profile.name }}" />
                    <div class="card-body p-2">
                        <div class="card-title m-0">{{ member.title }}</div>
                    </div>
                </div>
            {% if member.profile.website %}</a>{% endif %}
        </div>
    {% endfor %}
</div>
