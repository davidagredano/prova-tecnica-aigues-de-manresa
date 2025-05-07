const messageElement = document.getElementById("mqtt-message");

async function getMessage() {
  const url = "/api/mqtt";
  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }

    const json = await response.json();
    messageElement.textContent = json.value;
  } catch (error) {
    console.error(error.message);
  }
}

getMessage();

setInterval(getMessage, 1000);
