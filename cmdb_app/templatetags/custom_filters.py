from django import template

register = template.Library()


@register.filter(name="add_class")
def add_class(value, arg):
    return value.as_widget(attrs={"class": arg})


@register.filter(name="attr")
def add_attr(field, arg):
    # Si le champ est déjà rendu (SafeString), nous ne pouvons pas modifier ses attributs,
    # donc nous retournons simplement le champ tel quel.
    if isinstance(field, template.base.SafeString):
        return field

    # Sinon, nous travaillons avec le champ original
    args = arg.split(",")
    for a in args:
        if ":" in a:
            key, value = a.split(":", 1)
            field.field.widget.attrs[key] = value
    return field
