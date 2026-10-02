from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


def gerar_pdf(filename="boletim_inventario_cafeteria.pdf"):
    # Configurações do documento PDF
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()
    story = []

    # Conteúdo do boletim
    story.append(
        Paragraph(
            "<b>Boletim Rápido de Inventário:</b> Cafeteria",
            styles['Heading1']
        )
    )

    story.append(
        Paragraph(
            "<b>Responsável pelo Inventário:</b> Equipe da Cafeteria",
            styles['Normal']
        )
    )

    story.append(Spacer(1, 15))

    # Dados do inventário
    dados = [
        ["Item / Suprimento", "Nível Atual"],
        ["Café em grãos", "Alto"],
        ["Leite", "Médio"],
        ["Açúcar", "Alto"],
        ["Copos descartáveis", "Baixo"],
        ["Guardanapos", "Médio"],
        ["Xarope para bebidas", "Baixo"]
    ]

    tabela = Table(dados, colWidths=[250, 250])

    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E293B')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#CBD5E1')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [
            colors.white,
            colors.HexColor('#F8FAFC')
        ])
    ]))

    story.append(tabela)

    story.append(Spacer(1, 15))

    story.append(
        Paragraph(
            "<b>Resumo:</b> Estoque geral em nível adequado, "
            "com atenção para copos descartáveis e xaropes, "
            "que apresentam nível baixo e podem exigir reposição.",
            styles['Normal']
        )
    )

    doc.build(story)

    print(f"Boletim gerado com sucesso: {filename}")


if __name__ == "__main__":
    gerar_pdf()
