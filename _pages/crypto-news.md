---
layout: default
title: "Crypto News"
permalink: /crypto-news/
---

<div class="section-title">
	<h2><span>Crypto News</span></h2>
</div>

{% assign found = false %}
{% for post in site.posts %}
	{% assign cats = post.categories | join: "," | downcase %}
	{% assign tags = post.tags | join: "," | downcase %}
	{% if cats contains 'crypto-news' or cats contains 'crypto' or tags contains 'crypto' %}
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
	<p>No crypto posts yet—check back soon for market updates.</p>
{% endunless %}
