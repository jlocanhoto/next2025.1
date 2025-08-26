# NExT 2025.1

### Primeiros passos

Esses passos só devem ser feitos uma única vez.

#### Python

Instale uma versão do Python de preferência acima da versão 3.12: https://www.python.org/downloads/


#### Poetry

Instale o Poetry, seguindo as instruções de acordo com o seu sistema operacional: https://python-poetry.org/docs/#installing-with-the-official-installer

Lembre-se de adicionar o caminho do Poetry a sua `$PATH`.

#### Dependências do projeto

Instale todas as dependências do projeto:

```
poetry install
```

### Execução dos códigos

Sempre que abrir um novo terminal para executar os códigos desse projeto, faça os passos a seguir.

Selecione o ambiente virtual Python do projeto:

```
poetry env use .venv/bin/python
```

Obtenha o comando para ativar o seu ambiente virtual com:

```
poetry env activate
```

Copie o comando que seu terminal mostrou e execute-o para ativar o ambiente virtual Python.

No meu caso, como estou usando o Linux, o comando acima retornou:

```
source /home/jloc/Documentos/next2025.1/.venv/bin/activate.fish
```

No Windows, geralmente o comando para Powershell é:

```
.\.venv\Scripts\activate.ps1
```
