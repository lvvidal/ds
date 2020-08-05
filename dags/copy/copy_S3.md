### Dag: Copy S3
<details>
  <summary>
  Clique aqui para maiores informações sobre a Dag
  </summary>
<p>

<p align="center">
  <a href="https://datasprints.com/">
    <img src="https://data-sprints-candidate-luizvidal.s3.us-east-2.amazonaws.com/logo.png" alt="Data Sprints" width="256" height="128">
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
    <td class="texto" rowspan="6">Esta task faz o download dos arquivos de payment, vendor e trips do bucket da data-sprints.</td>
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
    <td class="subheader">clean_task</td>
    <td class="texto">Dummy task apenas para entendimento do fluxo.</td>
  </tr>
  <tr>
    <td class="subheader">clean_csv</td>
    <td class="texto" rowspan="2">Essas tasks fazem a limpeza tanto dos csv's, removendo um header extra do arquivo payment e transformam os arquivos json que estão em um formato no qual não é possível transforma-lo em csv.</td>
  </tr>
  <tr>
    <td class="subheader">clean_json</td>
  </tr> 
  <tr>
    <td class="subheader">json_to_csv</td>
    <td class="texto">Esta task converte os arquivos json's em arquivos csv.</td>
  </tr>
  <tr>
    <td class="subheader">move_files</td>
    <td class="texto">Esta task move os arquivos csv para a pasta load, pasta na qual a task do s3 irá buscar os arquivos que serão "upados" para nuvem.</td>
  </tr>
  <tr>
    <td class="subheader">upload_to_s3_extractJSON2009</td>
    <td class="texto" rowspan="6">Esta task faz o download dos arquivos de payment, vendor e trips do bucket da data-sprints.</td>
  </tr>
  <tr>
    <td class="subheader">upload_to_s3_extractJSON2010</td>
  </tr> 
  <tr>  
    <td class="subheader">upload_to_s3_extractJSON2011</td>
  </tr>
  <tr>
    <td class="subheader">upload_to_s3_extractJSON2012</td>
  </tr> 
  <tr>  
    <td class="subheader">upload_to_s3_extractCSVPayment</td>
  </tr>
  <tr>
    <td class="subheader">upload_to_s3_extractCSVVendor</td>
  </tr> 
  <tr>
    <td class="subheader">remove_old_files</td>
    <td class="texto">Task que remove os arquivos nas pastas dos contêiners, para que caso a dag execute novamente não venha a falhar.</td>
  </tr>
  <tr>
    <td class="subheader">end_log</td>
    <td class="texto">Task Final - apenas indica o horário de encerramento da execução do fluxo.</td>
  </tr>
</table><br>
                                                                                                                                               
#### Data-Engineer

Em caso de dúvidas, favor contactar:

- [Luiz Vidal](mailto:lvvidal@gmail.com)
- [Skype](callto:winicjusz.vidal)
- [Whatsapp](tel:+5541991335129)

</p>
</details>