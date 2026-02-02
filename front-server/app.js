const cfg = window.__APP_CONFIG__ || { API_URL: "/api", EVENTS_URL: "/events" };

const apiEl = document.getElementById("apiUrl");
if (apiEl) apiEl.textContent = cfg.API_URL;

const eventsEl = document.getElementById("eventsUrl");
if (eventsEl) eventsEl.textContent = cfg.EVENTS_URL;


const out = document.getElementById("output");
const btn = document.getElementById("pingBtn");

btn.addEventListener("click", async () => {
  out.textContent = "Pinging backend...";
  btn.disabled = true;
  try {
    const res = await fetch(cfg.API_URL.replace(/\/$/, "") + "/ping");
    const text = await res.text();
    out.textContent = `✅ Backend replied:\n${text}`;
  } catch (e) {
    out.textContent = `❌ Backend error\n${e.message}`;
  } finally {
    btn.disabled = false;
  }
});

// SSE stream
const gameNumberEl = document.getElementById("gameNumber");
const gameStatusEl = document.getElementById("gameStatus");

const es = new EventSource(cfg.EVENTS_URL);

es.onopen = () => {
  gameStatusEl.textContent = `Game stream: connected ✅ (${cfg.EVENTS_URL})`;
};

es.onmessage = (ev) => {
  gameNumberEl.textContent = ev.data;
};

es.onerror = () => {
  gameStatusEl.textContent = `Game stream: reconnecting 🔁 (${cfg.EVENTS_URL})`;
};
