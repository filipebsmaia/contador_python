<div align="center">
  
  <b>Aplicação Python desenvolvida para materia de Processamento Digital de Imagens!</b>

<!--  Shields -->
   <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/filipebsmaia/contador_python">

  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/filipebsmaia/contador_python">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/filipebsmaia/contador_python">
  <a href="https://github.com/filipebsmaia/contador_python/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/filipebsmaia/contador_python">
  </a>

  <a href="https://github.com/filipebsmaia/contador_python/issues">
    <img alt="Repository issues" src="https://img.shields.io/github/issues/filipebsmaia/contador_python">
  </a>

  <img alt="GitHub" src="https://img.shields.io/github/license/filipebsmaia/contador_python">
<!--  Shields -->
</div>
</br>

# Índice

- [Sobre](#sobre)
- [Tecnologias Utilizadas](#tecnologias)
- [Como Usar](#como-usar)

<a id="sobre"></a>

## :bookmark: Sobre

<p>
O <strong>contador_python</strong> foi uma aplicação desenvolvida para a materia de processamento digital de imagens. O objetivo era que a aplicação capturasse imagens provindas de uma camera e conseguisse processar, além de armazenar as imagens.
<p>

<a id="tecnologias"></a>

## :rocket: Tecnologias

O projeto foi desenvolvido utilizando as seguintes tecnologias:

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [OpenCV](https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.htmlhttps://nodejs.org/en/)
- [Numpy](https://numpy.org/)

<a id="como-usar"></a>

## :information_source: Como usar

- ### **Pré-requisitos**

Para clonar a aplicação você ira precisar do [Python](https://www.python.org/), [pip](https://pypi.org/project/pip/) instalado em seu computador.
Por linha de comando:

```sh
  # Clone o repósitorio
  $ git clone https://github.com/filipebsmaia/contador_python.git

  ## Instale as dependencias e configurações do backend
  $ pip3 install -r libs.txt

  # Acesse o arquivo index.py e altere o valor da variavel ``url`` para o endereço de sua camera ip
  # Caso não possua uma camera ip, você pode simular uma utilizando o aplicativo IPWEBCAM disponível para android, neste caso é necessário que o dispositivo e a aplicativo estejam na mesma rede.
  # No aplicativo, inicie o servidor na opção ``start server``, na tela ira ser exibido o ip no qual a aplicação está rodando, para esse aplicativo a url se dá por http://${IP_V4}:${PORTA}/video, onde ${IP_V4} é o endereço ip da camera e a ${PORTA} é a porta (normalmente 8080 ou 8088).

  # Inice a aplicação
  $ python index.py

  # O endereço ip da aplicação ira ser exibido no termal, basta acessar ou utilizar o ip abaixo
  # http://localhost:5000


```

</div>
