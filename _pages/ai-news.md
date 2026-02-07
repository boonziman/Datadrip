---
layout: default
title: "AI News"
permalink: /ai-news/
---

<div class="section-title">
	<h2><span>AI News</span></h2>
</div>

{% assign ai_posts = site.posts | where_exp: "post", "post.categories contains 'ai-news' or post.categories contains 'ai' or post.tags contains 'ai'" %}

{% if ai_posts.size > 0 %}
	{% for post in ai_posts %}
		<article class="list-item">
			<h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
			<p>{{ post.excerpt }}</p>
		</article>
	{% endfor %}
{% else %}
	<p>No AI posts yet—check back soon for the latest AI coverage.</p>
{% endif %}
