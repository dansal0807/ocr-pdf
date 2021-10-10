Este programa tem o intuito de ser um modificador de arquivos PDF. Os arquivos PDFs podem ser 3: PDFs verdadeiros - em que podem ser selecionados o tipo de texto, PDFs-de-imagem - arquivos feitos de imagens e que o conteúdo é "aprisionado" e não pode ser acessado. Como terceiro tipo temos o PDFs-buscáveis: estes são os PDFs que resultam de aplicação OCR (Optical Character Recognition - Reconhecimento óptico de caracter), em que o documento é analizado e estruturado com uma nova camada de texto por detrás da camada de imagem do PDF-de-Imagem. 

A criação do terceiro tipo de PDF a partir do segundo tipo é o intuito deste programa.
Para isto é necessário a aplicação de alguns programas externos ao python.

Abaixo listarei o processo que utilizei para instalar estes programas externos:

Além de ter o python instalado e um ambiente virtual iniciado, é necessário utilizar o comando pip: pip install ocrmypdf.
Esta biblioteca é um conjunto de pacotes que atuará sobre o PDF.

Primeiro de tudo, caso seja usuário de windows, é necessário ter um administrador de pacotes chamado<a href="https://chocolatey.org/"> Chocolotey </a>.
Após ter instalado ele, é necessário escrever os seguintes comandos:
- choco install --pre tesseract
- choco install ghostscript

Para mais informações sobre esse processo, caso utilizar MacOS ou Linux, acesse <a href="https://ocrmypdf.readthedocs.io/en/latest/installation.html#installing-on-windows">aqui</a>.
