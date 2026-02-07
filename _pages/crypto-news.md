---
layout: default
title: "Crypto News"
permalink: /crypto-news/
---

<div class="section-title">
	<h2><span>Crypto News</span></h2>
</div>

{% assign crypto_posts = site.posts | where_exp: "post", "post.categories contains 'crypto-news' or post.categories contains 'crypto' or post.tags contains 'crypto'" %}

{% if crypto_posts.size > 0 %}
	{% for post in crypto_posts %}
		<article class="list-item">
			<h3><a href="{{ post.url }}">{{ post.title }}</a></h3>
			<p>{{ post.excerpt }}</p>
		</article>
	{% endfor %}
{% else %}
	<p>No crypto posts yet—check back soon for market updates.</p>
{% endif %}
