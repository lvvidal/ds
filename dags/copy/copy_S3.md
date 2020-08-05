### Dag: Copy S3
<details>
  <summary>
  Clique aqui para maiores informações sobre a Dag
  </summary>
<p>

<p align="center">
  <a href="https://datasprints.com/">
    <img src="https://data-sprints-candidate-luizvidal.s3.us-east-2.amazonaws.com/logo.png" alt="Data Sprints" width="128" height="44">
  </a>
</p>

#### Propósito

Esta DAG faz o download dos arquivos csv e json do bucket disponibilizado pelo time da Data Sprints, faz a limpeza dos arquivos, removendo cabeçalho e transformando os arquivos json's em csvs. Em seguida move os arquivos para os buckets do candidato Luiz Vinicius Vidal. 

#### Tasks

Este workflow faz as seguintes tarefas:

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
.tg .header{border-color:inherit;font-weight:bold;text-align:center;vertical-align:center}
.tg .subheader{border-color:inherit;font-size:12px;color: red;font-weight:bold;text-align:left;vertical-align:center}
.tg .texto{border-color:inherit;font-size:12px;font-weight:normal;text-align:left;vertical-align:center}
</style>
<table class="tg">
  <tr>
    <th class="header">Task</th>
    <th class="header">Função</th>
  </tr>
  <tr>
    <td class="subheader">start_log</td>
    <td class="texto">Task Inicial - apenas indica o horário de início da execução do fluxo.</td>
  </tr>
  <tr>
    <td class="subheader">get_file_extractJSON2009</td>
    <td class="texto" rowspan="3">Esta task faz o download dos arquivos de payment, vendor e trips do bucket da data-sprints.</td>
  </tr>
  <tr>
    <td class="subheader">get_file_extractJSON2010</td>
  </tr> 
  <tr>  
    <td class="subheader">get_file_extractJSON2011</td>
  </tr>
  <tr>
    <td class="subheader">get_file_extractJSON2012</td>
  </tr> 
  <tr>  
    <td class="subheader">get_file_extractCSVPayment</td>
  </tr>
  <tr>
    <td class="subheader">get_file_extractCSVVendor</td>
  </tr> 
  <tr>
    <td class="subheader">create_athena_scci_securitizadora_raw</td>
    <td class="texto" rowspan="3">Esta task faz a criação - "CREATE" - dos bancos de dados  "raw" no Athena  - Securitizadora, Hipotecária e Banco.</td>
  </tr>
  <tr>
    <td class="subheader">create_athena_database_scci_hipotecaria_raw</td>
  </tr> 
  <tr>  
    <td class="subheader">create_athena_database_scci_banco_raw</td>
  </tr>
  <tr>
    <td class="subheader">remove_ddl_raw_securitizadora</td>
    <td class="texto" rowspan="3">Esta task limpa a pasta que contém os scripts .sql de criação de tabelas dos bancos "raw" no Athena  - Securitizadora, Hipotecária e Banco.</td>
  </tr>
  <tr>
    <td class="subheader">remove_ddl_raw_hipotecaria</td>
  </tr> 
  <tr>  
    <td class="subheader">remove_ddl_raw_banco</td>
  </tr>
  <tr>
    <td class="subheader">download_ddls_securitizadora_from_s3</td>
    <td class="texto" rowspan="3">Esta task faz o download dos scripts de criação de tabelas "raw" do Athena para a pasta local do servidor do Airflow - Securitizadora, Hipotecária e Banco.</td>
  </tr>
  <tr>
    <td class="subheader">download_ddls_hipotecaria_from_s3</td>
  </tr> 
  <tr>  
    <td class="subheader">download_ddls_banco_from_s3</td>
  </tr>
  <tr>
    <td class="subheader">create_raw_tables_securitizadora</td>
    <td class="texto" rowspan="3">Esta task executa todos os scripts .sql de criação de tabela para o banco de dados "Raw" do Athena, dependendo da origem dos dados, ou seja, Securitizadora, Hipotecária ou Banco, a tabela irá pertencer a seu banco de dados respectivo.</td>
  </tr>
  <tr>
    <td class="subheader">create_raw_tables_hipotecaria</td>
  </tr> 
  <tr>  
    <td class="subheader">create_raw_tables_banco</td>
  </tr>
  <tr>
    <td class="subheader">drop_athena_database_processed</td>
    <td class="texto">Esta task faz a deleção - "DROP" - dos bancos de dados "processed" no Athena.</td>
  </tr>
  <tr>
    <td class="subheader">create_athena_database_processed</td>
    <td class="texto">Esta task faz a criação - "CREATE" - dos bancos de dados "processed" no Athena.</td>
  </tr>
  <tr>
    <td class="subheader">create_processed_tables</td>
    <td class="texto">Esta task executa todos os scripts .sql de criação de tabela para o banco de dados "Processed" do Athena e também faz o "union" entre as tabelas de mesmo nome de bancos diferentes. Ex: tabela PRETENDENTE do banco da Hipotecária com tabela PRETENDENTE da Securitizadora irá se transformar em apenas um tabelas no banco de dados "Processed".</td>
  </tr>
  <tr>
    <td class="subheader">drop_athena_database_business</td>
    <td class="texto">Esta task faz a deleção - "DROP" - dos bancos de dados "business" no Athena.</td>
  </tr>
  <tr>
    <td class="subheader">create_athena_database_business</td>
    <td class="texto">Esta task faz a criação - "CREATE" - dos bancos de dados "business" no Athena.</td>
  </tr>
  <tr>
    <td class="subheader">end_log</td>
    <td class="texto">Task Final - apenas indica o horário de encerramento da execução do fluxo.</td>
  </tr>
</table><br>
                                                                                                                                               
#### Data-Team

Em caso de dúvidas, favor contactar:

- [Anderson Igarashi](mailto:anderson.igarashi@baripromotora.com.br)
- [Marcos Gritti](mailto:marcos.gritti@baritecnologia.com.br)
- [Luiz Vidal](mailto:luiz.vidal@baritecnologia.com.br)

</p>
</details>