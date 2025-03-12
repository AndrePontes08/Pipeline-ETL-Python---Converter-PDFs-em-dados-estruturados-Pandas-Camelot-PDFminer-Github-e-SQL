import os
import camelot
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt



file_name = 'report'
path= os.path.abspath(f'db\{file_name}.pdf')


tables = camelot.read_pdf(
    path,
    pages='1-end', # quantidade de paginas
    flavor='stream',
    table_areas=['20, 720, 577, 124 '], #definindo o tamanho da tabela no pdf
    columns=['25, 250, 260, 360,370, 480, 500, 570'], # definindo as posiçoes das colunas
    strip_text=' .\n'
    
)

print (tables[0].parsing_report)


camelot.plot(tables[0],kind='contour')


#plt.show() # plota oq o sistema consegue identificar no pdf

print(tables[0].df)

print('pause')