# Lista de Tarefas (To-Do-List)

**Sistema desenvolvido em Python para gerenciamento de tarefas. A aplicação permite registrar novas atividades, exibir a lista completa, atualizar status e remover itens, utilizando uma interface web simples com HTML e CSS integrada ao Flask. O foco é oferecer uma ferramenta direta, funcional e objetiva para organização do dia a dia.**

## Criadores

• Vinícius Teles dos Santos Silva – Front-End  
• Matheus de Souza Castro – Back-End  
• Gabriel do Nascimento de Souza – Front-End  
• Heitor Luiz Pereira Vasconcelos – Scrum Master  
• Luis Davi Peidão Silva – Back-End  

---

## Funcionalidades Principais

• Cadastro de tarefas com título, descrição, data limite e prioridade  
• Visualização da lista completa de tarefas  
• Atualização de status (pendente, concluída)  
• Exclusão de tarefas (remoção do JSON)  
• Interface web com HTML e CSS  
• Integração com Flask (backend em Python)  
• Encerramento seguro do sistema  

---

## Tecnologias Utilizadas

• Linguagens: **Python, HTML, CSS**  
• Framework: **Flask**  
• Persistência: **JSON**  
• Bibliotecas: **json, os, datetime, flask**

---

## Estrutura de Dados

### Arquivo raiz (JSON object / dict)

A estrutura principal é um objeto JSON no qual cada tarefa é armazenada como uma chave única.

**Chave (nome da tarefa):**
Tipo: `string`  
Observação: o nome é usado como chave principal. Nomes duplicados podem causar conflitos.

### Campos da tarefa

**status**  
Tipo: `string`  
Valores possíveis: `"pendente", "concluída"`


---

## Comportamento no Código

• `adicionar_tarefa` cria nova tarefa com status **"pendente"**  
• `atualizar_status` modifica o status de uma tarefa existente  
• `remover_tarefa` apaga a tarefa do JSON  


---

## Requisitos Funcionais

• CRUD de tarefas (criar, ler, atualizar e excluir)  
• Organização por categorias  
• Controle de status   
• Filtros e busca  
• Relatório de tarefas  
• Suporte a exportação em JSON / CSV  

---

## Requisitos Não Funcionais

• Persistência local em arquivo JSON  
• Interface simples, intuitiva e responsiva  
• Boas práticas de organização de código  
• Escalabilidade básica (até milhares de tarefas)  
• Segurança contra entradas inválidas  
• Desempenho satisfatório para uso cotidiano  

---

## Testes

### Testes Unitários (mínimo 3)

1. **Teste de criação de tarefa**
   - Verifica se uma nova tarefa é corretamente adicionada ao arquivo JSON
   - Resultado esperado: tarefa salva com status "pendente"
   - Resultado obtido: ✅ Sucesso

2. **Teste de atualização do status**
   - Altera o status de "pendente" para "concluída"
   - Resultado esperado: alteração registrada no JSON
   - Resultado obtido: ✅ Sucesso

3. **Teste de remoção de tarefa**
   - Remove uma tarefa existente
   - Resultado esperado: tarefa não aparecer mais no sistema
   - Resultado obtido: ✅ Sucesso

---

### Teste de Integração (mínimo 1)

**Integração Flask + HTML + JSON**

Foi testado o funcionamento completo da aplicação via navegador:

- O usuário adiciona uma tarefa pelo formulário HTML
- O Flask recebe os dados
- O JSON é atualizado
- A nova tarefa aparece na lista automaticamente

✅ Resultado: Integração funcionando perfeitamente entre front-end e back-end.

---

## Relatório de Testes

**O que foi testado:**
- Cadastro de tarefas
- Atualização de status
- Exclusão de tarefas
- Integração do formulário com Flask

**Resultados:**
- Todos os testes tiveram êxito
- Sem falhas críticas detectadas

**Problemas detectados:**
- Possibilidade de conflito com nomes de tarefas iguais (mesma chave no JSON)
- Falta de verificação avançada de datas inválidas

**O que ainda precisa de testes:**
- Testes de carga (muitas tarefas)
- Testes com múltiplos usuários
- Validação mais rigorosa de datas e entradas
- Sistema de backup e restauração

---

## Checklist do Projeto

✓ Funcionalidades expandidas (novos módulos e regras)  
✓ Integração do sistema funcionando (Flask + HTML + CSS + JSON)  
✓ Testes unitários e integração documentados  
✓ Git organizado (branches, commits e versionamento)  
✓ UML atualizado  
✓ Validação de requisitos funcionando  
✓ Projeto revisado e documentado  

---
## Diagrama de Classes

![Imagem do WhatsApp de 2025-11-26 à(s) 23 03 55_313b7c96](https://github.com/user-attachments/assets/484d01a6-0a57-4cad-8f28-b530c0c06b2e)

---

## Diagrama de casos de uso

![Imagem do WhatsApp de 2025-11-26 à(s) 22 51 22_3b5030e2](https://github.com/user-attachments/assets/72b67354-c867-44c5-8cdc-2119b0b30497)

**Projeto desenvolvido como parte da disciplina de Engenharia de Software / Desenvolvimento Web — UNINASSAU**
