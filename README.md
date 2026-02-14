# Sistema de Vacinação de Pets 🐾💉

## Visão Geral

O **Sistema de Vacinação de Pets** é uma aplicação web desenvolvida para gerenciar o cadastro de pets, clínicas, profissionais de saúde e controle de vacinas.  
Ele permite que **múltiplas clínicas utilizem o sistema simultaneamente**, acompanhando de forma independente o histórico de vacinação dos pets, cadastrando profissionais e vacinas, e gerenciando informações de forma segura e organizada.

O sistema foi desenvolvido com foco em **facilidade de uso, modularidade e escalabilidade**, sendo uma solução prática para clínicas veterinárias de pequeno, médio e grande porte.
---
## Diagrama MER

![Diagrama MER do Sistema](assets/diagrama_mer.png)

O **Diagrama MER (Modelo Entidade-Relacionamento)** mostra a estrutura de dados do sistema, representando todas as entidades principais e seus relacionamentos:

- **Clínica** → Cada clínica possui seus próprios **profissionais**,**tutores**, **pets**, **tutores**, **vacinas** e **vacinação**, permitindo uso multi-clínicas.  
- **Tutor** → Representa o dono do pet, vinculado a uma clínica.  
- **Pet** → Cada pet pertence a um tutor e pode receber diversas vacinas ao longo do tempo.  
- **Vacina** → Lista de vacinas disponíveis na clinica.  
- **Vacinação** → Registra a aplicação de uma vacina em um pet, realizada por um profissional em uma clínica.  
- **Profissional** → Profissionais vinculados a clínicas, responsáveis pela aplicação das vacinas.

Esse diagrama garante que **os dados sejam consistentes e relacionados corretamente**, facilitando consultas e mantendo a integridade entre pets, tutores, profissionais e vacinas.

## Tecnologias Utilizadas

- **Linguagem:** Python 3.x  
- **Framework Web:** Django (com Django REST Framework para APIs)  
- **Banco de Dados:** SQLite  
- **Gerenciamento de Dependências:** pip / virtualenv  
- **Controle de Versão:** Git / GitHub  

---

## Descrição Geral das Rotas / Endpoints

### Clínicas
- `POST /api/clinics/` → Cria nova clínica  
- `GET /api/clinics/<id>/` → Detalhes de uma clínica  
- `PUT /api/clinics/<id>/` → Atualiza clínica  
- `DELETE /api/clinics/<id>/` → Remove clínica  

### Profissionais
- `GET /api/professionals/` → Lista profissionais  
- `POST /api/professionals/` → Cria profissional  
- `GET /api/professionals/<id>/` → Detalhes do profissional  
- `PUT /api/professionals/<id>/` → Atualiza profissional  
- `DELETE /api/professionals/<id>/` → Remove profissional  

### Tutores
- `GET /api/tutors/` → Lista todos os tutores  
- `POST /api/tutors/` → Cadastra novo tutor  
- `GET /api/tutors/<id>/` → Detalhes do tutor  
- `PUT /api/tutors/<id>/` → Atualiza tutor  
- `DELETE /api/tutors/<id>/` → Remove tutor  

### Pets
- `GET /api/pets/` → Lista todos os pets  
- `POST /api/pets/` → Cadastra novo pet  
- `GET /api/pets/<id>/` → Detalhes do pet  
- `PUT /api/pets/<id>/` → Atualiza pet  
- `DELETE /api/pets/<id>/` → Remove pet  

### Vacinas
- `GET /api/vaccines/` → Lista vacinas  
- `POST /api/vaccines/` → Cadastra nova vacina  
- `GET /api/vaccines/<id>/` → Detalhes da vacina  
- `PUT /api/vaccines/<id>/` → Atualiza vacina  
- `DELETE /api/vaccines/<id>/` → Remove vacina  

### Vacinações (registro de aplicação de vacinas)
- `GET /api/vaccinations/` → Lista todas as vacinações realizadas  
- `POST /api/vaccinations/` → Registra uma nova vacinação (pet + vacina + data + profissional)  
- `GET /api/vaccinations/<id>/` → Detalhes de uma vacinação específica  
- `PUT /api/vaccinations/<id>/` → Atualiza registro de vacinação  
- `DELETE /api/vaccinations/<id>/` → Remove registro de vacinação  
