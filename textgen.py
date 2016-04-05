#!/usr/bin/env python
#-*- coding: utf-8 -*-
import inkex

class TextGeneratorClass(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('-g', '--text_generator', action='store', type='string', dest='text_generator', default='samples', help='Set the default page')
        self.OptionParser.add_option('-t', '--text_type', action='store', type='string', dest='text_type', default='headLine', help='Set the default text type')
        self.OptionParser.add_option('-r', '--rss', action='store', type='string', dest='rss', default='http://www.theonion.com/feeds/rss', help='Chosse your RSS page')
        self.OptionParser.add_option('-c', '--rss_text', action='store', type='string', dest='rss_text', default='http://www.theonion.com/feeds/rss', help='Chosse your RSS text type')

    def effect(self):
        # inkex.debug(self.options.text_generator)
        # inkex.debug(self.options.text_type)
        # inkex.debug(self.options.rss)
        # inkex.debug(self.options.rss_text)

        if self.options.text_generator == '"samples"':
            text_type = self.options.text_type
            text = self._modifyTextNode(text_type)

    def _getSampleText(self, text_type):
        return text_type

    def _modifyTextNode(self, text_type):
        svg = self.document.getroot()
        current_selected = self.selected
        if current_selected:
            for id_, node in current_selected.items():
                if node.tag == inkex.addNS('text', 'svg'):
                    tspan = node.getchildren()[0]
                    text = self._getSampleText(text_type)
                    tspan.text = text

        # width  = self.unittouu(svg.get('width'))
        # height = self.unittouu(svg.attrib['height'])
        # layer = inkex.etree.SubElement(svg, 'g')
        # layer.set(inkex.addNS('label', 'inkscape'), '%s Layer' % (textType))
        # layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')
        # text = inkex.etree.Element(inkex.addNS('text','svg'))

        # text.text = 'Hello %s!' % (textType)
        #http://www.theonion.com/feeds/rss
        #
        # style = {'text-align' : 'center', 'text-anchor' : 'middle'}
        # text.set('style', formatStyle(style))
        #
        # text.set('x', str(width / 2))
        # text.set('y', str(height / 2))
        # layer.append(text)


if __name__ == '__main__':
    TextGenerator = TextGeneratorClass()
    TextGenerator.affect()
