import requests

#Salva a UrlBase em uma variável
UrlBase = "http://pokeapi.azurewebsites.net/"

#Definição do teste
def test_get_all_pokemons():
    #Salva o retorno da chamada na variável resposta para validação
    resposta = requests.get(UrlBase+"/api/pokemon/list")
    #Converte a resposta da chamada em um json para poder navegar com mais facilidade
    resposta_json = resposta.json()
    #Validade se o status code da chamada é o esperado
    assert resposta.status_code == 200
    #Valida se o campo Success da chamada retornou true
    assert resposta_json["success"] == True

#Definição do teste
def test_get_one_pokemon():
    # Salva o retorno da chamada na variável resposta para validação
    resposta = requests.get(UrlBase+"/api/pokemon/Bulbasaur")
    # Converte a resposta da chamada em um json para poder navegar com mais facilidade
    resposta_json = resposta.json()
    # Validade se o status code da chamada é o esperado
    assert resposta.status_code == 200
    # Valida se o campo name da chamada retornou Bulbasaur
    assert resposta_json["data"]["name"] == "Bulbasaur"
