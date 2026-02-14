# Sistema de Vacinação de Pets 🐾💉

## Visão Geral

O **Sistema de Vacinação de Pets** é uma aplicação web desenvolvida para gerenciar o cadastro de pets, clínicas, profissionais de saúde e controle de vacinas.  
Ele permite que **múltiplas clínicas utilizem o sistema simultaneamente**, acompanhando de forma independente o histórico de vacinação dos pets, cadastrando profissionais e vacinas, e gerenciando informações de forma segura e organizada.

O sistema foi desenvolvido com foco em **facilidade de uso, modularidade e escalabilidade**, sendo uma solução prática para clínicas veterinárias de pequeno, médio e grande porte.
---
## Diagrama MER

![Diagrama MER do Sistema](assets/diagrama_mer.png)

O **Diagrama MER (Modelo Entidade-Relacionamento)** mostra a estrutura de dados do sistema, representando todas as entidades principais e seus relacionamentos:

- **Clínica** → Cada clínica possui seus próprios **profissionais**,**tutores**, **pets**, **vacinas** e **vacinação**, permitindo uso multi-clínicas.  
- **Tutor** → Representa o dono do pet, vinculado a uma clínica.  
- **Pet** → Cada pet pertence a um tutor e pode receber diversas vacinas ao longo do tempo.  
- **Vacina** → Lista de vacinas disponíveis na clinica.  
- **Vacinação** → Registra a aplicação de uma vacina em um pet, realizada por um profissional em uma clínica.  
- **Profissional** → Profissionais vinculados a clínicas, responsáveis pela aplicação das vacinas.

Esse diagrama garante que **os dados sejam consistentes e relacionados corretamente**, facilitando consultas e mantendo a integridade entre pets, tutores, profissionais e vacinas.

## Tecnologias Utilizadas

- **Linguagem:** Python 3 
- **Framework Web:** Django (com Django REST Framework para APIs)  
- **Banco de Dados:** SQLite  
- **Gerenciamento de Dependências:** pip / virtualenv  
- **Controle de Versão:** Git / GitHub  

---

## Descrição Geral das Rotas / Endpoints

### Clínicas
- `POST /api/clinica/` → Cria nova clínica  
- `GET /api/clinica/<id>/` → Detalhes de uma clínica  
- `PUT /api/clinica/<id>/` → Atualiza clínica  
- `DELETE /api/clinica/<id>/` → Remove clínica  

### Profissionais
- `GET /api/profissionais/` → Lista profissionais  
- `POST /api/profissionais/` → Cria profissional  
- `GET /api/profissionais/<id>/` → Detalhes do profissional  
- `PUT /api/profissionais/<id>/` → Atualiza profissional  
- `DELETE /api/profissionais/<id>/` → Remove profissional  

### Tutores
- `GET /api/tutor/` → Lista todos os tutores  
- `POST /api/tutor/` → Cadastra novo tutor  
- `GET /api/tutor/<id>/` → Detalhes do tutor  
- `PUT /api/tutor/<id>/` → Atualiza tutor  
- `DELETE /api/tutor/<id>/` → Remove tutor  

### Pets
- `GET /api/pets/` → Lista todos os pets  
- `POST /api/pets/` → Cadastra novo pet  
- `GET /api/pets/<id>/` → Detalhes do pet  
- `PUT /api/pets/<id>/` → Atualiza pet  
- `DELETE /api/pets/<id>/` → Remove pet  

### Vacinas
- `GET /api/vacina/` → Lista vacinas  
- `POST /api/vacina/` → Cadastra nova vacina  
- `GET /api/vacina/<id>/` → Detalhes da vacina  
- `PUT /api/vacina/<id>/` → Atualiza vacina  
- `DELETE /api/vacina/<id>/` → Remove vacina  

### Vacinações (registro de aplicação de vacinas)
- `GET /api/vacinacao/` → Lista todas as vacinações realizadas  
- `POST /api/vacinacao/` → Registra uma nova vacinação (pet + vacina + data + profissional)  
- `GET /api/vacinacao/<id>/` → Detalhes de uma vacinação específica  
- `PUT /api/vacinacao/<id>/` → Atualiza registro de vacinação  
- `DELETE /api/vacinacao/<id>/` → Remove registro de vacinação  
