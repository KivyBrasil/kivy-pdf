# kivy-pdf

## O Que É
Widget criado para usar PDF no kivy, 
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

## Requisitos
```
Python >= 3.7
Kivy   >= 1.11.1
```

## Dependências
```
python -m pip install --upgrade pip
python -m pip install --upgrade wheel
python -m pip install --upgrade pypdf2
python -m pip install --upgrade pymupdf
```

## Para testar
```
python3 kivypdf.py

or

py kivypdf.py
```
