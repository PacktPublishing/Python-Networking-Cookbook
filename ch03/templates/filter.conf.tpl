{% for addr in addresses %}
{{ addr }} -> {{ addr|toIPv6 }}
{% endfor %}