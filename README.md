### Teste engenheiro de dados -  Datasprints
<details>
  <summary>
  Clique aqui para maiores informações sobre o teste
  </summary>
<p>

<p align="center">
  <a href="https://datasprints.com/">
    <img src="https://data-sprints-candidate-luizvidal.s3.us-east-2.amazonaws.com/logo.png" alt="Data Sprints" width="256" height="128">
  </a>
</p>

#### Arquitetura

Em resumo, segue uma imagem sobre a arquitetura utilizada:
- Os dados vem do bucket S3 da Data Sprints
- Apache Airflow faz o processo de extract e limpeza dos dados carregando-os no "data-lake" da Amazon em modelo batch
- Nifi faz o mesmo processo que o Airflow, com a diferença que pode ser usado como um streaming de dados
- Athena consulta os dados sobre o s3
- Tableau conecta-se ao Athena via ODBC
- Outras tecnologias: Python, SQL, Shell Scripting, Docker-Compose.
                                                                                                    
#### Tecnologias utilizadas:

> Scripts shell/AWS cli

Comandos utilizados: 
    Linux: mkdir -p, curl, sed, rm -rf, 
    AWS Cli: aws s3 cp

* [Curl](https://raw.githubusercontent.com/lvvidal/ds/master/dags/copy/create_folder.sh)
* [AWS Cli](https://raw.githubusercontent.com/lvvidal/ds/master/dags/copy/upload_s3.sh)

> Python : DAG Airflow (Operators: Bash, Python, Dummy), além de script de auxílio aos operadores (tasks).

Bibliotecas (os, csv, json, sys, shutil)

* [Dags](https://raw.githubusercontent.com/lvvidal/ds/master/dags/copy/copy_S3.py)
* [Utils](https://raw.githubusercontent.com/lvvidal/ds/master/dags/scripts/utils.py)

> SQL : Scripts usados para criação das tabelas pasta _raw (tabelas com dados do jeito que foram colocados no S3, sem transformação), tabelas pasta _processed (tabelas que foram transformadas, alguns campos que serão usados na análise já estão calculados) e pasta _results (scripts que trazem as mesmas respostas que são obtidas com ferramenta de visualização de dados)

* [Raw](https://raw.githubusercontent.com/lvvidal/ds/master/dags/sql/raw/create_trips.sql)
* [Processed](https://raw.githubusercontent.com/lvvidal/ds/master/dags/sql/processed/fact_trips.sql)
* [Answers](https://raw.githubusercontent.com/lvvidal/ds/master/dags/sql/answers/results.sql)

> Apache Airflow: ferramenta para gerenciamento de fluxos de trabalho, através de códigos Python, com possibilidade de agendamento de tarefas.

DAG :

![image](https://raw.githubusercontent.com/lvvidal/ds/master/images/airflow.png)

> Nifi : ferramenta para fluxo de dados em streaming, no nosso cenário, faz o mesmo que o Airflow, mas pode ser usada para um fluxo ininterrupto de dados, seja de fontes oriúndas de IoT, bancos de dados, arquivos, etc.

Fluxo de Dados:

* [Template](https://raw.githubusercontent.com/lvvidal/ds/master/nifi/Data_Sprints.xml)

Group Principal : Contém os subgroups (Extract & Load)

![image](https://raw.githubusercontent.com/lvvidal/ds/master/images/nifi_main.png)

Extract: copia os arquivos dos buckets do S3 da Data Sprints e move-os para a pasta do docker do Nifi

![image](https://raw.githubusercontent.com/lvvidal/ds/master/images/nifi_extract.png)

Load: faz a limpeza dos arquivos csv e json, quebra os arquivos json em linhas e depois junta-os novamente fazendo merge, transforma e csv e faz o upload de todos os arquivos novamente para o S3.

![image](https://raw.githubusercontent.com/lvvidal/ds/master/images/nifi_load.png)

> Tableau : ferramenta para visualização de dados, utilizada no nosso cenário para algumas análises referentes aos dados sobre viagens de táxi de NYC.

Dashboard: ao acessar o dashboard, existe um "radio button" na parte superior da tela, basta clicar nas opções para ir trocando o painel que será exibido. Cada painel representar uma resposta diferente do teste.

![image](https://raw.githubusercontent.com/lvvidal/ds/master/images/tableau.png)

Link para acessar o dashboard
* [Tableau](https://public.tableau.com/profile/luiz.vinicius.vidal#!/vizhome/DataSprints/TestDataEngineer?publish=yes)

## Observação
Estou utilizando minha conta pessoal da AWS e portanto deixei a máquina onde roda o Airflow e Nifi desligadas, portanto se possível entrar em contato para que eu possa subir as máquina e passar os links para que seja possível acessar o que está na cloud.
Informei isto por e-mail também para: recrutamento@datasprints.com 

#### Data-Engineer

Em caso de dúvidas, favor contactar:
Luiz Vinicius Vidal <br>

- [E-mail](mailto:lvvidal@gmail.com)
- [Linkedin](https://www.linkedin.com/in/vinicius-vidal-b5849458/)

</p>
</details>
