import os

# --- KONFIGURASI ---
DOMAIN_NAME = "cekpeluangsnbp.web.id" # Ganti dengan domainmu
SITE_NAME = "Cek Peluang SNBP 2026"
EMAIL_CONTACT = "admin@" + DOMAIN_NAME
OUTPUT_DIR = "output"

def create_page(filename, title, content):
    html = f"""
    <!DOCTYPE html>
    <html lang="id">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title} - {SITE_NAME}</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@picocss/pico@1/css/pico.min.css">
        <style> .container {{ max-width: 800px; margin-top: 2rem; }} </style>
        
        <!-- Google tag (gtag.js) -->
        <script async src="https://www.googletagmanager.com/gtag/js?id=G-HTQRSG37TV"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){{dataLayer.push(arguments);}}
            gtag('js', new Date());

            gtag('config', 'G-HTQRSG37TV');
        </script>
        <meta name="google-site-verification" content="8LoOmKJcFqUGEb_NZnxpiaBxitt85K6HDBV7W3arKII" />
    </head>
    <body>
        <main class="container">
            <nav>
                <ul>
                    <li><strong><a href="index.html">{SITE_NAME}</a></strong></li>
                </ul>
                <ul>
                    <li><a href="about.html">About</a></li>
                    <li><a href="privacy.html">Privacy</a></li>
                    <li><a href="disclaimer.html">Disclaimer</a></li>
                </ul>
            </nav>
            <h1>{title}</h1>
            <hr>
            {content}
            <footer style="margin-top:3rem; text-align:center;">
                <small>&copy; 2026 {SITE_NAME}. All rights reserved.</small>
            </footer>
        </main>
    </body>
    </html>
    """
    with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[OK] {filename} berhasil dibuat.")

def main():
    # 1. ABOUT US
    about_text = f"""
    <p>Selamat datang di <strong>{SITE_NAME}</strong>.</p>
    <p>Kami adalah platform data independen yang menyajikan analisis statistik penerimaan mahasiswa baru jalur SNBP (Seleksi Nasional Berdasarkan Prestasi) di Indonesia.</p>
    <p>Tujuan kami adalah membantu calon mahasiswa melihat data historis daya tampung dan peminat agar dapat menyusun strategi pemilihan jurusan yang lebih rasional dan berbasis data.</p>
    <p>Data yang kami sajikan bersumber dari publikasi resmi panitia seleksi nasional dan universitas terkait yang diolah kembali untuk kemudahan akses.</p>
    """
    create_page("about.html", "Tentang Kami", about_text)

    # 2. PRIVACY POLICY (Standard AdSense Requirement)
    privacy_text = f"""
    <p>Di {SITE_NAME}, privasi pengunjung adalah prioritas kami.</p>
    <h3>Log Files</h3>
    <p>{SITE_NAME} menggunakan file log standar untuk mencatat pengunjung ketika mereka mengunjungi situs web. Informasi ini digunakan untuk menganalisis tren dan mengelola situs.</p>
    <h3>Cookies</h3>
    <p>Seperti situs web lainnya, {SITE_NAME} menggunakan 'cookies' untuk menyimpan informasi seperti preferensi pengunjung dan halaman yang diakses.</p>
    <h3>Google DoubleClick DART Cookie</h3>
    <p>Google adalah vendor pihak ketiga di situs kami. Google juga menggunakan cookie, yang dikenal sebagai cookie DART, untuk menayangkan iklan kepada pengunjung situs kami.</p>
    """
    create_page("privacy.html", "Privacy Policy", privacy_text)

    # 3. DISCLAIMER
    disclaimer_text = f"""
    <p>Semua informasi di situs web ini ({DOMAIN_NAME}) diterbitkan dengan itikad baik dan untuk tujuan informasi umum saja.</p>
    <p>{SITE_NAME} tidak memberikan jaminan apa pun tentang kelengkapan, keandalan, dan keakuratan data ini. Data daya tampung dan peminat dapat berubah sewaktu-waktu sesuai kebijakan PTN masing-masing.</p>
    <p>Tindakan apa pun yang Anda lakukan atas informasi yang Anda temukan di situs web ini sepenuhnya merupakan risiko Anda sendiri.</p>
    """
    create_page("disclaimer.html", "Disclaimer", disclaimer_text)

    # 4. CONTACT
    contact_text = f"""
    <p>Jika Anda memiliki pertanyaan, saran, atau ingin menghapus data tertentu, silakan hubungi kami melalui email:</p>
    <p><strong>Email: {EMAIL_CONTACT}</strong></p>
    """
    create_page("contact.html", "Hubungi Kami", contact_text)

if __name__ == "__main__":
    main()