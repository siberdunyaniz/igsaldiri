# Otomatik Pip Kurulum Scripti (Düzeltildi)

import subprocess
import sys
import importlib
import time  # time modülünü içe aktardık

# Gerekli kütüphaneler listesi
required_packages = {
    "requests": "requests",
    "pystyle": "pystyle"
}

# Standart kütüphaneler (kurulum gerektirmeyenler)
standard_libs = ["time", "re", "random", "os", "json", "getpass"]

def check_and_install_packages():
    print("📦 Gerekli kütüphaneler kontrol ediliyor...")
    for package_name, pip_name in required_packages.items():
        try:
            importlib.import_module(package_name)
            print(f"✅ {package_name} zaten yüklü.")
        except ImportError:
            print(f"❌ {package_name} bulunamadı, kuruluyor...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
                print(f"✅ {package_name} başarıyla yüklendi!")
            except subprocess.CalledProcessError as e:
                print(f"❌ {package_name} yüklenirken hata oluştu: {e}")
                sys.exit(1)

    # Standart kütüphaneleri kontrol et (bilgi amaçlı)
    print("\n📋 Standart kütüphaneler kontrol ediliyor...")
    for lib in standard_libs:
        try:
            importlib.import_module(lib)
            print(f"✅ {lib} (standart kütüphane) mevcut.")
        except ImportError:
            print(f"❌ {lib} bulunamadı (bu bir hata olmamalı, lütfen Python kurulumunu kontrol edin).")

def loading_animation():
    lix = ['/', '-', '\\', '|']
    for _ in range(8):
        for x in lix:
            sys.stdout.write(f"\r🔍 Kurulumlar kontrol ediliyor {x}")
            sys.stdout.flush()
            time.sleep(0.25)  # time modülü artık tanımlı
    print("\r✅ Kontrol tamamlandı!")

if __name__ == "__main__":
    loading_animation()
    check_and_install_packages()
    print("\n🎉 Tüm gerekli kütüphaneler hazır! Artık toolu çalıştırabilirsiniz.")
    input("⏎ Çıkmak için Enter'a basın...")