# Tarefa principio SOLID

## Single Responsiblity Princípio
Veja o código [Single.py](./Single.py), a classe `Usuario` tem um exemplo de falha de responsabilidade única, onde a função `salvar_no_banco` tem mais de uma responsabilidade, ele salva o valor no banco e também imprime o valor no console. Para corrigir isso, separe as responsabilidades em funções diferentes.

A classe `UsuarioCorrigido` tem metódos com responsabilidades únicas, como `salvar_no_banco` e `informar_valor`, que são chamadas separadamente.

## Princípio Deméter 

Veja o código [Demeter.py](./Demeter.py), a classe `Pedido` tem um exemplo de violação do princípio de Deméter, onde o método `imprimir_endereco_entrega` acessa diretamente o atributo `rua` do objeto `Cliente`. 

Para corrigir isso, você pode criar um método na classe `Cliente` que retorna o endereço completo, e chamar esse método no `Pedido`.

## Princípio da interface segregada
Veja o código [InterfaceSegregada.py](./Interface.py), a classes `Funcionario`,  `FuncionarioCLT` e `FuncionarioPublico` respeitam o princípio da interface segregada, onde cada classe implementa apenas os métodos que são relevantes para ela.

A classe `FuncionarioIncorreto` viola esse princípio, pois implementa métodos que não são relevantes para ela, como `get_fgts` e `get_siape`.

## Princípio de inversão de dependência
Veja o código [InversaoDependencia.py](./Inversao.py), a classe `Pedido` tem um exemplo de violação do princípio de inversão de dependência, onde ela depende diretamente da classe `Cliente`. 