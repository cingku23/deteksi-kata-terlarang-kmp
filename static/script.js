let currentUser = "Syaikha";
let chats = { Syaikha: [], Azkadina: [] };

function switchUser(name) {
    currentUser = name;
    document.getElementById("currentUser").innerText = name;

    document.querySelectorAll(".user").forEach(u => u.classList.remove("active"));
    event.target.classList.add("active");

    render();
}

function render() {
    const box = document.getElementById("messages");
    box.innerHTML = "";
    chats[currentUser].forEach(m => box.appendChild(m));
}

async function send() {
    const input = document.getElementById("input");
    const text = input.value;
    if (!text) return;

    document.getElementById("status").innerText = "Memeriksa...";

    const res = await fetch("/cek", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ text })
    });

    const data = await res.json();

    const msg = document.createElement("div");
    msg.classList.add("msg");

    if (data.blocked) {
        msg.classList.add("blocked");
        msg.innerText = "❌ DITOLAK\nKata: " + data.kata.join(", ");
        document.getElementById("status").innerText = "Pesan ditolak";
    } else {
        msg.classList.add("allowed");
        msg.innerText = text;
        document.getElementById("status").innerText = "Pesan aman";
    }

    chats[currentUser].push(msg);
    render();
    input.value = "";
}
