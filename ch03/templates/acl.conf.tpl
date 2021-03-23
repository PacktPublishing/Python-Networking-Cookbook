interface {{ intf }}
ip access-group 1 in
{% for host in disallowed %}
access-list 1 deny host {{ host }}
{% endfor %}
{% for host in allowed %}
access-list 1 permit host {{ host }}
{% endfor %}
