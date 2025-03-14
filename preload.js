// preload.js
window.addEventListener('DOMContentLoaded', () => {
    // Any preload scripts can go here
    console.log('Preload script loaded');
    
    // You can expose custom APIs to the renderer process here if needed
    // For example, if you want to implement actual speech recognition:
    /*
    const { ipcRenderer } = require('electron');
    
    window.speechRecognition = {
      start: () => {
        // Implement speech recognition start
      },
      stop: () => {
        // Implement speech recognition stop
      }
    };
    */
  });