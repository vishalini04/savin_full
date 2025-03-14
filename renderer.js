// renderer.js - Handles UI interactions and API communication

const { ipcRenderer } = require('electron');

// DOM Elements
const micButton = document.getElementById('mic-btn');
const responseText = document.getElementById('response-text');
const assistantContainer = document.querySelector('.assistant-container');
const minimizeBtn = document.getElementById('minimize-btn');
const closeBtn = document.getElementById('close-btn');

// Backend API configuration
const API_BASE_URL = 'http://localhost:5000'; // Change this to your Flask server address

// Speech recognition setup
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
let recognition;
let isListening = false;

function initSpeechRecognition() {
  if (!SpeechRecognition) {
    responseText.textContent = "Speech recognition is not supported in this browser/environment.";
    return false;
  }

  recognition = new SpeechRecognition();
  recognition.continuous = false;
  recognition.interimResults = false;
  recognition.lang = 'en-US';

  recognition.onstart = () => {
    isListening = true;
    assistantContainer.classList.add('listening');
    responseText.textContent = "Listening...";
  };

  recognition.onresult = (event) => {
    const transcript = event.results[0][0].transcript;
    responseText.textContent = `I heard: "${transcript}"`;
    sendCommandToBackend(transcript);
  };

  recognition.onerror = (event) => {
    console.error("Speech recognition error", event.error);
    responseText.textContent = event.error === 'no-speech' ? "I didn't hear anything. Please try again." : `Error: ${event.error}`;
    stopListening();
  };

  recognition.onend = stopListening;
  return true;
}

// Window control handlers
minimizeBtn.addEventListener('click', () => ipcRenderer.send('minimize-window'));
closeBtn.addEventListener('click', () => ipcRenderer.send('close-window'));

// Microphone button handler
micButton.addEventListener('click', () => isListening ? stopListening() : startListening());

function startListening() {
  if (!recognition && !initSpeechRecognition()) return;
  try {
    recognition.start();
  } catch (error) {
    console.error("Error starting speech recognition:", error);
    responseText.textContent = "Could not start listening. Please try again.";
  }
}

function stopListening() {
  if (recognition) recognition.stop();
  isListening = false;
  assistantContainer.classList.remove('listening');
}

async function sendCommand(command) {
  console.log("Sending command:", command); // Debug log
  try {
      const response = await fetch("http://127.0.0.1:5000/savin", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ command: command })
      });

      const data = await response.json();
      console.log("Response from backend:", data); // Debug log

      document.getElementById("response").innerText = data.message; // Show response in UI
  } catch (error) {
      console.error("Error communicating with backend:", error);
  }
}

// Attach event listener
document.getElementById("submitBtn").addEventListener("click", () => {
  const userCommand = document.getElementById("commandInput").value;
  sendCommand(userCommand);
});

function speakResponse(text) {
  if ('speechSynthesis' in window) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.rate = 1.0;
    utterance.pitch = 1.0;
    window.speechSynthesis.speak(utterance);
  }
}

// Enable window dragging
let isDragging = false;
let initialX, initialY;

document.addEventListener('mousedown', (e) => {
  if (!e.target.closest('.mic-button') && !e.target.closest('.window-controls')) {
    isDragging = true;
    initialX = e.clientX;
    initialY = e.clientY;
  }
});

document.addEventListener('mousemove', (e) => {
  if (isDragging) {
    const window = require('@electron/remote').getCurrentWindow();
    const [posX, posY] = window.getPosition();
    window.setPosition(posX + (e.clientX - initialX), posY + (e.clientY - initialY));
    initialX = e.clientX;
    initialY = e.clientY;
  }
});

document.addEventListener('mouseup', () => isDragging = false);

// Check connection to backend on startup
document.addEventListener('DOMContentLoaded', async () => {
  initSpeechRecognition();
  try {
    const response = await fetch(`${API_BASE_URL}/health_check`);
    responseText.textContent = response.ok ? "Hello! I'm your AI assistant. Click the microphone to speak." : "Warning: Backend server is not responding correctly.";
  } catch {
    responseText.textContent = "Cannot connect to backend server. Some features may be unavailable.";
  }
});
const axios = require('axios');

async function sendCommand(command) {
    try {
        const response = await axios.post("http://127.0.0.1:5000/savin", {
            command: command
        });
        console.log(response.data);
    } catch (error) {
        console.error("Error:", error);
    }
}

// Example: Send "open YouTube" when a button is clicked
document.getElementById("sendButton").addEventListener("click", () => {
    sendCommand("open YouTube");
});

