---
layout: default
title: Home
permalink: /
---

<header class="hero" style="background: #007BFF; color: white; padding: 50px; text-align: center;">
  <h1>Welcome to DataDrip: Your Source for AI News Updates 2026</h1>
  <p>Latest crypto, tech, and AI trends - SEO-optimized and AI-powered.</p>
</header>

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
