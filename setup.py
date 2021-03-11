from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='mkdocs-mktemplate-plugin',
    version='1.0.0',
    packages=['mktemplate'],
    url='https://github.com/fiinnnn/mkdocs-mktemplate-plugin',
    license='MIT',
    author='Finn Vos',
    description='mkdocs plugin to insert jinja templates on any page',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['mkdocs', 'Jinja2', 'PyYAML'],

    # The following rows are important to register your plugin.
    # The format is "(plugin name) = (plugin folder):(class name)"
    # Without them, mkdocs will not be able to recognize it.
    entry_points={
        'mkdocs.plugins': [
            'mktemplate = mktemplate:MkTemplate',
        ]
    },
)
