﻿# Tutorial Instalação Django

1. Preparação  
Abra um terminal no seu sistema Ubuntu. Você pode fazer isso pressionando Ctrl + Alt + T ou procurando por "Terminal" no menu de aplicativos.


1. Atualização dos pacotesv  
Antes de começar, é uma boa prática atualizar os pacotes do sistema. Execute os seguintes comandos para atualizar a lista de pacotes e atualizar os pacotes instalados:

    >``sudo apt update``

    >``sudo apt upgrade``




1. Instalação do Python e do pip  
Django é um framework Python, portanto, é necessário ter o Python instalado. O Ubuntu geralmente já vem com o Python instalado. Verifique a versão do Python usando o seguinte comando:  

    >``python3 --version``

    Certifique-se de que a versão seja 3.6 ou superior. Além disso, verifique se o gerenciador de pacotes pip está instalado:

    >``sudo apt install python3-pip``


1. Criação de um ambiente virtual (opcional, mas recomendado)  
É altamente recomendado criar um ambiente virtual para isolar as dependências do projeto. Isso ajuda a evitar conflitos entre diferentes projetos Python. Para criar um ambiente virtual, execute os seguintes comandos:


    >``sudo apt install python3-venv``


    >``mkdir nome_do_projeto``


    >``cd nome_do_projeto``

    >``python3 -m venv venv``


    Isso criará um ambiente virtual chamado venv dentro da pasta nome_do_projeto.


1.  Ativação do ambiente virtual  
Agora, ative o ambiente virtual:


    > ``source venv/bin/activate``


    Se você fizer isso corretamente, o prompt do terminal deve mudar para indicar que você está agora dentro do ambiente virtual.


1. Instalação do Django  
    Com o ambiente virtual ativado, você pode usar o pip para instalar o Django:


    >``pip install Django``


1. Verificação da instalação
    Após a instalação, verifique se o Django foi instalado corretamente:


    >``django-admin --version``  

    Isso deve imprimir a versão do Django que você acabou de instalar.


    Passo 8: Desativação do ambiente virtual (opcional)
    Quando você terminar de trabalhar com o projeto, pode sair do ambiente virtual digitando:


    >``deactivate``


    Isso o levará de volta ao ambiente global do sistema.