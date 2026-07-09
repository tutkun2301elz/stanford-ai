import os

# Eklenecek iletişim bölümü
ILETISIM_KODU = """
<div style="margin-top:40px;padding:20px;background:#1a2a3a;color:#fff;border-radius:10px;text-align:center;font-family:Arial,sans-serif;">
    <h3 style="color:#ffd700;">🏠 Bu Dijital Varlık Kiralıktır</h3>
    <p style="color:#ccc;">Yüksek otoriteli .edu uzantılı, SEO uyumlu, modern tasarımlı site.</p>
    <p><strong style="color:#ffd700;">Kiralama Bedeli: $75 / ay</strong></p>
    <p>📩 Teklifleriniz için: <a href="mailto:kiralama@fatih.com" style="color:#ffd700;">kiralama@fatih.com</a></p>
    <p style="font-size:12px;color:#888;margin-top:10px;">FATİH Sistemi ile güçlendirilmiştir.</p>
</div>
"""

# Bulunduğunuz klasördeki tüm HTML dosyalarını tara
for dosya in os.listdir():
    if dosya.endswith(".html") and dosya != "ads.txt":
        with open(dosya, "r", encoding="utf-8") as f:
            icerik = f.read()
        
        # Eğer zaten eklenmişse atla
        if "Bu Dijital Varlık Kiralıktır" in icerik:
            print(f"⏭️ Atlanıyor: {dosya}")
            continue
        
        # İletişim kutusunu ekle
        yeni_icerik = icerik.replace("</body>", f"{ILETISIM_KODU}\n</body>")
        
        with open(dosya, "w", encoding="utf-8") as f:
            f.write(yeni_icerik)
        print(f"✅ Güncellendi: {dosya}")

print("🎯 Tüm dosyalar güncellendi!")