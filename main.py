from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Carregar o JSON do arquivo
with open("vingadores.json", "r", encoding="utf-8") as arquivo:
    vingadores = json.load(arquivo)


@app.get("/", status_code=200)
def home():
    return {"quantidade_personagens": len(vingadores)}

@app.get("/vingadores", status_code=200)
def listar_herois():
    return vingadores


@app.get("/vingadores/{id_heroi}", status_code=200)
def pegar_heroi(id_heroi: int):
    id_str = str(id_heroi)
    if id_str in vingadores:
        return vingadores[id_str]
    raise HTTPException(status_code=404, detail="Herói não encontrado")


@app.post("/vingadores", status_code=201)
def adicionar_heroi(novo_heroi: dict = Body(...)):
    novo_id = str(len(vingadores) + 1)
    vingadores[novo_id] = novo_heroi

    with open("vingadores.json", "w", encoding="utf-8") as arquivo:
        json.dump(vingadores, arquivo, indent=4, ensure_ascii=False)

    return {"mensagem": "Herói adicionado com sucesso!", "id": novo_id}


@app.put("/vingadores/{id_heroi}", status_code=200)
def atualizar_heroi(id_heroi: int, dados_atualizados: dict = Body(...)):
    id_str = str(id_heroi)

    if id_str not in vingadores:
        raise HTTPException(status_code=404, detail="Herói não encontrado")

    vingadores[id_str].update(dados_atualizados)

    with open("vingadores.json", "w", encoding="utf-8") as arquivo:
        json.dump(vingadores, arquivo, indent=4, ensure_ascii=False)

    return {"mensagem": "Herói atualizado com sucesso!", "id": id_str}


@app.delete("/vingadores/{id_heroi}", status_code=200)
def deletar_heroi(id_heroi: int):
    id_str = str(id_heroi)
    if id_str not in vingadores:
        raise HTTPException(status_code=404, detail="Herói não encontrado")

    del vingadores[id_str]

    with open("vingadores.json", "w", encoding="utf-8") as arquivo:
        json.dump(vingadores, arquivo, indent=4, ensure_ascii=False)

    return {"mensagem": "Herói deletado com sucesso!", "id": id_str}
