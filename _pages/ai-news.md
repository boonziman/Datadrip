---
layout: default
title: "AI News"
permalink: /ai-news/
---

<div class="section-title">
	<h2><span>AI News</span></h2>
</div>

{% assign found = false %}
{% for post in site.posts %}
	{% assign cats = post.categories | join: "," | downcase %}
	{% assign tags = post.tags | join: "," | downcase %}
	{% if cats contains 'ai-news' or cats contains 'ai' or tags contains 'ai' %}
		{% unless found %}
			{% assign found = true %}
		{% endunless %}
		<article class="list-item">
			<h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
			<p>{{ post.excerpt }}</p>
		</article>
	{% endif %}
{% endfor %}

{% unless found %}
	<p>No AI posts yet—check back soon for the latest AI coverage.</p>
{% endunless %}
