const fs = require('fs');
const path = require('path');

let diretorioAudios = './audios/hinosdexango/'


function carregarMusicas() {
    fetch('./Json/hinosdexango.json')
        .then(response => response.json())
        .then(data => exibirMusicas(data))
        .catch(error => console.error('Ocorreu um erro ao carregar as músicas:', error));
}

function exibirMusicas(musicas) {
    const musicasContainer = document.getElementById('musicas');

    musicas.forEach(musica => {
        const divMusica = document.createElement('div');
        divMusica.classList.add('musica');

        const tituloTom = document.createElement('div');
        tituloTom.classList.add('titulo-tom');
        tituloTom.textContent = `${musica.id + 1}. ${musica.Titulo} - Tom: ${musica.Tom}`;
        divMusica.appendChild(tituloTom);

        const testaudio = document.createElement('audio');

        fs.readdirSync(diretorioAudios).forEach(nomeArquivo => {
            if (nomeArquivo.slice(0, 2) === musica.id) {
              testaudio.src = path.join(diretorioAudios, nomeArquivo);
              console.log(`O arquivo ${nomeArquivo} atende ao critério. Caminho: ${testaudio.src}`);
            }
          });

        // testaudio.src = `./audios/hinosdexango/${musica.id}.mp3`

        testaudio.controls = true;
        testaudio.autoplay = false;
        testaudio.loop = true;
        testaudio.preload = "auto";
        testaudio.style.width = "300px";
        testaudio.style.height = "50px";

        // const recebidoPor = document.createElement('div');
        // recebidoPor.classList.add('recebido-por');
        // recebidoPor.textContent = 'Recebido por: ' + musica['Recebido por'];
        // divMusica.appendChild(recebidoPor);

        const letra = document.createElement('div');
        letra.classList.add('letra');
        letra.textContent = musica.Letra;
        divMusica.appendChild(testaudio);
        divMusica.appendChild(letra);
        

        musicasContainer.appendChild(divMusica);
    });
}

carregarMusicas();
