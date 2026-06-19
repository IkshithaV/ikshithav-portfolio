"""
============================================================
 PORTFOLIO GENERATOR
============================================================
Reads data.py and generates index.html.

Usage:
    python generate.py

Re-run this any time you edit data.py to rebuild the site.
============================================================
"""

import json
from data import (
    PROFILE,
    TERMINAL_LINES,
    EDUCATION,
    EXPERIENCE,
    PROJECTS,
    CERTIFICATIONS,
    SKILLS,
)


def esc(text: str) -> str:
    """Minimal HTML escaping for safety when injecting text content."""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def render_nav() -> str:
    items = [
        ("#about", "about"),
        ("#education", "education"),
        ("#experience", "experience"),
        ("#projects", "projects"),
        ("#skills", "skills"),
        ("#certifications", "certs"),
        ("#contact", "contact"),
    ]
    links = "\n".join(
        f'<li><a href="{href}">{label}</a></li>' for href, label in items
    )
    initials = "".join(w[0] for w in PROFILE["name"].split()[:2]).upper()
    return f"""
    <nav>
      <div class="wrap">
        <div class="nav-logo">~/{esc(initials.lower())}<span class="blink">_</span></div>
        <ul class="nav-links">
          {links}
        </ul>
      </div>
    </nav>
    """


def render_hero() -> str:
    lines_json = esc(json.dumps(TERMINAL_LINES)).replace('"', "&quot;")
    return f"""
    <header class="hero">
      <div class="wrap">
        <div class="eyebrow">SYSTEM ONLINE</div>
        <h1>{esc(PROFILE['name'])}</h1>
        <p class="role">{esc(PROFILE['role'])} — {esc(PROFILE['tagline'])}</p>

        <div class="terminal">
          <div class="terminal-bar">
            <span class="terminal-dot"></span>
            <span class="terminal-dot"></span>
            <span class="terminal-dot"></span>
            <span class="terminal-title">guest@portfolio: ~</span>
          </div>
          <div class="terminal-body" id="terminal-body" data-lines="{lines_json}"></div>
        </div>

        <div class="hero-cta">
          <a class="btn btn-primary" href="#projects">View projects</a>
          <a class="btn btn-ghost" href="#contact">Get in touch</a>
        </div>
      </div>
    </header>
    """


def render_about() -> str:
    info = [
        ("location", PROFILE["location"]),
        ("email", PROFILE["email"]),
        ("phone", PROFILE["phone"]),
        ("focus", "AI / ML / Security"),
    ]
    info_html = "\n".join(
        f"""<div class="info-item"><div class="k">{esc(k)}</div><div class="v">{esc(v)}</div></div>"""
        for k, v in info
    )
    return f"""
    <section id="about">
      <div class="wrap">
        <div class="section-label"><span class="sym">$</span> cat about.md</div>
        <h2 class="section-title">About</h2>
        <p class="about-text reveal">{esc(PROFILE['summary'])}</p>
        <div class="info-grid reveal">
          {info_html}
        </div>
      </div>
    </section>
    """


def render_education() -> str:
    cards = ""
    for ed in EDUCATION:
        cards += f"""
        <div class="card reveal">
          <div class="card-head">
            <div class="card-title">{esc(ed['degree'])}</div>
            <div class="card-period">{esc(ed['period'])}</div>
          </div>
          <div class="card-org">{esc(ed['school'])}</div>
          <span class="score-pill">{esc(ed['score'])}</span>
        </div>
        """
    return f"""
    <section id="education">
      <div class="wrap">
        <div class="section-label"><span class="sym">$</span> cat education.log</div>
        <h2 class="section-title">Education</h2>
        {cards}
      </div>
    </section>
    """


