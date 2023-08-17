<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>




<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="src/road.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Road Mapper - Using UNET</h3>

  <p align="center">
    Rede Neural para segmentação de Mapas de Remissão.
    <br />
    <a href="https://www.kaggle.com/code/ludmiladias/multiclasses-unet?scriptVersionId=140214419"><strong>Arquivo no Kaggle >></strong></a>
    <br />
    <br />
    <a href="https://www.kaggle.com/datasets/ludmiladias/road-mapper-dataset-csv">Dataset</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/luddias/road_mapper-study/blob/main/Artigos_e_relatorios/IJCNN_2018_UFES_Raphael_Carneiro_Mapping_road_lanes_using_laser_remission_and_deep_neural_networks-1.pdf">Artigo</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Sumário</summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre o Projeto</a>
      <ul>
        <li><a href="#built-with">Tecnologias Utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Primeiros Passos</a>
      <ul>
        <li><a href="#prerequisites">Pré-requisitos</a></li>
        <li><a href="#installation">Instalação</a></li>
      </ul>
    </li>
    <li><a href="#usage">Colocando pra rodar!</a></li>
    <li><a href="#application">Aplicação</a></li>
    <li><a href="#acknowledgments">Referências</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contato</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->

## Sobre o Projeto

Projeto desenvolvido usando a rede de segmentação U-NET, biblioteca Keras e Tensorflow.
O Road Mapper DNN tem como objetivo gerar mapas de estrada com segmentação das faixas de sinalização utilizada pelos veículos, tendo como entrada mapas de remissão gerados pelo LIDAR - sensor laser que faz parte do sistema de carros autônomos como o ASTRO da Lume Robotics.

<div align="center">
  
  Input | Output
  ------|--------
  ![](https://github.com/LCAD-UFES/carmen_lcad/blob/master/src/road_mapper/data/i7705600_-338380.png?raw=true)|![](https://github.com/LCAD-UFES/carmen_lcad/blob/master/src/road_mapper/data/r7705600_-338380_map_1_6.png?raw=true)
</div>


<p align="right">(<a href="#readme-top">back to top</a>)</p>

Esse projeto foi feito utilizando como referência o artigo "Mapping Road Lanes using Laser Remission and Deep Neural Networks", entretanto utilizando-se uma rede neural de segmentaçõ semântica diferente e mais atual, U-NET, ao invés da E-NET.
O artigo usado como referência propõe o uso de Redes Neurais Profundas (Deep Neural Networks – DNN) para solucionar o problema de inferir a posição e as propriedades relevantes das faixas de trânsito urbanas com pouca ou nenhuma sinalização horizontal – subsistema da sinalização viária composta de marcas, símbolos e legendas, apostos sobre o pavimento da pista de rolamento – a fim de permitir a operação de carros autônomos nas descritas situações.
Nas vias urbanas, um carro autônomo deve permanecer dentro de uma faixa mantendo um espaço entre outros veículos, para que isso ocorra deve-se conter mapas internos das faixas das estradas. Os seres humanos fazem uso das sinalizações horizontais para se orientar quanto as estradas e existem vários trabalhos sobre como detectar essas marcações para se utilizar em sistemas ADAS, porém se essas marcas estiverem em condições ruins e o sistema depender somente disso, então se tornará impossível para o carro autônomo se locomover nas condições desejadas.

### Tecnologias Utilizadas

* [![Python.logo][Python]][py-url]
* [![Keras.logo][Keras]][keras-url]
* [![Tensorflow.logo][tf]][tf-url]
* [![numpy.logo][Numpy]][np-url]
  


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Colocando pra rodar!

### Pré-Requisitos
Siga um dos tutoriais abaixo para instalar a biblioteca Python caso esteja executando diretamente no seu dispositivo ao invés de um serviço em nuvem (colab, kaggle).

Obs.: Talvez seja necessário a instalação de outros pacotes além desse e dos que estão disponíveis no jupyter notebook do projeto.

 * ![baixarPython][windowsPy]
 * ![baixarMac][macPy]
 * ![baixarLinux][linuxPy]
  
### Execução
O projeto é dividido em duas partes: Geração de dados e Treinamento e Teste da Rede. As duas etapas se encontram no notebook mas deve-se realizar uma pausa após a primeira etapa para reiniciar o kernel e liberar a memória para a próxima etapa.
Com o objetivo de treinar uma grande quantidade de dados mesmo com hardware limitado, é se utilizado no treinamento o "batch_generator" uma função que acessa o arquivo json e resgata para uso apenas uma parte do tamanho do batch para o step. No próximo step, um novo batch é recuperado e os dados do batch anterior são descartados.
Sendo assim, após tratar e normalizar os dados do dataset eles devem ser salvos em um arquivo json.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Aplicação

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Referências

CARNEIRO, Raphael Vivacqua; GUIDOLINI, Ranik; CARDOSO, Vinicius Brito; NASCIMENTO, Rafael C. Mapping Road Lanes using Laser Remission and Deep Neural Networks. IEEE, [S. l.], p. 1-8, 27 abr. 2018. <br>Disponível em: https://www.researchgate.net/publication/324859984_Mapping_Road_Lanes_Using_Laser_Remission_and_Deep_Neural_Networks. 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contato

![adress][email-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
[keras]: https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white
[keras-url]: https://keras.io/
[tf]: https://img.shields.io/badge/Tensorflow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white
[tf-url]: https://www.tensorflow.org/?hl=pt-br
[python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[py-url]: https://www.python.org/
[Numpy]: https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white
[np-url]: https://numpy.org/
[windowsPy]: https://img.shields.io/badge/Instalar%20Python%20no%20Windows-0078D6?style=for-the-badge&logo=windows10&logoColor=white&link=https%3A%2F%2Fpython.org.br%2Finstalacao-windows%2F
[macPy]: https://img.shields.io/badge/Instalar%20Python%20no%20Mac%20OS-000000?style=for-the-badge&logo=apple&logoColor=white&link=https%3A%2F%2Fpython.org.br%2Finstalacao-mac%2F
[linuxPy]: https://img.shields.io/badge/Instalar%20Python%20no%20LInux-F09D13?style=for-the-badge&logo=linux&logoColor=white&link=https%3A%2F%2Fpython.org.br%2Finstalacao-linux%2F
[email-url]: https://img.shields.io/badge/ludmialdias.inf%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white



