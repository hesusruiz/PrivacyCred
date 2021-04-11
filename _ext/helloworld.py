from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.util import logging
logger = logging.getLogger(__name__)


class HelloWorld(Directive):

    def run(self):
        logger.warning('Hola desde Hello world extension!')
        paragraph_node = nodes.paragraph(text='Hello World!')
        return [paragraph_node]


def setup(app):
    app.add_directive("helloworld", HelloWorld)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }