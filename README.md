## Replica OLX

app para anuncios de produtos

### Funcionalidades
- qualquer pessoa pode anunciar produtos
- qualquer pessoa pode fazer pedidos dos produtos anunciados
    - pessoa tem:
        - name
        - celular(whatsApp)
        - password(?)
    - announcement tem:
        - name
        - details
        - price
        - available (yes/not)
        - photo(?)
    - pedido tem:
        - product of announcement(anuncio)
        - amount
        - delivery place (local de entrega)
        - observation
        - delivery or withdrawal (entrega ou retirada)
- cada usuario tera uma lista de pedidos recebidos(minhas vendas) e pedidos feitos(minhas compras)
- O pedido dever ser aceito pelo vendedor
- o comprador podera acompanhar seus pedidos:
    - status(feito,aceito)

### Arquitetura e Ferramentas
- Python + FastApi (pydantic)
- Será uma API REST
- Banco de Dados Postgres e/ou MongoDB(firebase firestore)
- docker para postgres
- MVC
- Domain Driven Designer (DDD) e Arquitetura Limpa(Clean Arch)