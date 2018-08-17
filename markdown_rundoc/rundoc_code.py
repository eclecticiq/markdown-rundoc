"""
Rundoc Code Extension for Python Markdown
=========================================

This extension adds Rundoc Code Blocks to Python-Markdown.

Based on Fenced Code Extension:
    See <https://Python-Markdown.github.io/extensions/rundoc_code_blocks>
    for documentation.
    Original code Copyright 2007-2008 [Waylan Limberg](http://achinghead.com/).
    Changes Copyright 2008-2014 The Python Markdown Project

Changes Copyright 2018 Predrag Mandic

License: [BSD](http://www.opensource.org/licenses/bsd-license.php)
"""

from __future__ import absolute_import
from __future__ import unicode_literals
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re


class RundocCodeExtension(Extension):

    def __init__(self, **kwargs):
        self.config = {
            'tags': [ kwargs.get('tags') ],
            'must_have_tags': [ kwargs.get('must_have_tags') ],
            'must_not_have_tags': [ kwargs.get('must_not_have_tags') ],
            }
        super(RundocCodeExtension, self).__init__(**kwargs)
    
    def extendMarkdown(self, md, md_globals):
        """ Add RundocBlockPreprocessor to the Markdown instance. """
        md.registerExtension(self)

        md.preprocessors.add('rundoc_code_block',
                             RundocBlockPreprocessor(md),
                             ">normalize_whitespace")


class RundocBlockPreprocessor(Preprocessor):
    RUNDOC_BLOCK_RE = re.compile(r'''
(?P<fence>^(?:~{3,}|`{3,}))[ ]*         # Opening ``` or ~~~
(\{?\.?(?P<tags>[^\n\r]*))?[ ]*         # Optional {, and lang
# Optional highlight lines, single- or double-quote-delimited
(hl_lines=(?P<quot>"|')(?P<hl_lines>.*?)(?P=quot))?[ ]*
}?[ ]*\n                                # Optional closing }
(?P<code>.*?)(?<=\n)
(?P=fence)[ ]*$''', re.MULTILINE | re.DOTALL | re.VERBOSE)
    CODE_WRAP = '<pre><code%s>%s</code></pre>'
    CLASS_TAG = ' class="%s"'
    config = None

    def __init__(self, md):
        super(RundocBlockPreprocessor, self).__init__(md)

    def run(self, lines):
        """ Match and store Rundoc Code Blocks in the HtmlStash. """

        # Get config
        for ext in self.markdown.registeredExtensions:
            if isinstance(ext, RundocCodeExtension):
                self.config = ext.config
                #print(self.config)
                break

        text = "\n".join(lines)
        while 1:
            m = self.RUNDOC_BLOCK_RE.search(text)
            tags = []
            have_tags = []
            must_have_tags = []
            must_not_have_tags = []
            if self.config['tags'][0]:
                have_tags = self.config['tags'][0].split('#')
                have_tags = list(filter(bool, have_tags))
            if self.config['must_have_tags'][0]:
                must_have_tags = self.config['must_have_tags'][0].split('#')
                must_have_tags = list(filter(bool, must_have_tags))
            if self.config['must_not_have_tags'][0]:
                must_not_have_tags = self.config['must_not_have_tags'][0].split('#')
                must_not_have_tags = list(filter(bool, must_not_have_tags))

            if m:
                if m.group('tags'):
                    tags = m.group('tags').split('#')
                    tags = list(filter(bool, tags))
                classes = tags[:]
                rundoc_selected = False
                if have_tags:
                    for tag in have_tags:
                        if tag in classes:
                            rundoc_selected = True
                            break
                else:
                    if len(classes):
                        # check if at least interpreter is defined
                        rundoc_selected = True
                if must_have_tags:
                    for tag in must_have_tags:
                        if tag not in classes:
                            rundoc_selected = False
                            break
                if rundoc_selected and must_not_have_tags:
                    for tag in must_not_have_tags:
                        if tag in classes:
                            rundoc_selected = False
                            break
                if not (have_tags or must_have_tags or must_not_have_tags):
                    if len(tags):
                        rundoc_selected = True
                if rundoc_selected:
                    classes.append("rundoc_selected")

                class_tag = self.CLASS_TAG % ' '.join(classes)
                code = self.CODE_WRAP % (class_tag,
                                         self._escape(m.group('code')))

                placeholder = self.markdown.htmlStash.store(code, safe=True)
                text = '%s\n%s\n%s' % (text[:m.start()],
                                       placeholder,
                                       text[m.end():])
            else:
                break
        return text.split("\n")

    def _escape(self, txt):
        """ basic html escaping """
        txt = txt.replace('&', '&amp;')
        txt = txt.replace('<', '&lt;')
        txt = txt.replace('>', '&gt;')
        txt = txt.replace('"', '&quot;')
        return txt


def makeExtension(*args, **kwargs):
    return RundocCodeExtension(*args, **kwargs)

