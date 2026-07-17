---
layout: page
title: Co-Evolution Tutorial
description: Tutorial on Theory of Competitive Co-evolutionary Algorithms
permalink: /CoEvolutionTutorial/
news: false  # includes a list of news items
latest_posts: false  # includes a list of the newest posts
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false  # includes social icons at the bottom of the page
---

(Presented at GECCO 2026 in Costa Rica.)

**Authors**

 - Per Kristian Lehre and Mario Hevia Fajardo. Thanks also to Alistair Benford.

**Resources**

 - [Slides](../assets/pdf/gecco2026-coevolution-tutorial.pdf)
 - [Animations](../blog/2024/coevolutionary-algorithms-tutorial)
 - [Implementation of PDCoEA in Python](https://github.com/pklehre/pdcoea)

**Abstract**

Classical evolutionary algorithms require a fitness function to
compare the quality of candidate solutions. However, in real-world
optimisation, the quality of candidate solutions is often a function
of adversarial and unforeseen factors that are difficult to model
explicitly. Identifying hard or worst-case scenarios to evaluate a
given solution could be a difficult optimisation problem. Thus,
solutions obtained by EAs using a fixed fitness function may perform
poorly when deployed in a competitive, real-world scenario.

Co-evolutionary algorithms — which model evolutionary arms races
between populations of predators and prey — do not rely on explicit
fitness functions. They represent one of the most exciting ideas in
evolutionary computation, with successful applications ranging from
designing sorting networks, playing backgammon, and patching software
bugs. Related approaches from the broader AI field, including
self-play in reinforcement learning and generative adversarial
networks (GANs), highlight the importance of co-evolution.

This tutorial focuses on the theory of competitive co-evolutionary
algorithms including No Free Lunch theorems, runtime analysis, and
black box complexity. This will give participants a deeper and
theoretically founded understanding of how and why co-evolutionary
algorithms work, and why they sometimes fail.

The first part focuses on adversarial optimisation scenarios where
co-evolutionary algorithms are applicable. We will explain how such
problems can be captured within a game-theoretic framework with
appropriate solution concepts. Furthermore, we will look at the
difficulty of adversarial optimisation problems in terms of the
structure of their payoff landscapes. This part will allow
participants to recognise problem types where co-evolution can be
applied.

The second part considers the design of co-evolutionary algorithms,
including essential components – such as evaluation and archiving
methods and diversity mechanisms – and how they impact their
runtime. This part will also cover so-called co-evolutionary
pathologies and how they can be remedied. This part will provide
participants with theoretical insights into how to design effective
co-evolutionary algorithms.

Several interactive activities are planned, including the
visualisation of algorithms using our own software. This will give the
audience a practical and hands-on experience in how co-evolutionary
population dynamics are influenced by the characteristics of the game
and the design of the algorithm.

**Some References**

 - [Pairwise Dominance Co-Evolutionary Algorithm (PDCoEA)](https://link.springer.com/article/10.1007/s00453-024-01218-3)
   
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
