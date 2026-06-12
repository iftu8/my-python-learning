<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Iftu's Codebase | Future Tech</title>
    <style>
        /* === Modern, Non-Hacker Aesthetic === */
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Rajdhani:wght@400;600&display=swap');

        :root {
            --bg-color: #050510;
            --surface: #0f111a;
            --primary: #00d2ff;
            --secondary: #3a7bd5;
            --text-main: #e0e6ed;
            --text-muted: #8c9baf;
        }

        body {
            margin: 0;
            padding: 0;
            font-family: 'Rajdhani', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            overflow-x: hidden;
        }

        /* === Beautiful Animated Logo Section === */
        .hero {
            text-align: center;
            padding: 80px 20px 40px;
            background: radial-gradient(circle at top, rgba(0, 210, 255, 0.15), transparent 60%);
        }

        .animated-logo {
            font-family: 'Orbitron', sans-serif;
            font-size: 4.5rem;
            font-weight: 700;
            background: linear-gradient(90deg, #00d2ff, #3a7bd5, #00d2ff);
            background-size: 200% auto;
            color: transparent;
            -webkit-background-clip: text;
            background-clip: text;
            animation: gradientShine 4s linear infinite;
            margin-bottom: 10px;
        }

        @keyframes gradientShine {
            0% { background-position: 0% center; }
            100% { background-position: 200% center; }
        }

        .subtitle {
            font-size: 1.5rem;
            color: var(--text-muted);
            letter-spacing: 2px;
        }

        /* === Contact & Badges === */
        .badges {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 30px 0;
            flex-wrap: wrap;
        }

        .contact-btn {
            display: inline-flex;
            align-items: center;
            padding: 10px 20px;
            background: linear-gradient(135deg, rgba(0, 210, 255, 0.1), rgba(58, 123, 213, 0.1));
            border: 1px solid rgba(0, 210, 255, 0.3);
            border-radius: 30px;
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
            font-family: 'Orbitron', sans-serif;
            transition: all 0.3s ease;
        }

        .contact-btn:hover {
            background: var(--primary);
            color: #000;
            box-shadow: 0 0 20px rgba(0, 210, 255, 0.5);
            transform: translateY(-2px);
        }

        /* === Future Tokyo Gallery (No Humans) === */
        .section-title {
            text-align: center;
            font-family: 'Orbitron', sans-serif;
            font-size: 2rem;
            margin: 60px 0 30px;
            color: var(--primary);
        }

        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            padding: 0 5%;
        }

        .gallery img {
            width: 100%;
            height: 250px;
            object-fit: cover;
            border-radius: 12px;
            filter: brightness(0.8) contrast(1.2);
            transition: all 0.4s ease;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        }

        .gallery img:hover {
            filter: brightness(1.1) contrast(1.3);
            transform: scale(1.03);
            box-shadow: 0 15px 40px rgba(0, 210, 255, 0.3);
        }

        /* === Projects & Large Code Section === */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }

        .card {
            background: var(--surface);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 30px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }

        .code-window {
            background: #0d1117;
            border-radius: 10px;
            padding: 20px;
            overflow-x: auto;
            border: 1px solid #30363d;
        }

        pre {
            margin: 0;
            font-family: 'Courier New', Courier, monospace;
            font-size: 14px;
            color: #c9d1d9;
            line-height: 1.6;
        }

        .keyword { color: #ff7b72; }
        .function { color: #d2a8ff; }
        .string { color: #a5d6ff; }
        .comment { color: #8b949e; }
    </style>
</head>
<body>

    <header class="hero">
        <div class="animated-logo">Welcome to My Codebase! 🚀</div>
        <div class="subtitle">Python Developer | Web Enthusiast | Automation Expert</div>
        <p style="margin-top: 20px; color: var(--text-muted); font-size: 1.2rem;">Hello! I am <strong>Iftu</strong>. Welcome to my curated collection of advanced scripts and interfaces.</p>
        
        <div class="badges">
            <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
            <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML5">
            <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS3">
            <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JS">
        </div>

        <div class="badges">
            <a href="mailto:iftekharc78@gmail.com" class="contact-btn">✉️ iftekharc78@gmail.com</a>
            <a href="https://linkedin.com/in/YOUR_LINKEDIN_PROFILE" class="contact-btn">🔗 LinkedIn Profile</a>
        </div>
    </header>

    <h2 class="section-title">Visions of the Future</h2>
    <div class="gallery">
        <img src="https://images.unsplash.com/photo-1540959733332-eab4deabeeaf?auto=format&fit=crop&w=1000&q=80" alt="Future Tokyo Skyline Night">
        <img src="https://images.unsplash.com/photo-1536098561742-ca998e48cbcc?auto=format&fit=crop&w=1000&q=80" alt="Neon Architecture">
        <img src="https://images.unsplash.com/photo-1580838154564-9d554a9916ab?auto=format&fit=crop&w=1000&q=80" alt="Abstract Futuristic Cityscape">
        <img src="https://images.unsplash.com/photo-1601042879364-f3947d3f9c16?auto=format&fit=crop&w=1000&q=80" alt="Cyberpunk Empty Streets">
    </div>

    <div class="container">
        <h2 class="section-title">📂 Project Categories</h2>
        
        <div class="card">
            <h3 style="color: var(--primary);">🔒 Cybersecurity & Cryptography</h3>
            <p><strong>`password_shield.py`</strong> - Advanced password generation and secure vault tools.<br>
            <strong>`log_security_analyzer.py`</strong> - Automated log analysis for threat detection.</p>
            
            <h3 style="color: var(--primary);">⚙️ Automation & Web Scraping</h3>
            <p><strong>`weather_tracker.py`</strong> - Real-time weather data fetching.<br>
            <strong>`news_fetcher.py`</strong> - Automated news scraping and aggregation.</p>
        </div>

        <h2 class="section-title">💻 Featured Deep-Tech Code</h2>
        <div class="card">
            <p style="color: var(--text-muted); margin-bottom: 20px;">An extensive demonstration of my asynchronous Python architecture capabilities.</p>
            <div class="code-window">
<pre>
<span class="comment"># advanced_network_analyzer.py</span>
<span class="keyword">import</span> asyncio
<span class="keyword">import</span> aiohttp
<span class="keyword">import</span> ssl
<span class="keyword">import</span> time
<span class="keyword">import</span> logging
<span class="keyword">from</span> typing <span class="keyword">import</span> List, Dict

<span class="comment"># Configure advanced logging for system analytics</span>
logging.basicConfig(level=logging.INFO, format=<span class="string">'%(asctime)s - %(levelname)s - %(message)s'</span>)

<span class="keyword">class</span> <span class="function">FutureNetworkAnalyzer</span>:
    <span class="keyword">def</span> <span class="function">__init__</span>(self, target_urls: List[str], concurrency_limit: int = <span class="string">50</span>):
        self.target_urls = target_urls
        self.semaphore = asyncio.Semaphore(concurrency_limit)
        self.results: Dict[str, dict] = {}
        <span class="comment"># Bypassing strict SSL for massive parallel scraping</span>
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = <span class="keyword">False</span>
        self.ssl_context.verify_mode = ssl.CERT_NONE

    <span class="keyword">async def</span> <span class="function">fetch_data</span>(self, session: aiohttp.ClientSession, url: str) -> <span class="keyword">None</span>:
        <span class="keyword">async with</span> self.semaphore:
            start_time = time.time()
            <span class="keyword">try</span>:
                <span class="keyword">async with</span> session.get(url, ssl=self.ssl_context, timeout=<span class="string">10</span>) <span class="keyword">as</span> response:
                    content_length = len(<span class="keyword">await</span> response.read())
                    elapsed = time.time() - start_time
                    self.results[url] = {
                        <span class="string">'status'</span>: response.status,
                        <span class="string">'size_bytes'</span>: content_length,
                        <span class="string">'latency_sec'</span>: round(elapsed, <span class="string">4</span>)
                    }
                    logging.info(<span class="string">f"Successfully analyzed {url} in {elapsed:.2f}s"</span>)
            <span class="keyword">except</span> Exception <span class="keyword">as</span> e:
                self.results[url] = {<span class="string">'error'</span>: str(e)}
                logging.error(<span class="string">f"Failed to analyze {url}: {e}"</span>)

    <span class="keyword">async def</span> <span class="function">execute_scan</span>(self):
        logging.info(<span class="string">f"Initiating high-concurrency scan on {len(self.target_urls)} targets..."</span>)
        <span class="keyword">async with</span> aiohttp.ClientSession() <span class="keyword">as</span> session:
            tasks = [self.fetch_data(session, url) <span class="keyword">for</span> url <span class="keyword">in</span> self.target_urls]
            <span class="keyword">await</span> asyncio.gather(*tasks)

    <span class="keyword">def</span> <span class="function">generate_report</span>(self):
        logging.info(<span class="string">"=== FINAL ANALYSIS REPORT ==="</span>)
        successful = sum(<span class="string">1</span> <span class="keyword">for</span> r <span class="keyword">in</span> self.results.values() <span class="keyword">if</span> <span class="string">'status'</span> <span class="keyword">in</span> r)
        logging.info(<span class="string">f"Total Analyzed: {len(self.results)} | Successful: {successful}"</span>)
        <span class="keyword">for</span> url, data <span class="keyword">in</span> self.results.items():
            <span class="keyword">print</span>(<span class="string">f"{url} -> {data}"</span>)

<span class="keyword">if</span> __name__ == <span class="string">'__main__'</span>:
    <span class="comment"># Simulating a massive array of system nodes</span>
    nodes = [<span class="string">f"https://api.example.com/node/{i}"</span> <span class="keyword">for</span> i <span class="keyword">in</span> range(<span class="string">1</span>, <span class="string">101</span>)]
    analyzer = FutureNetworkAnalyzer(target_urls=nodes, concurrency_limit=<span class="string">20</span>)
    
    start_execution = time.time()
    asyncio.run(analyzer.execute_scan())
    analyzer.generate_report()
    logging.info(<span class="string">f"Total Execution Time: {time.time() - start_execution:.2f} seconds."</span>)
</pre>
            </div>
        </div>
        
        <h2 class="section-title">💻 How to Run Locally</h2>
        <div class="card" style="text-align: center;">
            <p>Clone the repository using the command below:</p>
            <div class="code-window" style="display: inline-block; text-align: left;">
                <pre><span class="keyword">git</span> clone https://github.com/iftu8/my-python-learning.git</pre>
            </div>
        </div>
    </div>

</body>
</html>
