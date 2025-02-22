from .subscribers_repository import SubscribersRepository
import pytest
@pytest.mark.skip("Insert in DB")
def test_insert():
    subscriber_info = {
        "name" :"meuNome",
        "email" :"email@example.com",
        "evento_id":1
    }
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)

@pytest.mark.skip("Select in DB")
def test_select_subscriber():
    email = "email@example.com"
    evento_id = 1
    subs_repo = SubscribersRepository()
    resposta = subs_repo.select_subscriber(email,evento_id)
    print(resposta.nome)