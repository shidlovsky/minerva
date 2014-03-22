import json
from django import template
register = template.Library()

@register.filter(name='addattributes')
def addattributes(field, arg):
	args = json.loads(arg)
	attrs = {}
	for key, value in args.iteritems():
		attrs[key] = value
	return field.as_widget(attrs=attrs)