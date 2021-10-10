import os


def ocrpdf(pdforigin, finalpdf):
    if '.pdf' in pdforigin:
        pdforigin = " ".join(pdforigin)
    else:
        pdforigin = pdforigin + '.pdf'
    pdforigin = pdforigin.strip()

    if '.pdf' in finalpdf:
        finalpdf = finalpdf
    else:
        finalpdf += '.pdf'
    finalpdf = finalpdf.strip()

    return os.system('ocrmypdf ' + f'"{pdforigin}"' + " " f'"{finalpdf}"')

print("\nPara aplicar o OCR no seu pdf é necessário que o arquivo esteja no mesmo diretório que a pasta deste código.\n")
pdforigin = input("diga o nome do pdf-imagem que você deseja aplicar OCR:\n")
print("...\n")
finalpdf = input("diga o nome do pdf final, após conversão:\n")
print("\n...\n")
ocrpdf(pdforigin, finalpdf)
print("seu PDF está com OCR aplicado agora!")
