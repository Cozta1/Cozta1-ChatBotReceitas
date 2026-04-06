const messagesEl  = document.getElementById('messages');
const inputEl     = document.getElementById('user-input');
const sendBtn     = document.getElementById('send-btn');
const emptyState  = document.getElementById('empty-state');

function removeEmptyState() {
  if (emptyState && emptyState.parentNode) {
    emptyState.remove();
  }
}

function scrollToBottom() {
  messagesEl.scrollTo({ top: messagesEl.scrollHeight, behavior: 'smooth' });
}

function formatResponse(text) {
  if (!text) return "";
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
    .replace(/^-{3,}$/gm, '<hr>')
    .replace(/^[-•]\s*(.+)/gm, '<li>$1</li>')
    .replace(/(<li>.*<\/li>)/s, '<ul>$1</ul>')
    .replace(/\n/g, '<br>');
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\n/g, '<br>');
}

function createBubble(type, html) {
  const row    = document.createElement('div');
  row.className = `msg-row ${type}`;

  const avatar  = document.createElement('div');
  avatar.className = `avatar ${type}`;
  avatar.textContent = type === 'bot' ? '🍳' : '👤';

  const bubble  = document.createElement('div');
  bubble.className = `bubble ${type}`;
  bubble.innerHTML = html;

  row.appendChild(avatar);
  row.appendChild(bubble);
  return { row, bubble };
}

function addUserMessage(text) {
  removeEmptyState();
  const { row } = createBubble('user', escapeHtml(text));
  messagesEl.appendChild(row);
  scrollToBottom();
}

function showTypingIndicator() {
  const { row, bubble } = createBubble('bot', '');
  bubble.innerHTML = `
    <div class="typing-dots">
      <span></span><span></span><span></span>
    </div>`;
  bubble.id = 'typing-bubble';
  row.id    = 'typing-row';
  messagesEl.appendChild(row);
  scrollToBottom();
}

function removeTypingIndicator() {
  const el = document.getElementById('typing-row');
  if (el) el.remove();
}

function addBotMessage(text, isError = false) {
  removeTypingIndicator();
  const { row } = createBubble('bot', formatResponse(text));
  if (isError) {
      row.querySelector('.bubble').innerHTML = `<span class="error-text">${formatResponse(text)}</span>`;
  }
  messagesEl.appendChild(row);
  scrollToBottom();
}

async function sendMessage(text) {
  const trimmed = text.trim();
  if (!trimmed) return;

  addUserMessage(trimmed);
  inputEl.value = '';
  autoResize();
  setLoading(true);
  showTypingIndicator();

  try {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ mensagem: trimmed }),
    });

    if (!res.ok) throw new Error(`Erro HTTP: ${res.status}`);

    const data = await res.json();
    addBotMessage(data.resposta || 'Desculpe, não consegui processar sua mensagem.');
  } catch (err) {
    addBotMessage('⚠️ Não foi possível conectar ao servidor. Verifique se o Flask está rodando.', true);
    console.error('[ChefBot] Erro ao enviar mensagem:', err);
  } finally {
    setLoading(false);
  }
}

function setLoading(loading) {
  sendBtn.disabled = loading;
  inputEl.disabled = loading;
  if(loading) {
    inputEl.style.opacity = '0.7';
  } else {
    inputEl.style.opacity = '1';
    inputEl.focus();
  }
}

function sendSuggestion(text) {
  sendBtn.focus();
  inputEl.value = text;
  autoResize();
  setTimeout(() => sendMessage(text), 150);
}

window.sendSuggestion = sendSuggestion;

sendBtn.addEventListener('click', () => sendMessage(inputEl.value));

inputEl.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage(inputEl.value);
  }
});

function autoResize() {
  inputEl.style.height = 'auto';
  inputEl.style.height = Math.min(inputEl.scrollHeight, 120) + 'px';
}

inputEl.addEventListener('input', autoResize);

const suggestionsBar = document.getElementById('suggestions-bar');
const scrollArrowRight = document.getElementById('scroll-arrow-right');
const scrollArrowLeft = document.getElementById('scroll-arrow-left');

if (suggestionsBar && scrollArrowRight && scrollArrowLeft) {
  const updateArrowVisibility = () => {
    const maxScroll = suggestionsBar.scrollWidth - suggestionsBar.clientWidth;
    
    if (maxScroll > 0 && suggestionsBar.scrollLeft < maxScroll - 10) {
      scrollArrowRight.classList.add('visible');
    } else {
      scrollArrowRight.classList.remove('visible');
    }

    if (suggestionsBar.scrollLeft > 10) {
      scrollArrowLeft.classList.add('visible');
    } else {
      scrollArrowLeft.classList.remove('visible');
    }
  };

  updateArrowVisibility();
  window.addEventListener('resize', updateArrowVisibility);
  suggestionsBar.addEventListener('scroll', updateArrowVisibility);

  scrollArrowRight.addEventListener('click', () => {
    suggestionsBar.scrollBy({ left: 250, behavior: 'smooth' });
  });

  scrollArrowLeft.addEventListener('click', () => {
    suggestionsBar.scrollBy({ left: -250, behavior: 'smooth' });
  });
}
