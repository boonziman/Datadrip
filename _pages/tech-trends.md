---
layout: default
title: "Tech Trends"
permalink: /tech-trends/
---

<div class="section-title">
	<h2><span>Tech Trends</span></h2>
</div>

{% assign found = false %}
{% for post in site.posts %}
	{% assign cats = post.categories | join: "," | downcase %}
	{% assign tags = post.tags | join: "," | downcase %}
	{% if cats contains 'tech-trends' or cats contains 'tech' or tags contains 'tech' or tags contains 'technology' %}
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
	<p>No tech posts yet—check back soon for trend coverage.</p>
{% endunless %}
