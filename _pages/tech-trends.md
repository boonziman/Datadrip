---
layout: default
title: "Tech Trends"
permalink: /tech-trends/
---

<div class="section-title">
	<h2><span>Tech Trends</span></h2>
</div>

{% assign tech_posts = site.posts | where_exp: "post", "post.categories contains 'tech-trends' or post.categories contains 'tech' or post.tags contains 'tech' or post.tags contains 'technology'" %}

{% if tech_posts.size > 0 %}
	{% for post in tech_posts %}
		<article class="list-item">
			<h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
			<p>{{ post.excerpt }}</p>
		</article>
	{% endfor %}
{% else %}
	<p>No tech posts yet—check back soon for trend coverage.</p>
{% endif %}
