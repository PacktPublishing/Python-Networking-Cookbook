banner motd #
{% block motd %}
Welcome to this device. This is the default message of the day that can be changed in the configuration.
{% endblock %}
#
hostname production-{% block name_suffix %}default{% endblock %}
