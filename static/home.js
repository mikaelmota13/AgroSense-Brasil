// Função para alternar o menu hambúrguer
function toggleMenu() {
    var sidebar = document.querySelector('.sidebar');
    sidebar.classList.toggle('active');
}

// Fecha o menu ao clicar em um item do menu
const menuItems = document.querySelectorAll('.sidebar .menu-item'); // Substitua '.sidebar .menu-item' pelo seletor dos itens do seu menu
menuItems.forEach(item => {
    item.addEventListener('click', () => {
        toggleMenu();
    });
});

// Fecha a sidebar ao clicar fora dela e do menu hambúrguer
window.addEventListener('click', function (event) {
    var sidebar = document.querySelector('.sidebar');
    var hamburgerMenu = document.querySelector('.hamburger-menu');

    if (sidebar && hamburgerMenu && !sidebar.contains(event.target) && !hamburgerMenu.contains(event.target)) {
        sidebar.classList.remove('active');
    }
});

// Função para exibir o conteúdo correspondente ao botão clicado
function showContent(contentId) {
    document.querySelectorAll('.content').forEach(content => {
        content.classList.remove('active');
    });

    // Exibe o conteúdo correspondente
    const content = document.getElementById(contentId);
    if (content) {
        content.classList.add('active');
    }

    // Fecha o menu hambúrguer se ele estiver aberto
    var sidebar = document.querySelector('.sidebar');
    if (sidebar.classList.contains('active')) {
        sidebar.classList.remove('active');
    }
}

// Função para o botão "Sair"
function sair() {
    alert("Você saiu da aplicação.");
    window.location.href = 'login.html';
}

// Função para fechar o modal
function closeModal() {
    document.getElementById('modal').classList.remove('active');
}

// Função para abrir o modal
function openModal() {
    document.getElementById('modal').classList.add('active');
}

// Fecha o modal ao clicar fora dele
window.addEventListener('click', function (event) {
    var modal = document.getElementById('modal');
    var modalContent = document.querySelector('.modal-content');

    if (modal && modalContent && !modalContent.contains(event.target) && modal.contains(event.target)) {
        closeModal();
    }
});

// Função para enviar o formulário de cadastro
document.getElementById('cadastroForm').addEventListener('submit', function (e) {
    //e.preventDefault(); 
    alert("Setor cadastrado com sucesso!");
    closeModal();
});

// Função para pesquisar histórico
function pesquisarHistorico(event) {
    event.preventDefault();
    const dataInicio = document.getElementById('data-inicio').value;
    const dataFim = document.getElementById('data-fim').value;
    alert(`Pesquisando histórico de ${dataInicio} até ${dataFim}`);
}

// Função para fechar o overlay
function closeOverlay() {
    document.getElementById('overlay').classList.remove('active');
}

// Função para abrir o overlay
function openOverlay() {
    document.getElementById('overlay').classList.add('active');
}

function pesquisarHistorico(event) {
    event.preventDefault();
    const dataInicio = document.getElementById('data-inicio').value;
    const dataFim = document.getElementById('data-fim').value;

    const resultadoDiv = document.getElementById('resultado-pesquisa');
    resultadoDiv.innerHTML = `<h3>Resultados da Pesquisa</h3>
    <p>Exibindo dados de ${dataInicio} até ${dataFim}</p>
    <h4> No período foi realizado o monitoramento do sistema de irrigação na Fazenda Modelo - Setor 3. Durante esse tempo, foram coletados dados sobre temperatura ambiente, temperatura da água, umidade do solo e nível de irrigação.

A temperatura ambiente apresentou uma média de 28.5°C, com valores máximo e mínimo registrados de 35.2°C e 22.1°C, respectivamente. A temperatura da água manteve-se relativamente estável, com uma média de 24.8°C, atingindo um máximo de 29.3°C e um mínimo de 20.5°C.

A umidade do solo foi monitorada constantemente, apresentando uma média de 52.3%, com valores variando entre um máximo de 68.7% e um mínimo de 35.2%. O nível de irrigação foi ajustado conforme a necessidade, com uma média de 5.2 mm/dia, chegando a um máximo de 7.8 mm/dia e um mínimo de 2.5 mm/dia.

Durante o período analisado, observou-se que a temperatura ambiente permaneceu dentro do esperado para a época do ano, enquanto a temperatura da água não apresentou oscilações bruscas. A umidade do solo foi mantida acima do limite crítico, garantindo condições adequadas para o cultivo. O nível de irrigação foi regulado para evitar desperdício e garantir eficiência no uso da água.

Dessa forma, conclui-se que o sistema de irrigação funcionou de maneira eficiente ao longo do período avaliado. Os ajustes automáticos permitiram a manutenção da umidade do solo dentro dos parâmetros recomendados, sem excessos ou déficits hídricos. Não foram registradas anomalias significativas.

</h4>`;
    resultadoDiv.style.display = 'block';
}

function openClimaOverlay() {
    document.getElementById('clima-overlay').classList.add('active');
}

function closeClimaOverlay() {
    document.getElementById('clima-overlay').classList.remove('active');
}

// Fecha o overlay ao clicar fora dele
window.addEventListener('click', function(event) {
    var overlay = document.getElementById('clima-overlay');
    var content = document.querySelector('#clima-overlay .overlay-content');

    if (overlay && content && event.target === overlay) {
        closeClimaOverlay();
    }
});


// Adiciona um evento de clique na janela para fechar o overlay ao clicar fora dele
window.addEventListener('click', function (event) {
    var overlay = document.getElementById('overlay');
    var overlayContent = document.querySelector('.overlay-content');
    // Verifica se o clique ocorreu fora do conteúdo do overlay
    if (overlay && overlayContent && event.target === overlay) {
        closeOverlay();
    }
});