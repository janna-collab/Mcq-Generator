// Helper to get CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let cookie of cookies) {
          cookie = cookie.trim();
          if (cookie.startsWith(name + "=")) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

// Log the CSRF token for debugging
const csrfToken = getCookie("csrftoken");
console.log("CSRF Token:", csrfToken);

document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("mcq-form");
  const resultsDiv = document.getElementById("mcq-results");

  form.addEventListener("submit", function(e) {
      e.preventDefault();
      const text = document.getElementById("textInput").value;
      const mcqCount = document.getElementById("mcqCount").value;

      const formData = new URLSearchParams();
      formData.append("text", text);
      formData.append("mcqCount", mcqCount);

      fetch("/generate/", {
          method: "POST",
          body: formData,
          headers: {
              "Content-Type": "application/x-www-form-urlencoded",
              "X-CSRFToken": getCookie("csrftoken")
          }
      })
      .then(response => {
          console.log("Raw response:", response);
          return response.json();
      })
      .then(data => {
          console.log("Data received:", data);
          if (data.error) {
              resultsDiv.innerHTML = `<p>Error: ${data.error}</p>`;
          } else {
              displayMCQs(data.mcqs);
          }
      })
      .catch(error => {
          console.error("Fetch error:", error);
          resultsDiv.innerHTML = `<p>Error: ${error}</p>`;
      });
  });

  function displayMCQs(mcqs) {
      resultsDiv.innerHTML = "";
      mcqs.forEach((mcq, index) => {
          const card = document.createElement("div");
          card.className = "mcq-card";
          card.innerHTML = `
              <h3>Question ${index+1}:</h3>
              <p>${mcq.question}</p>
              <ul>
                  ${mcq.options.map(option => `<li>${option}</li>`).join("")}
              </ul>
              <p><strong>Answer:</strong> ${mcq.answer}</p>
              <p><strong>Explanation:</strong> ${mcq.explanation}</p>
          `;
          resultsDiv.appendChild(card);
      });
  }
});
