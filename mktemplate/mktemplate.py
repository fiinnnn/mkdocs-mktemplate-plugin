from mkdocs.plugins import BasePlugin
import re
from pathlib import Path
from jinja2 import Template
import yaml

class MkTemplate(BasePlugin):
    regex = re.compile(r'{%\s*template\s+"(?P<filename>[^"]+)"(?P<yaml>.*?)\s*%}', flags=re.DOTALL|re.VERBOSE)

    def on_page_markdown(self, markdown, page, **kwargs):

        def include_tag(match):
            file_path = Path('templates/' + match['filename'])

            if not file_path.exists():
                raise FileNotFoundError(f'File \'{filename}\' not found')

            template =  Template(file_path.read_text(encoding='utf8'))

            yml = yaml.safe_load(match['yaml'])

            return template.render(yml)

        markdown = re.sub(self.regex, include_tag, markdown)

        return markdown