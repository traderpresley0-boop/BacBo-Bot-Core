fetch('http://127.0.0.1:5000/status')
.then(response => response.json())
.then(data => {
    document.getElementById('status').innerText = data.status;
})
.catch(error => console.log('Erro:', error));
