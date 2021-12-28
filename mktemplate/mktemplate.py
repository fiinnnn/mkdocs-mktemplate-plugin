from mkdocs.plugins import BasePlugin
import re
from os.path import join, dirname
from jinja2 import Template, FileSystemLoader, Environment
import yaml

class MkTemplate(BasePlugin):
    regex = re.compile(r'{%\s*template\s+"(?P<filename>[^"]+)"(?P<yaml>.*?)\s*%}', flags=re.DOTALL|re.VERBOSE)

    def on_page_markdown(self, markdown, page, **kwargs):

        def include_tag(match):
            filename = match['filename']

            templateLoader = FileSystemLoader(searchpath='templates')
            templateEnv = Environment(loader=templateLoader)
            template = templateEnv.get_template(filename)

            yml = yaml.safe_load(match['yaml'])

            return template.render(yml)

        markdown = re.sub(self.regex, include_tag, markdown)

        return markdown
