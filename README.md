# kivy-pdf

## O Que É
Widget criado para usar PDF dentro do kivy, 
basicamente ele cria uma pasta com o nome do 
arquivo pdf, por exemplo nosso arquivo é ```test.pdf```.
```
from kivypdf import PdfView

# main.kv
BoxLayout:
    orientation: "vertical"
    PdfView:
        source: 'test.pdf'
```

## Como Instalar
```
pypdf2 == 1.26.0
pymupdf == 1.17.2
python == 3.7
kivy == 1.11.1
```

## Para testar
```
python3 kivypdf.py

or

py kivypdf.py
```