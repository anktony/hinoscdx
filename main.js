function carregarMusicas() {
    fetch('musicas.json')
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
        tituloTom.textContent = `${musica.id}. ${musica.Titulo} - Tom: ${musica.Tom}`;
        divMusica.appendChild(tituloTom);

        // const recebidoPor = document.createElement('div');
        // recebidoPor.classList.add('recebido-por');
        // recebidoPor.textContent = 'Recebido por: ' + musica['Recebido por'];
        // divMusica.appendChild(recebidoPor);

        const letra = document.createElement('div');
        letra.classList.add('letra');
        letra.textContent = musica.Letra;
        divMusica.appendChild(letra);

        musicasContainer.appendChild(divMusica);
    });
}

carregarMusicas();
