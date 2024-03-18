from fastapi import FastAPI, HTTPException, status, Header, Path, Depends
from models import MaravilhasDoMundo
from typing import Any, List
from time import sleep

def fake_db():
    try:
        print("Abrindo BD")
        sleep(1)
    finally:
        print("Fechando BD")
        sleep(1)

app = FastAPI(title="Api MaravilhasDoMundo", version="0.0.1", description="Api MaravilhasDoMundo")

maravilhasdoMundo = {
    1:{
        "nome":"Cristo Redentor ",
        "localizacao": "Brasil",
        "descricao" : "A imagem de Jesus Cristo de braços abertos no Rio de Janeiro faz jus ao título de uma das 7 Maravilhas do Mundo Moderno. Inaugurado em 1931, levou 5 anos para ser construído, e hoje é um dos cartões postais mais conhecidos do Brasil.",
    },
    2:{
        "nome":"Machu Picchu",
        "localizacao": "Peru",
        "descricao" : "Machu Picchu é uma das mais prestigiadas heranças do povo Inca, um dos mais intrigantes da história. Descoberta em 1911, a Cidade Perdida dos Incas fica no topo de uma montanha com 2400 metros de altitude, no vale do rio Urubamba.",
    },
    3:{
        "nome":"Chichén Itzá",
        "localizacao": "México",
        "descricao" : "A civilização maia nos presenteou com legados arquitetônicos, artísticos, matemáticos, astronômicos e sociais. Chichén Itzá, escolhida como uma das Maravilhas do Mundo Moderno, era o centro político e econômico desse povo.",
    },
    4:{
        "nome":"Coliseu",
        "localizacao": " Itália",
        "descricao" : "Símbolo do Império Romano, o Coliseu é o mais famoso anfiteatro do mundo e uma das obras arquitetônicas mais importantes da história da humanidade. Com cerca de 2 mil anos de história, foi palco de lutas de gladiadores a obras teatrais. ",
    },
    5:{
        "nome":"Ruínas de Petra",
        "localizacao": "Jordânia",
        "descricao" : "Inteiramente esculpida em arenito, as Ruínas de Petra, que sobreviveram aos terremotos e à corrosão natural do tempo, são donas de uma beleza única.",
    },
    6:{
        "nome":"Taj Mahal",
        "localizacao": "Índia",
        "descricao" : "Principal monumento da Índia, o Taj Mahal é um impressionante mausoléu. Construído entre 1630 e 1652, cerca de 22 mil homens trabalharam durante as obras. Localizado em Agra, o monumento foi feito em homenagem à Aryumand Banu Begam, a esposa preferida do imperador Shah Jahan, que faleceu dando à luz ao seu 14º filho.",
    },
    7:{
        "nome":"Grande Muralha da China",
        "localizacao": "China",
        "descricao" : "Idealizada e construída ao longo de várias dinastias chinesas, a Grande Muralha da China começou a ser feita em 220 a.C., por ordem do primeiro imperador chinês Qin Shihuang, da dinastia Qin. A ideia da obra era oferecer proteção das invasões vindas do Norte. ",
    },
  
}

@app.get('/')
async def mensagem():
    return {'Mensagem' : 'Funcionou'}

@app.get ('/maravilhasdomundo', description='Retorna uma lista com as Maravilhas do Mundo, ou lista vazia')
async def get_maravilhasdoMundo():
    return maravilhasdoMundo

@app.get('/maravilhasdomundo/{maravilhasdomundo_id}')
async def get_maravilhasdomundo(maravilhasdomundo_id: int):
    if maravilhasdomundo_id not in maravilhasdoMundo:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail="Maravilha do Mundo não Encontrado")
    return {"item:": maravilhasdoMundo[maravilhasdomundo_id]}
    
@app.post("/maravilhasdomundo", status_code=status.HTTP_201_CREATED)
async def post_maravilhasdomundo(maravilhasdomundo: MaravilhasDoMundo):
    if maravilhasdomundo.id not in maravilhasdoMundo:
        nextid = len(maravilhasdoMundo) + 1
        maravilhasdoMundo[nextid] = maravilhasdomundo
        del maravilhasdomundo.id
        return maravilhasdomundo
    raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Maravilhas do mundo not found.")

@app.put('/maravilhasdomundo/{maravilhasdomundo_id}')
async def put_maravilhasdomundo(maravilhasdomundo_id: int, maravilhasdomundo: MaravilhasDoMundo):
    if maravilhasdomundo_id in maravilhasdoMundo:
        maravilhasdoMundo [maravilhasdomundo_id] = maravilhasdoMundo
        maravilhasdomundo_id = maravilhasdomundo_id
        del maravilhasdomundo_id
        return maravilhasdomundo
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Não existe maravilhas do mundo com id {maravilhasdomundo_id}.')
    
@app.delete("/maravilhasdomundo/{maravilhasdomundo_id}")
async def delete_maravilhasdomundo(maravilhasdomundo_id: int):
    if maravilhasdomundo_id in maravilhasdoMundo:
        del maravilhasdoMundo[maravilhasdomundo_id]
        return {'message': 'item deleted'}
    else:
        return {'Não existe maravilhas do mundo com este id'}
    

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host='127.0.0.1', port=8001, log_level='info', reload=True)

