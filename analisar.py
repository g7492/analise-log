from datetime import datetime

print("=== Análise de Log ===\n")

nome_arquivo = input("Digite o nome do arquivo de log: ")

erros = 0
warnings = 0
infos = 0
linhas_importantes = []

try:
    with open(nome_arquivo, "r") as arquivo:
        for linha in arquivo:
            if "ERROR" in linha:
                erros += 1
                linhas_importantes.append(linha.strip())
            elif "WARNING" in linha:
                warnings += 1
                linhas_importantes.append(linha.strip())
            elif "INFO" in linha:
                infos += 1
except FileNotFoundError:
    print("Arquivo não encontrado!")
    exit()

agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

with open("relatorio.txt", "w") as relatorio:
    relatorio.write("=== RELATÓRIO DE ANÁLISE ===\n")
    relatorio.write(f"Data/Hora: {agora}\n")
    relatorio.write(f"Arquivo analisado: {nome_arquivo}\n\n")
    relatorio.write("--- Linhas importantes (ERROR e WARNING) ---\n")
    for linha in linhas_importantes:
        relatorio.write(linha + "\n")
    relatorio.write(f"\nTotal de ERRORs: {erros}\n")
    relatorio.write(f"Total de WARNINGs: {warnings}\n")
    relatorio.write(f"Total de INFOs: {infos}\n")

print("\nRelatório salvo em relatorio.txt")
print(f"ERRORs: {erros} | WARNINGs: {warnings} | INFOs: {infos}")
