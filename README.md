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
