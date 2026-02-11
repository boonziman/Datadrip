---
layout: default
title: Home
permalink: /

<div class="hero">
    <h1>Welcome to DataDrip</h1>
    <p>Your daily source for curated AI, crypto, and tech news with smart analysis — updated automatically.</p>
</div>

<!-- Featured
================================================== -->
<section class="featured-posts">
    <div class="section-title">
        <h2><span>Featured</span></h2>
    </div>
    <div class="row">
    {% for post in site.posts %}
        {% if post.featured == true %}
            {% include featuredbox.html %}
        {% endif %}
    {% endfor %}
    </div>
</section>

<!-- Posts Index
================================================== -->
<section class="recent-posts">
    <div class="section-title">
        <h2><span>All Stories</span></h2>
    </div>
    <div class="row listrecent">
        {% for post in paginator.posts %}
        {% include postbox.html %}
        {% endfor %}
    </div>
</section>
