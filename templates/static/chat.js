// Toggle chat visibility
let chatVisible = false;

function toggleChat() {
  const box = document.getElementById('chat-box');
  chatVisible = !chatVisible;
  box.style.display = chatVisible ? 'flex' : 'none';
}

// Handle sending a message
function sendMessage(event) {
  if (event.key === 'Enter') {
    const input = event.target;
    const message = input.value.trim();
    if (message) {
      const chat = document.getElementById('chat-messages');
      const userMsg = document.createElement('div');
      userMsg.textContent = "You: " + message;
      chat.appendChild(userMsg);

      // Simulated assistant reply
      const botMsg = document.createElement('div');
      botMsg.style.color = "green";

      if (message.toLowerCase().includes("price") || message.toLowerCase().includes("cost")) {
        botMsg.textContent = "SB Assistant: All product prices are fixed as listed. No extra charges!";
      } else if (message.toLowerCase().includes("delivery")) {
        botMsg.textContent = "SB Assistant: Delivery is done in 15–20 minutes by our local network.";
      } else if (message.toLowerCase().includes("vendor") || message.toLowerCase().includes("map")) {
        botMsg.textContent = "SB Assistant: You can view vendors on the 🗺 Vendor Map.";
      } else {
        botMsg.textContent = "SB Assistant: Thanks for reaching out! We'll help you with any queries.";
      }

      chat.appendChild(botMsg);
      input.value = "";
      chat.scrollTop = chat.scrollHeight;
    }
  }
}
