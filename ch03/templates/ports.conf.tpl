{% for p in ports %}
interface {{ p['type'] }} {{ p['slot'] }}/{{ p['port_num'] }}
switchport mode {{ p['intf_type'] }}
{% if p['intf_type'] == "trunk" %}
switchport trunk native vlan 5
{% endif %} 
{% endfor %}
