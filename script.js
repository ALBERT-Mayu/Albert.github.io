document.getElementById("send-button").addEventListener("click", function() {
    const userInput = document.getElementById("user-input");
    const message = userInput.value;
    
    if (message) {
        displayMessage(message, "user");
        userInput.value = "";

        // Simple response logic (could be improved with an API)
        setTimeout(() => {
            let botResponse = "";
            if (message.toLowerCase().includes("weight loss")) {
                botResponse = "Great! For weight loss, I recommend a mix of cardio and strength training.";
            } else if (message.toLowerCase().includes("muscle gain")) {
                botResponse = "Awesome! Focus on strength training and a protein-rich diet.";
            } else {
                botResponse = "I can help with that! What specific exercises or nutrition tips are you interested in?";
            }
            displayMessage(botResponse, "bot");
        }, 1000);
    }
});

function displayMessage(message, sender) {
    const chatBox = document.getElementById("chat-box");
    const messageDiv = document.createElement("div");
    messageDiv.className = "message " + (sender === "bot" ? "bot-message" : "user-message");
    messageDiv.innerText = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to bottom
}
