---
layout: about
title: Home
permalink: /
subtitle: 

profile:
  align: right
  address: >
    <p>School of Computer Science</p>
    <p>University of Birmingham</p>
    <p>Edgbaston</p>
    <p>Birmingham</p>
    <p>B15 2TT</p>
    <p>United Kingdom</p>

news: false  # includes a list of news items
latest_posts: false  # includes a list of the newest posts
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false  # includes social icons at the bottom of the page
---

{: style="text-align:center"}
![GECCO 2023 in Lisbon](assets/img/group-picture-lisbon-small.jpg){: width="800" .rounded}

We do fundamental research in the theory of optimisation, particularly
evolutionary computation. Our research methodology is based on
rigorous mathematical analysis of evolutionary processes, and the
application of insights from this analysis to the design of improved
optimisation algorithms with provable performance bounds.

We have developed an analytical toolbox which allows us to prove upper
and lower bounds on the runtime (computational complexity) of
realistic evolutionary algorithms, including

 - [The level-based theorem](https://ieeexplore.ieee.org/document/8039236) (upper bounds)
 - The negative drift theorem for populations (lower bounds)

Runtime bounds give insight into how the performance of evolutionary
algorithms depends on the structure of optmisation problems and the
parameter settings of the algorithm. This insight has aided us in
developing better algorithms for challenging optimisation scenarios,
such as

 - [PDCoEA](https://dl.acm.org/doi/abs/10.1145/3512290.3528853) (a population-based co-evolutionary algorithm for adversarial
   optimisation problems) ([code](https://github.com/pklehre/pdcoea.git))
 - [MOSA-EA](https://github.com/ChengCheng-Qin/mosa-ea) (a self-adaptive
   algorithm for single-objective, pseudo-Boolean optimisation)

Our research has been funded by the European Commission, and UKRI/EPSRC
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
