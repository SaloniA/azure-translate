async function translateText() {
    url = "https://saloni-2.azurewebsites.net/translate";
    // url = "http://localhost:5000/translate";
    data = {
        to_translate: document.getElementById("to_translate").value,
        language: document.getElementById("language").value,
    };
    const response = await fetch(url, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
          'Content-Type': 'application/json'
        }
      });
      result = await response.json();
      translation = result[0].translations[0].text;
      document.getElementById("translated").value = translation;
}