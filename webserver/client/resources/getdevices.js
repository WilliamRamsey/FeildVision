async function getDevices() {
    const response = await fetch("http://127.0.0.1:5000/api/devices");
    const jsonData = await response.json();
    console.log(jsonData['device_id']);
    document.getElementById('display-id').innerHTML = jsonData['device_id']
  }
