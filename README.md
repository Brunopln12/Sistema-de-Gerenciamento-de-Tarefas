# Projeto de Gerenciamento de Tarefas

Este é um projeto simples de gerenciamento de tarefas, desenvolvido em Python, que permite adicionar, exibir, buscar, atualizar e excluir tarefas.

## Funcionalidades

- **Adicionar Tarefas**: Adiciona uma nova tarefa à lista.
- **Exibir Tarefas**: Exibe todas as tarefas adicionadas.
- **Buscar Tarefas**: Busca tarefas pelo responsável ou pela descrição.
- **Atualizar Tarefas**: Atualiza o responsável ou a descrição de uma tarefa existente.
- **Excluir Tarefas**: Exclui uma tarefa específica da lista.

## Como Usar

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/Brunopln12/gerenciamento_tarefas.git
   cd gerenciamento_tarefas
   ```

2. **Executar o Script**

   Certifique-se de ter o Python instalado em sua máquina. Para executar o script, use o comando:

   ```bash
   python gerenciamento_tarefas.py
   ```

3. **Navegar no Menu**

   Utilize o menu interativo para adicionar, exibir, buscar, atualizar ou excluir tarefas.

## Estrutura do Código

- **Funções Principais:**
  - `adicionar_tarefas(descricao, responsavel)`: Adiciona uma nova tarefa.
  - `exibir_tarefas(tarefas)`: Exibe todas as tarefas.
  - `buscar_tarefa_responsavel(tarefas, responsavel)`: Busca tarefas pelo responsável.
  - `buscar_tarefa_descricao(tarefas, descricao)`: Busca tarefas pela descrição.
  - `atualizar_tarefa()`: Atualiza o responsável ou a descrição de uma tarefa.
  - `excluir_tarefa(tarefas)`: Exclui uma tarefa específica.
  
- **Menu Principal:**
  - `while True`: Loop principal que exibe o menu e permite a seleção de opções.

## Exemplo de Uso

Ao executar o script, você verá um menu interativo como este:

```
MENU

[a] Adicionar Tarefas
[e] Exibir Tarefas
[b] Buscar tarefas
[at] Atualizar tarefas
[ex] Excluir tarefas
[q] Sair

=> 
```

### Adicionar uma Tarefa

Selecione a opção `a` e forneça a descrição e o responsável pela tarefa.

### Exibir Tarefas

Selecione a opção `e` para exibir todas as tarefas adicionadas.

### Buscar Tarefas

Selecione a opção `b` e escolha buscar pelo responsável (`r`) ou pela descrição (`d`).

### Atualizar Tarefas

Selecione a opção `at` e escolha atualizar o responsável (`r`) ou a descrição (`d`) de uma tarefa existente.

### Excluir Tarefas

Selecione a opção `ex` para excluir uma tarefa fornecendo o responsável e a descrição.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

---

**Autor:** Bruno Pinho Lôbo Nascimento

**Contato:** seu.email@exemplo.com
