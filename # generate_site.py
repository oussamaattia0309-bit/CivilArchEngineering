# generate_site.py

html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>CivilArchEngineering – Construction & Engineering Excellence</title>
  <meta name="description" content="CivilArchEngineering - Experts in civil engineering, architectural design, structural projects and construction services in Tunisia and beyond.">
  
  <style>
    :root {{
      --primary: #1a3c6e;
      --primary-dark: #132d54;
      --accent: #e67e22;
      --light: #f8f9fa;
      --dark: #222;
      --gray: #6c757d;
    }}

    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}

    body {{
      font-family: 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      line-height: 1.6;
      color: #333;
      background-color: #fff;
    }}

    .container {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 0 20px;
    }}

    /* ─── Header & Nav ─── */
    header {{
      background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%);
      color: white;
      position: fixed;
      width: 100%;
      top: 0;
      z-index: 1000;
      box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }}

    nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1.1rem 0;
    }}

    .logo {{
      font-size: 1.7rem;
      font-weight: 800;
      letter-spacing: 1px;
    }}

    .logo span {{
      color: var(--accent);
    }}

    .nav-links {{
      display: flex;
      gap: 2.2rem;
      list-style: none;
    }}

    .nav-links a {{
      color: white;
      text-decoration: none;
      font-weight: 500;
      transition: 0.3s;
      position: relative;
    }}

    .nav-links a:hover,
    .nav-links a.active {{
      color: var(--accent);
    }}

    .nav-links a::after {{
      content: '';
      position: absolute;
      width: 0;
      height: 2px;
      bottom: -6px;
      left: 0;
      background-color: var(--accent);
      transition: width 0.3s ease;
    }}

    .nav-links a:hover::after,
    .nav-links a.active::after {{
      width: 100%;
    }}

    /* Hero and other styles... (truncated for brevity - copy full CSS from original) */

    /* ... paste the rest of the <style> content here ... */

  </style>
</head>
<body>

  <header>
    <div class="container">
      <nav>
        <div class="logo">Civil<span>Arch</span>Engineering</div>
        <ul class="nav-links">
          <li><a href="#hero" class="active">Home</a></li>
          <li><a href="#about">About</a></li>
          <li><a href="#projects">Projects</a></li>
          <li><a href="#services">Services</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Hero section -->
  <section id="hero">
    <div class="container hero-content">
      <h1>Building the Future with Precision & Vision</h1>
      <h2>Civil Engineering • Architecture • Construction Management</h2>
      <a href="#contact" class="btn">Get in Touch</a>
    </div>
  </section>

  <!-- About, Projects, Services, Contact sections... -->
  <!-- Paste the rest of the <body> content from the original HTML here -->

</body>
</html>
"""

# Write to file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("index.html has been generated!")