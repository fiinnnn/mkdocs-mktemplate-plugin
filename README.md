# mktemplate

This is a plugin for [mkdocs](https://www.mkdocs.org/) to render jinja
templates in markdown documents.

## Usage

Template files must be in `templates/` in the root directory of your
mkdocs project.

An example template file might look like this:
```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

Then in any of the pages of your mkdocs project use the following syntax
to include a template and provide the variables.
```md
{%
template "template.html" # filename of the template in templates/ directory
items:
    - item 1
    - item 2
    - item 3
%}
```

This will generate the following result:
```html
<ul>
    <li>item 1</li>
    <li>item 2</li>
    <li>item 3</li>
</ul>
```

## Packages used
- [mkdocs](https://www.mkdocs.org/)
- [Jinja](https://palletsprojects.com/p/jinja/)
- [PyYAML](https://pyyaml.org/)