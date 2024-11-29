import pandas as pd
from fpdf import FPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


# importamos o panda que é o principal leitor de arquivos
arquivo = "Prova/Prova/alunos.csv"
df = pd.read_csv(arquivo, encoding="latin1", delimiter=";")

print(df.head())
# print(df['nome'])

# Aqui colocamos algum filtro para mostrar notas acima de 7 ou apenas pessoas com o nome Maria

# filtro = df[df['nota1'] > 6]
# ou
filtro = df[df["nome"] == "Maria"]
print(filtro)

# Criando PDF
pdf = canvas.Canvas("relatorio_alunos.pdf")
largura, altura = 595.28, 841.89  # Largura e altura em pontos
margem = 50
linha_atual = altura - margem  # Posição inicial no topo da página


# Função para adicionar texto e gerenciar quebras de página
def adicionar_linha(texto, pdf):
    global linha_atual
    if linha_atual < margem:  # Verifica o rodapé da página
        pdf.showPage()  # Cria uma nova página
        linha_atual = altura - margem  # Reseta a posição da linha
    pdf.drawString(margem, linha_atual, texto)  # Adiciona o texto
    linha_atual -= 20  # Move para a próxima linha


pdf.setFont("Helvetica", size=12)

# Adicionando Título
pdf.setFont("Helvetica", size=16)
x, y = 200, 750
pdf.drawString(x, y, "Relatório de Alunos")
y -= 100
x -= 100
# Pulando Linhas

pdf.setFont("Helvetica", size=12)
for index, row in filtro.iterrows():
    linha = f"Nome: {row['nome']}, Curso: {row['curso']}, Notas: {row['nota1']}, Notas2: {row['nota2']}, Notas3: {row['notas3']}"

pdf.drawString(x, y, linha)
pdf.save()
print("PDF gerado com sucesso")

# Continua = Fazer uma media dentro do data frame e mostrala no relatorio, seria interessante se mostrasse TODOS os aprovados do semestre.
