# Portal de Accesso

![Captura de tela_2024-07-19_19-09-00](https://github.com/user-attachments/assets/e316b66c-f5cb-4043-81ad-d715442a8dc8)



## Descrição
Um sistema Escolar Américano escrito em inglês e feito totalmente em python, para permitir alunos a ver sua média escolar e ver suas notas em tempo real, e permitir para os professores alterarem as notas dos alunos
Todos os Dados dos logins São ficticios e foram criados apenas para esta aplicação, Para os alunos acessarem,eles teriam que consultar a secretaria da escola para obter o numero de matricula
e a senha é a data de nascimento 

## Proteções 
- **Todos os Inputs foram tratados para receber apenas dados veridicos**
- **Todos os Dados Foram Salvos no Banco de Dados Criptografados com Sha512**
- **Foi Utilizado Placeholders e tratamento de todos os inputs para previnir Ataques de injeção de código como SQL Injection e Cross Site-Scripting**
- **As entradas de dados foram tratadas para receber apenas Números inteiros**
- **Caracteres como "=", ";", "?" São proibidos**

## Tecnologias Utilizadas 
- **Mysql**
- **SHA512**
- **PySide6**
- **Python3.12.3**
- **QtDesigner**
- **Biblioteca sys**

## Funcionalidades do Portal de Accesso Escolar 
- **Logs Tratando diversos Erros, e exibindo esses erros na tela de forma**
- **Função para ver a senha digitada**
- **Limitação de caracteres nos inputs**
- **Identifica Após o Login Quais são Alunos e Professores e os encaminha para a pagina especifica**
- **Quando um retornar for clicado, todos os inputs são limpados automaticamente**

## Tela do Aluno 
![Captura de tela_2024-07-19_19-32-01](https://github.com/user-attachments/assets/685a907f-4d37-481a-8c28-23048f4fd610)

## Funcionalidades  
- **Exibe a nota do Aluno em tempo real**
- **Calcula e exibe a nota do aluno**
- **Mostra automaticamente um Welcome com o nome do Aluno**
- **Botão retornar e sair**
- **Exibe o Semestre Atual do aluno**

## Tela do Professor
![Captura de tela_2024-07-19_19-36-36](https://github.com/user-attachments/assets/d0d0f635-c39a-42ac-946a-0e56320dc6fc)

## Funcionalidades 
- **Função pesquisar e selecionar um aluno para mudar e ver as notas**
- **Função para selecionar qual Materia ira mudar a nota**
- **Na função pesquisar Aluno Mostrará o nome e todas as notas registradas**
- **Na pesquisa, caso seja inserido um codigo de matricula invalido ou incorreto, ira retornar uma tela de erro**
- **Caso o Aluno não exista será retornado uma pagina de erro**
- **Caso o Professor não insira uma categoria e clique em "set grade" Sera retornado uma tela de erro**
- **Caso ele clique em "set grade" e não tenha selecionado um estudante retornara um erro**

## Tela do Professor em funcionamento 
  ![Captura de tela_2024-07-19_20-03-09](https://github.com/user-attachments/assets/9b6648a1-a234-46f5-b8e2-bbfeea35c614)

## Menu de Ajuda 
![Captura de tela_2024-07-19_20-05-56](https://github.com/user-attachments/assets/df24c79b-137c-442b-aa88-05e087da0650)

## Funcionalidades 
- **No menu há uma opção de "I do not know my password", nesta opção sera explicado que a senha é a data de nascimento no formato "dd/mm/year"**
- **No menu há uma opção de "I do not know my matriculation Code",nesta opção sera explicado para o Aluno comparecer a secretaria da escola**


## Telas de erro do Portal de Accesso
- **Foram colocados apenas 3 Telas de Erros para não prejudicar a visibilidade**
![Captura de tela_2024-07-19_20-16-46](https://github.com/user-attachments/assets/77b4e3ff-fefb-4dc0-8c19-37b60686a41a)
![Captura de tela_2024-07-19_20-17-17](https://github.com/user-attachments/assets/65d2fc0d-c31b-4735-a70e-ef5931bc86ca)
![Captura de tela_2024-07-19_20-17-58](https://github.com/user-attachments/assets/a99d8fac-0dc1-43b9-9bb0-f250f761de1d)

## Telas de erro da Tela de Professores
- **Foram colocados apenas 3 Telas de Erros para não prejudicar a visibilidade**
![Captura de tela_2024-07-19_20-41-27](https://github.com/user-attachments/assets/06baca26-6d11-4d8a-8786-34c5ccc6a4fa)
![Captura de tela_2024-07-19_20-42-00](https://github.com/user-attachments/assets/59d10c60-125d-4845-9a55-8d034f88a1a0)
![Captura de tela_2024-07-19_20-42-23](https://github.com/user-attachments/assets/1bd173e4-dfb9-4c2d-baf8-72ac1dc095a7)

## Como os Dados ficam Salvos ( Tela DBeaver )
**Tabela dos Estudantes**
![Captura de tela_2024-07-19_20-45-49](https://github.com/user-attachments/assets/845b0409-0371-4340-9ac2-05c9590c0110)
**Tabela das Notas**
![Captura de tela_2024-07-19_20-46-05](https://github.com/user-attachments/assets/ca58f767-5f44-4a2d-ae56-d4381b9a8502)

## Observação
- **Todos os dados registrados na DB tem ligação entre si ,Caso algum seja apagado sera ocorrido uma operação Cascade e o id da outra tabela também sera apagado** 
- **Todos os dados são ficticios e não pertencem a nínguem**
  
