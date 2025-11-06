<<<<<<< HEAD
import json

ARQUIVO = "vingadores.json"

def carregar():
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar(vingadores):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(vingadores, arquivo, indent=4, ensure_ascii=False)
=======
import json

ARQUIVO = "vingadores.json"

def carregar():
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar(vingadores):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(vingadores, arquivo, indent=4, ensure_ascii=False)
>>>>>>> c4931e1 (API dos Vingadores)
