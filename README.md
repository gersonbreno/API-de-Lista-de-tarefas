AQui a dcomentçao do uso dessa api
https://api-de-lista-de-tarefas.onrender.com/api/swagger/
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API de Lista de Tarefas</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }

        .container {
            max-width: 800px;
            margin: 20px auto;
            padding: 20px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 5px;
        }

        h1 {
            font-size: 36px;
            margin-bottom: 20px;
            color: #333;
            text-align: center;
        }

        h2 {
            font-size: 24px;
            margin-bottom: 15px;
            color: #333;
        }

        p {
            font-size: 16px;
            margin-bottom: 15px;
            color: #333;
        }

        code {
            font-family: Consolas, monospace;
            font-size: 14px;
            background-color: #f8f8f8;
            padding: 2px 4px;
            border-radius: 3px;
        }

        pre {
            background-color: #f8f8f8;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }

        pre code {
            display: block;
            white-space: pre;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>API de Lista de Tarefas</h1>
        
        <p>Bem-vindo à API de Lista de Tarefas! Esta API foi desenvolvida com Django Rest Framework (DRF) e oferece uma maneira simples e eficiente de gerenciar suas tarefas.</p>

        <h2>Recursos</h2>
        <ul>
            <li><strong>Autenticação</strong>: A API suporta autenticação de token para garantir a segurança dos seus dados.</li>
            <li><strong>Operações CRUD</strong>: Você pode criar, ler, atualizar e excluir tarefas facilmente.</li>
            <li><strong>Filtragem e Ordenação</strong>: É possível filtrar e ordenar suas tarefas com base em diferentes critérios.</li>
            <li><strong>Paginação</strong>: A resposta da API é paginada para lidar com grandes conjuntos de dados de forma eficiente.</li>
        </ul>

        <h2>Requisitos do Sistema</h2>
        <ul>
            <li>Python 3.10 ou versão mais recente</li>
            <li>Pip 22.0 ou versão mais recente</li>
            <li>Virtualenv 20.19 ou versão mais recente</li>
        </ul>

        <h2>Instalação Rápida</h2>
        <pre><code>git clone https://github.com/seu_usuario/sua_api_de_tarefas.git
cd sua_api_de_tarefas
python3 -m venv venv
venv\Scripts\activate   # No Windows
source venv/bin/activate   # No macOS e Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver</code></pre>

        <p>Agora você pode acessar a API em <code>http://localhost:8000/</code> e a interface de administração em <code>http://localhost:8000/admin/</code>. Use as credenciais do superusuário que você criou para fazer login na interface de administração.</p>

        <h2>Endpoints da API</h2>
        <ul>
            <li><strong>Listar todas as tarefas</strong>: <code>GET /api/tasks/</code></li>
            <li><strong>Criar uma nova tarefa</strong>: <code>POST /api/tasks/</code></li>
            <li><strong>Obter detalhes de uma tarefa específica</strong>: <code>GET /api/tasks/&lt;task_id&gt;/</code></li>
            <li><strong>Atualizar uma tarefa existente</strong>: <code>PUT /api/tasks/&lt;task_id&gt;/</code></li>
            <li><strong>Excluir uma tarefa</strong>: <code>DELETE /api/tasks/&lt;task_id&gt;/</code></li>
        </ul>

        <h2>Autenticação</h2>
        <p>Para acessar os endpoints da API, você precisará fornecer um token de autenticação válido. Você pode obter um token enviando uma solicitação POST para <code>/api/token-auth/</code> com suas credenciais de usuário (nome de usuário e senha). O token será retornado na resposta e você deve incluí-lo no cabeçalho <code>Authorization</code> de todas as solicitações subsequentes no formato <code>Token &lt;seu_token&gt;</code>.</p>

        <h2>Testes</h2>
        <p>Você pode executar os testes da API usando o pytest. Basta executar o seguinte comando:</p>
        <pre><code>pytest</code></pre>

        <p>Isso executará todos os testes no diretório <code>tests/</code>.</p>

        <h2>Documentação Adicional</h2>
        <p>Para mais informações sobre os recursos e endpoints da API, consulte a documentação oficial em <code>docs/</code>.</p>

        <p>Se você tiver alguma dúvida ou encontrar problemas, sinta-se à vontade para abrir uma issue neste repositório. Aproveite a API de Lista de Tarefas!</p>
    </div>
</body>
</html>
