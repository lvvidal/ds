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

> Scripts shell/AWS cli: criação de pastas, curl, sed, aws s3 cp

* [Curl](https://raw.githubusercontent.com/lvvidal/ds/master/dags/copy/create_folder.sh)
* [AWS Cli](https://raw.githubusercontent.com/lvvidal/ds/master/dags/copy/upload_s3.sh)

> Python : DAG Airflow (Operators: Bash, Python, Dummy), além de script de auxílio aos operadores (tasks).

* [Dags](https://raw.githubusercontent.com/lvvidal/ds/master/dags/copy/copy_S3.py)
* [Utils](https://raw.githubusercontent.com/lvvidal/ds/master/dags/scripts/utils.py)

#### Data-Engineer

Em caso de dúvidas, favor contactar:
Luiz Vinicius Vidal <br>

- [E-mail](mailto:lvvidal@gmail.com)
- [Linkedin](https://www.linkedin.com/in/vinicius-vidal-b5849458/)

</p>
</details>
