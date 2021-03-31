import PyPDF2
def outputpdf(inpdf,outpdf):
    pdfWriter = PyPDF2.PdfFileWriter()      # 用于写pdf
    pdfReader = PyPDF2.PdfFileReader(inpdf)   # 读取pdf内容


    def add_watermark(water_file,page_pdf):
        """
        将水印pdf与pdf的一页进行合并
        :param water_file:
        :param page_pdf:
        :return:
        """
        pdfReader = PyPDF2.PdfFileReader(water_file)
        page_pdf.mergePage(pdfReader.getPage(0))
        return page_pdf

    # 遍历pdf的每一页,添加水印
    for page in range(pdfReader.numPages):
        page_pdf = add_watermark(r'Desktop\test\1.pdf', pdfReader.getPage(page))
        pdfWriter.addPage(page_pdf)

    with open(outpdf, 'wb') as target_file:
        pdfWriter.write(target_file)

import os
filePath = r'Desktop\test\input'
for i,j,k in os.walk(filePath):
    print(i,j,k)
    
for i in k:
    inpdf=r'Desktop\test\input'+'\%s'%i
    #print(input)
    outpdf=r'Desktop\test\output'+'\%s'%i
    
    outputpdf(inpdf,outpdf)
