from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import date

app = FastAPI()
class Compra(BaseModel):
    produto: str
    quantidade: int
    realizado: bool
    preco_unitario: float
    data_compra: date
    observacoes: Optional[str] = None
    
lista = []
    
    
@app.post('/inserir')
def inserir (compra: Compra):
    try:
        lista.append(compra)
        return {"Mensagem": "Inserido com sucesso"}
    except Exception as e:
        return {"Mensagem": f"Erro ao inserir: {str(e)}"}
    
@app.get('/listar')
def listar(opcao: int = 0):
    if opcao == 0:
        return lista
    elif opcao == 1:
        return list(filter(lambda x: x.realizado == False, lista))
    elif opcao == 2:
        return list(filter(lambda x: x.realizado == True, lista))
    else:
        return {"Mensagem": "Opção inválida"}
    
@app.get('/listagemUnica/{produto}')
def listar(id: int):
    try:
        return lista[id]
    except:
        return {"Mensagem": "ID não encontrado"}
   

@app.post('/alterarStatus/{produto}')
def alteraStatus(id: int):
    try:
        lista[id] = not lista[id].realizado
        return {"Mensagem": "Alterado com sucesso"}
    except:
        return {"Mensagem": "erro ao alterar status"}
    
@app.post('/deletar/{produto}')
def deletar(id: int):
    try:
        del lista[id]
        return {"Mensagem": "Deletado com sucesso"}
    except:
        return {"Mensagem": "erro ao deletar"}