def render_experience() -> str:
    cards = ""
    for exp in EXPERIENCE:
        points = "\n".join(f"<li>{esc(p)}</li>" for p in exp["points"])
        cards += f"""
        <div class="card reveal">
          <div class="card-head">
            <div class="card-title">{esc(exp['title'])}</div>
            <div class="card-period">{esc(exp['period'])}</div>
          </div>
          <div class="card-org">{esc(exp['org'])}</div>
          <ul>{points}</ul>
        </div>
        """
    return f"""
    <section id="experience">
      <div class="wrap">
        <div class="section-label"><span class="sym">$</span> grep -r "experience" ./career</div>
        <h2 class="section-title">Experience</h2>
        {cards}
      </div>
    </section>
    """


def render_projects() -> str:
    cards = ""
    for proj in PROJECTS:
        tags = "\n".join(f'<span class="tech-tag">{esc(t)}</span>' for t in proj["tech"])
        points = "\n".join(f"<li>{esc(p)}</li>" for p in proj["points"])
        link_html = ""
        if proj.get("link"):
            link_html = f'<a class="project-link" href="{esc(proj["link"])}" target="_blank" rel="noopener">view_project →</a>'
        cards += f"""
        <div class="project-card reveal">
          <div class="project-name">{esc(proj['name'])}</div>
          <div class="tech-row">{tags}</div>
          <ul>{points}</ul>
          {link_html}
        </div>
        """
    return f"""
    <section id="projects">
      <div class="wrap">
        <div class="section-label"><span class="sym">$</span> cat projects.log</div>
        <h2 class="section-title">Projects</h2>
        {cards}
      </div>
    </section>
    """


def render_skills() -> str:
    groups = ""
    for category, items in SKILLS.items():
        chips = "\n".join(f'<span class="chip">{esc(i)}</span>' for i in items)
        groups += f"""
        <div class="skill-group reveal">
          <div class="k">{esc(category)}</div>
          <div class="chip-row">{chips}</div>
        </div>
        """
    return f"""
    <section id="skills">
      <div class="wrap">
        <div class="section-label"><span class="sym">$</span> pip list --installed</div>
        <h2 class="section-title">Skills</h2>
        <div class="skills-grid">{groups}</div>
      </div>
    </section>
    """


def render_certifications() -> str:
    items = "\n".join(
        f'<div class="cert-item reveal">{esc(c)}</div>' for c in CERTIFICATIONS
    )
    return f"""
    <section id="certifications">
      <div class="wrap">
        <div class="section-label"><span class="sym">$</span> ls ./certifications</div>
        <h2 class="section-title">Certifications</h2>
        <div class="cert-list">{items}</div>
      </div>
    </section>
    """


def render_contact() -> str:
    return f"""
    <section id="contact" class="contact-section">
      <div class="wrap">
        <div class="section-label"><span class="sym">$</span> ./connect.sh</div>
        <h2 class="section-title">Let's connect</h2>
        <p>Open to internships and opportunities in AI, machine learning, and cybersecurity. Reach out below.</p>
        <div class="contact-links">
          <a class="btn btn-primary" href="mailto:{esc(PROFILE['email'])}">Email me</a>
          <a class="btn btn-ghost" href="{esc(PROFILE['github'])}" target="_blank" rel="noopener">GitHub</a>
          <a class="btn btn-ghost" href="{esc(PROFILE['linkedin'])}" target="_blank" rel="noopener">LinkedIn</a>
        </div>
      </div>
    </section>
    """


def render_footer() -> str:
    return f"""
    <footer>
      <div class="wrap">
        built with python + html + css · © {esc(PROFILE['name'])}
      </div>
    </footer>
    """


def build_html() -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{esc(PROFILE['name'])} — {esc(PROFILE['role'])}</title>
<meta name="description" content="{esc(PROFILE['summary'][:150])}" />
<link rel="stylesheet" href="style.css" />
</head>
<body>
{render_nav()}
{render_hero()}
<main>
{render_about()}
{render_education()}
{render_experience()}
{render_projects()}
{render_skills()}
{render_certifications()}
{render_contact()}
</main>
{render_footer()}
<script src="script.js"></script>
</body>
</html>
"""


def main():
    html = build_html()
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("✓ index.html generated successfully.")
    print("  Open it in your browser, or run a local server:")
    print("  python -m http.server 8000")


if __name__ == "__main__":
    main()
