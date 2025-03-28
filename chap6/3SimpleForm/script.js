function submitName() {
  const username = document.getElementById('username').value;
    console.log(username);

  fetch('/submit', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username })
  })
    .then(response => response.text())
    .then(responseText => {
      const welcomeMessage = document.createElement('p');
      welcomeMessage.textContent = responseText;
      document.body.appendChild(welcomeMessage);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}



