const socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

const messages = document.getElementById('messages');
const input = document.getElementById('input');
const send = document.getElementById('send');
const refreshBtn = document.getElementById('refresh');
const darkModeToggle = document.getElementById('dark-mode-toggle');

let refreshState = false;

function addMessage(msg, classname, imgSrc) {
    const message = document.createElement('div');
    message.classList.add(classname, 'message');
    const content = document.createElement('div');
    content.classList.add('message-content');
    content.textContent = msg;
    const image = document.createElement('img');
    image.src = imgSrc;
    classname === 'user-msg' ? message.appendChild(content) : message.insertBefore(content, null);
    classname === 'user-msg' ? message.appendChild(image) : message.insertBefore(image, content);
    messages.appendChild(message);
    messages.scrollTop = messages.scrollHeight;
}

function sendMessage() {
    const msg = input.value.trim();
    if (msg) {
        socket.emit('message', {msg: msg, refresh: refreshState});
        addMessage(msg, 'user-msg', userImage);
        input.value = '';
        if (refreshState) {
            refreshState = false;
        }
    }
}


send.addEventListener('click', sendMessage);
input.addEventListener('keypress', (event) => {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

socket.on('response', (msg) => {
    addMessage(msg, 'bot-msg', botImage);
});

refreshBtn.addEventListener('click', () => {
    messages.innerHTML = '';
    refreshState = true;
});

darkModeToggle.addEventListener('change', () => {
    document.documentElement.classList.toggle('dark-mode');
});

const topicsContent = document.getElementById('topics-content');

fetch('/static/topics/video_transcripts.txt')
    .then(response => response.text())
    .then(data => {
        topicsContent.textContent = data;
    });

