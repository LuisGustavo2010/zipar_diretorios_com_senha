from tkinter import filedialog
import os
import subprocess

def compactar_tudo(pasta, ignore_zips=True, ignore_exe=True):
    nomesarquivos = os.listdir(pasta)
    if ignore_zips:
        nomesarquivos = [fn for fn in nomesarquivos if not fn.endswith('.zip')]

    if ignore_exe:
        nomesarquivos = [fn for fn in nomesarquivos if not fn.endswith('.exe')]

    for dirs in os.listdir(pasta):
            try:
                subprocess.call([r'C:\Program Files\7-Zip\7z.exe', 'a', dirs + '.zip', '-mx9', '-pTeste'] + [os.path.join(pasta,dirs) + '/'])
            except:
                pass


if __name__ == '__main__':
    pasta = filedialog.askdirectory()
    print(f"Compactando arquivos em {pasta}")
    n = compactar_tudo(pasta)
    print(f"{n} arquivos compactados com sucesso")