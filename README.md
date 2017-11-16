# AdminLTE with Django

Exemplo de integração usando [Python 3.6](https://www.python.org/downloads) e **Django 1.11** com o template [AdminLTE 2.4.2](https://github.com/almasaeed2010/AdminLTE).

Exemplo baseado no repositório [adminLTE_Django](https://github.com/drfrink/adminLTE_Django).


Instalação e execução
---------------------------
1. Fazer o download deste repositório
2. Configurar o módulo **virtualEnv** e ativá-lo
    1. Se não tiver o módulo instalado, basta executar o comando 'pip install virtualenv' no terminal
    2. Navegar até o diretório do projeto - `cd (diretório do projeto)` - e executar o comando `virtualenv -p (caminho do executável de python 3.6) ENV`
    3. Ativar a virtualização do ambiente com o comando:
        1. `Scripts\activate.bat` **(No Windows)**
        2. `bash Scripts/activate.sh` **(No Linux)**
3. Executar o comando `pip install -r requirements.txt` para instalar as dependências
4. Executar o comando `python manage.py runserver` para executar o projeto


Execução
---------------------------
1. Navegar até o diretório do projeto - `cd (diretório do projeto)`
2. Ativar a virtualização do ambiente com o comando:
   1. `Scripts\activate.bat` (No Windows)
   2. `bash Scripts/activate.sh` (No Linux)
3. Executar o comando `python manage.py runserver` para executar o projeto


Observações
============
* **Os apps loginManager, dataTables e fileUpload estão em fase experimental então podem ocorrer alguns bugs.**
