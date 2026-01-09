function checkSpam() {
    const email = document.getElementById("emailText").value;
    const result = document.getElementById("result");

    if (email.trim() === "") {
        result.innerText = "Please enter some text.";
        result.className = "result";
        result.style.color = "red";
        return;
    }
    result.innerText = "Checking...";
    result.className = "result loading";

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ email: email })
    })
    .then(response => response.json())
    .then(data => {
        if (data.result === "Spam") {
            result.innerText = "🚨 SPAM";
            result.className = "result spam";
        } 
        else if (data.result === "Potential Scam") {
    result.innerText = "⚠️ POTENTIAL JOB SCAM – BE CAUTIOUS";
    result.className = "result warning";
}
        else {
            result.innerText = "✅ Safe";
            result.className = "result safe";
            result.style.color ="";
        }
    })
    .catch(error => {
        result.innerText = "Error connecting to server";
        result.className = "result";
        result.style.color = "red";
    });
}
function resetForm() {
    document.getElementById("emailText").value = "";
    const result = document.getElementById("result");
    result.innerText = "";
    result.className = "result";
    result.style.color = "";
}
