// ============================================================
// PORTFOLIO INTERACTIONS
// ============================================================

document.addEventListener("DOMContentLoaded", () => {
  typeTerminal();
  setupScrollReveal();
  setupNavHighlight();
});

/* ---------- Terminal typing effect ---------- */
function typeTerminal() {
  const el = document.getElementById("terminal-body");
  if (!el) return;

  const lines = JSON.parse(el.dataset.lines || "[]");
  el.innerHTML = "";

  let lineIndex = 0;
  let charIndex = 0;

  function typeNextChar() {
    if (lineIndex >= lines.length) {
      // blinking cursor at the end, no more typing
      const cursor = document.createElement("span");
      cursor.className = "cursor";
      el.appendChild(cursor);
      return;
    }

    const fullLine = lines[lineIndex];
    const isCommand = !fullLine.startsWith(">");

    let currentLineEl = el.querySelector(`[data-line="${lineIndex}"]`);
    if (!currentLineEl) {
      currentLineEl = document.createElement("div");
      currentLineEl.className = "line";
      currentLineEl.dataset.line = lineIndex;
      if (isCommand) {
        currentLineEl.innerHTML = '<span class="prompt-sym">$ </span><span class="txt"></span>';
      } else {
        currentLineEl.innerHTML = '<span class="output txt"></span>';
      }
      el.appendChild(currentLineEl);
    }

    const txtSpan = currentLineEl.querySelector(".txt");
    txtSpan.textContent = fullLine.replace(/^>\s?/, "").slice(0, charIndex + 1);

    charIndex++;

    if (charIndex >= fullLine.replace(/^>\s?/, "").length) {
      lineIndex++;
      charIndex = 0;
      setTimeout(typeNextChar, isCommand ? 380 : 220);
    } else {
      setTimeout(typeNextChar, isCommand ? 38 : 14);
    }
  }

  typeNextChar();
}

/* ---------- Scroll reveal ---------- */
function setupScrollReveal() {
  const items = document.querySelectorAll(".reveal");
  if (!("IntersectionObserver" in window) || items.length === 0) {
    items.forEach((i) => i.classList.add("in"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("in");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );

  items.forEach((item) => observer.observe(item));
}

/* ---------- Nav active-link highlight ---------- */
function setupNavHighlight() {
  const links = document.querySelectorAll(".nav-links a");
  const sections = Array.from(links)
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);

  if (sections.length === 0) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        const id = "#" + entry.target.id;
        const link = document.querySelector(`.nav-links a[href="${id}"]`);
        if (!link) return;
        if (entry.isIntersecting) {
          links.forEach((l) => l.classList.remove("active"));
          link.classList.add("active");
        }
      });
    },
    { rootMargin: "-40% 0px -50% 0px", threshold: 0 }
  );

  sections.forEach((s) => observer.observe(s));
}
