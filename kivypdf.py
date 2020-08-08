from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.properties import (
    BooleanProperty, ListProperty, NumericProperty)

from PyPDF2 import PdfFileReader
import os, fitz #PyMuPDF

class PdfPage(ButtonBehavior, Factory.Image):
    allow_stretch = BooleanProperty(True)
    keep_ratio = BooleanProperty(True)
    size_hint = ListProperty([1, None])
    height = NumericProperty(Window.height)
    index = NumericProperty(0)

    # def __init__(self, **kwargs):
    #     super(PdfPage, self).__init__(**kwargs)

    def on_release(self, *args):
        print(self.index)

class PdfView(Factory.ScrollView):
    source = StringProperty('')
    pdfpath = StringProperty('')

    def __init__(self, **kwargs):
        super(PdfView, self).__init__(**kwargs)
        self.bind(on_source = self.on_source)

    def on_source(self, obj, source):
        self.children[0].clear_widgets()
        source = os.path.abspath(source)
        self.pdfpath = source[:-4]

        if not os.path.exists(self.pdfpath):
            os.mkdir(self.pdfpath)

        pages = self.getpdfpages(filename=source)

        for page_num in pages:
            # get the pux from the pages
            pix = pages[page_num][1]
            # save pdf page image in pdfpath
            fil = os.path.join(self.pdfpath, f"outfile{page_num}.png")
            # verify if img already exist, else create it.
            pix.writePNG(fil) if not os.path.exists(fil) else None
            # get image widget
            img = PdfPage(source = fil, index = page_num)
            # add image in the scrollview boxlayout
            self.children[0].add_widget(img)

    def getpdfpages(self, filename = "test.pdf"):
        """Get pdf pages as bytes."""
        FILEPATH = os.path.abspath(filename)
        # get the quantity of pages
        pdf = PdfFileReader(open(FILEPATH,'rb'))
        getNumPages = pdf.getNumPages()
        pages = dict()
        # open pdf file
        doc = fitz.open(FILEPATH)

        for pageNum in range(getNumPages):
            # get the page by index
            page = doc.loadPage(pageNum)
            # get byttes from image
            pix = page.getPixmap()
            # remove the alpha channel 'cause fitz don't works with alpha
            pix1 = fitz.Pixmap(pix, 0) if pix.alpha else pix  # PPM does not support transparency
            # get image data in this case "ppm", but we can use "png", etc.
            imgdata = pix1.getImageData(output = "ppm")
            # pix.writePNG(f"outfile{pageNum}.png")
            pages[pageNum] = [imgdata, pix]

        return pages

Builder.load_string("""
<PdfView>:
    do_scroll_x: False
    do_scroll_y: True
    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: self.minimum_height
""")

if __name__ == "__main__":
    from kivy.app import App

    class PdfApp(App):
        def build(self):
            return Builder.load_string("""
BoxLayout:
    orientation: "vertical"
    PdfView:
        source: 'test.pdf'
    """)

    PdfApp().run()