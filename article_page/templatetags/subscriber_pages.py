from django import template

register = template.Library()


@register.filter(name="Subscriber")
def is_subscriber(user, group_name):
    return user.groups.filter(name=group_name).exists()
