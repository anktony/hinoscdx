function carregarMusicas() {
    fetch('./Json/trezena_StAntonio_2023.json')
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
        tituloTom.textContent = `${musica.id}. ${musica.Titulo}` // - Tom: ${musica.Tom}`;
        divMusica.appendChild(tituloTom);

        const testaudio = document.createElement('audio');
        testaudio.src = `./audios/trezena/${musica.id}.mp3`
        testaudio.controls = true;
        testaudio.autoplay = false;
        testaudio.loop = true;
        testaudio.preload = "auto";
        testaudio.textContent = "This is the text inside the paragraph.";
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
