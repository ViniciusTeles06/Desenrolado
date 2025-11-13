# Lista de tarefas (To-Do-List)

**Sistema desenvolvido em Python para gerenciamento básico de tarefas. A aplicação permite registrar novas atividades, exibir a lista completa de tarefas cadastradas, remover itens selecionados e encerrar o programa de forma simples e objetiva. O foco é oferecer uma ferramenta direta, funcional e fácil de utilizar no dia a dia.**
# Criadores

**• Vinicius teles dos santos silva -Back-End**

**• Matheus de souza castro -Back-End**

**• Gabriel do nascimento de souza -Front-End**

**• Heitor luiz Pereira Vasconcelos -Scrumm-Master**

**• Luis davi peidão Silva -Front-End**

# Funcionalidades Principais


**• Cadastro de tarefas: adicione novas atividades informando título, descrição e prioridade.**

**• Gerenciamento da lista: visualize todas as tarefas registradas, organizadas de forma simples e objetiva.**

**• Atualização e exclusão: marque tarefas como concluídas ou remova itens que já não são necessários.**

**• Encerramento seguro: finalize o programa de forma controlada, garantindo que todos os dados da sessão sejam mantidos.**

# Trello



# Link:
https://trello.com/b/jyAGxS42/lista-de-tarefas-cc


# Diagrama de Classes

![Imagem do WhatsApp de 2025-11-12 à(s) 20 21 48_67e6ccbf](https://github.com/user-attachments/assets/f0df647f-1c1f-469a-b4d8-b9dc8bdefdd2)


# Diagrama de casos de uso

![Imagem do WhatsApp de 2025-11-12 à(s) 21 01 19_fd6cd0f6](https://github.com/user-attachments/assets/a398d249-e44e-4a6f-b577-0a8e5cad3cd6)


# Tecnologias Utilizadas
**•	Linguagem: Python (modo console)**

**•	Persistência: arquivo texto tarefas.txt**

**•	Bibliotecas padrão: os**
  
# Estrutura de Dados

## arquivo raiz: JSON object / dict
**chave (nome da tarefa): string**
**(uso atual: o código usa o próprio nome da tarefa como chave key = nome — atenção a nomes duplicados/maiúsculas).**

## status:
**tipo: string**
**valores possíveis: "pendente", "em andamento", "concluída"**
**restrição: deve ser uma dessas opções.**

## comportamento no código: 
**adicionar_tarefa cria uma nova entrada com status "pendente".**
**atualizar_status altera o status da tarefa existente.**
**remover_tarefa deleta a tarefa do dicionário.**

## prioridade:
**tipo: inteiro (int)**
**restrição: 1 <= prioridade <= 5 (1 = mais urgente, 5 = menos urgente).**
**comportamento no código: usada para ordenar a exibição das tarefas no relatório.**

## data_limite: 
**tipo: string com formato "dd/mm/YYYY" ou null**
**null indica tarefa sem data definida.**

## observado pelo código:  
**tradutor_str_pra_data aceita entrada "dd/mm/YYYY" ou "dd/mm/YY", retorna date.**
**_format_data_limite padroniza para "dd/mm/YYYY" ao salvar.**
**_esta_atrasada compara com date.today().**

## Invariantes importantes: 

**Se data_limite for null, _esta_atrasada trata como não atrasada.**
**Sempre que uma tarefa é removida, a chave correspondente é deletada do JSON.**
**O código assume que status e prioridade existem e são válidos — corrupção do arquivo pode causar exceções.**
**Toda nova tarefa começa com status “pendente” e prioridade 3 por padrão.**

# Requisitos

# Funcionalidades Principais

**· CRUD de tarefas (criar / ler / atualizar / excluir — preferencialmente soft delete para permitir restauração).**
**· Categorias de tarefas (organização hierárquica — ex.: trabalho, estudos, pessoal).**
**· Prioridades (níveis de urgência: 1 a 5).**
**· Controle de status (pendente, em andamento, concluída).**
**· Datas de criação e prazo final com cálculo automático de tarefas atrasadas.**
**· Histórico de alterações (quem criou, modificou ou concluiu a tarefa e quando).**
**· Anexos e observações opcionais por tarefa (ex.: links, notas, arquivos de referência).**
**· Relatórios e filtros (tarefas atrasadas, concluídas, por prioridade, por categoria).**
**· Busca por nome e ordenação por data, prioridade ou status.**
**· Painel/Dashboard com resumo de progresso (tarefas totais, pendentes, concluídas, atrasadas).**
**· Notificações ou alertas (opcional, para prazos próximos ou tarefas atrasadas).**
**· Importação/Exportação em formatos CSV ou JSON.**
**· Backups automáticos e versionamento básico do arquivo principal (JSON).**

# Requisitos Não Funcionais

**· Persistência durável: arquivo JSON local ou banco leve (SQLite), garantindo integridade após fechamento.**
**· Autenticação segura (quando multiusuário) com controle de permissões:**

**Leitor (read) – pode visualizar.**

**Editor (write) – pode adicionar e editar.**

**Administrador (admin) – pode excluir, restaurar e alterar configurações.**
**· Interface gráfica responsiva e intuitiva (Tkinter, PyQt ou web com HTML/CSS/JS).**
**· Escalabilidade leve: deve suportar desde 1 até milhares de tarefas sem degradação perceptível.**
**· Segurança: proteção contra injeção de comandos (especialmente se houver entrada de texto livre).**
**· Internacionalização: suporte a diferentes idiomas e formatos de data.**
**· Logs e auditoria interna: registro de ações (adição, exclusão, conclusão, alteração de status).**
**· Backups e recuperação: criação automática de cópia de segurança e restauração em caso de falha.**
**· Desempenho: carregamento e listagem das tarefas em < 1s para até 1000 registros.**
**· Privacidade: dados locais armazenados apenas no dispositivo do usuário, com opção de exclusão total.**
