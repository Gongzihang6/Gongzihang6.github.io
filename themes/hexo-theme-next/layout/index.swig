{% extends '_layout.swig' %}
{% import '_macro/sidebar.swig' as sidebar_template with context %}

{% block title %}{{ title }}{%- if theme.index_with_subtitle and subtitle %} - {{ subtitle }}{%- endif %}{% endblock %}

{% block class %}index posts-expand{% endblock %}

{% block content %}
  <div class="tag-cloud">
	  <div class="tag-cloud-tags" id="tags">
		{{ tagcloud({min_font: 16, max_font: 16, amount: 300, color: true, start_color: '#fff', end_color: '#fff'}) }}
	  </div>
	</div>
	<br>
	
	{% include 'tag-color.swig' %}

  {%- for post in page.posts.toArray() %}
    {{ partial('_macro/post.swig', {post: post, is_index: true}) }}
  {%- endfor %}

  {% include '_partials/pagination.swig' %}

{% endblock %}

{% block sidebar %}
  {{ sidebar_template.render(false) }}
{% endblock %}
