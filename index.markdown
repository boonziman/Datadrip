layout: default
title: Home
permalink: /
---

<!-- Hero Section -->
<header class="hero" style="background: #007BFF; color: white; padding: 50px; text-align: center;">
	<h1>Welcome to DataDrip: Your Source for AI News Updates 2026</h1>
	<p>Latest crypto, tech, and AI trends - SEO-optimized and AI-powered.</p>
</header>

<!-- Recent Articles -->
<section class="latest-posts">
	<div class="section-title">
		<h2><span>Recent Articles</span></h2>
	</div>

	{% for post in site.posts limit:5 %}
		<article class="list-item">
			<h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
			<p>{{ post.excerpt }}</p>
		</article>
	{% endfor %}

	{% if site.posts.size == 0 %}
		<p>No posts yet—check back soon for the latest AI and crypto news!</p>
	{% endif %}

</section>

<!-- Disabled to avoid generating a duplicate homepage. -->
