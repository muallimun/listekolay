# ListeKolay - EasyLister (Windows & Linux)

**ListeKolay** / **EasyLister** is a multilingual desktop utility that helps you generate organized and filtered file lists from any folder on your computer. It offers a user-friendly and modern interface with powerful filtering and preview features.

**ListeKolay**, bilgisayarınızdaki klasörlerdeki tüm dosyaları hızlı ve filtrelenebilir şekilde listelemenizi sağlayan çok dilli bir masaüstü uygulamasıdır. Modern, sade ve kullanıcı dostu arayüzü sayesinde dosya uzantılarına göre filtreleme, istatistik görüntüleme, farklı formatlarda dışa aktarma (TXT, Excel, Word, HTML) ve görsel önizleme gibi özellikleri destekler.

---

## 🚀 Features / Özellikler

- ✅ Fast folder scanning  
  Klasörlerdeki dosyaları hızlı tarama  
- 📂 Optional subfolder inclusion  
  Alt klasörleri dahil etme seçeneği  
- 🔍 Filter by file types (images, documents, media, etc.)  
  Dosya türüne göre filtreleme (resim, video, belge, vb.)  
- 📤 Export file list to TXT, Excel, Word, or HTML  
  Listeyi TXT, Excel, Word, HTML olarak dışa aktarabilme  
- 🖼️ Preview for images and PDFs (JPG, PNG, PSD, AI, PDF, etc.)  
  Görsel ve PDF dosyaları için önizleme  
- 📊 File statistics (count, size, folder count)  
  Dosya sayısı, boyut ve klasör istatistikleri  
- 🌐 Multilingual support (Turkish, English, Arabic, French, etc.)  
  Çoklu dil desteği (Türkçe, İngilizce, Arapça, Fransızca...)  
- 🔄 Built-in version check and update system  
  Güncelleme kontrolü ve versiyon görüntüleme  

---

## 🧰 Requirements / Gereksinimler

- Python 3.8+
- Libraries:

  - `requests`
  - `pillow`
  - `openpyxl`
  - `python-docx`
  - `pdf2image`
  - `PyMuPDF` (`fitz`)

📦 Install dependencies / Bağımlılıkları yüklemek için:

```bash
pip install -r requirements.txt
```

---

## 📦 Installation / Kurulum

### ▶️ Python Version (All Platforms):

You can run the `listekolay2.py` file directly after installing the dependencies.

Gerekli kütüphaneleri kurduktan sonra `listekolay2.py` dosyasını doğrudan çalıştırabilirsiniz.

---

### 🪟 Windows .exe Version:

You can download the precompiled `.exe` version from the [Releases](https://github.com/muallimun/listekolay/releases/) page.  
Hazır `.exe` dosyasını indirmek için [Releases](https://github.com/muallimun/listekolay/releases/) sayfasını ziyaret edin.

---

### 🐧 Linux Version:

The Linux version is provided as a `.deb` installer. You can download and install it using the commands below:

Linux sürümü `.deb` paketi olarak sunulmuştur. Aşağıdaki komutlarla indirebilir ve kurabilirsiniz:

```bash
wget https://github.com/muallimun/listekolay/releases/download/5.2.0/listekolay_linux.deb
sudo dpkg -i listekolay_linux.deb
```

> Eğer eksik bağımlılıklar nedeniyle hata alırsanız, şu komutu çalıştırın:
>
> ```bash
> sudo apt --fix-broken install
> ```

---

## 🌐 Supported Languages / Desteklenen Diller

- 🇹🇷 Turkish / Türkçe  
- 🇬🇧 English / İngilizce  
- 🇸🇦 Arabic / Arapça  
- 🇫🇷 French / Fransızca  
- ...and more / ve daha fazlası...

---

## 📁 Version / Sürüm

`5.2.0`

---

## 📄 License / Lisans

This project is licensed under the **Creative Commons BY-NC 4.0** license.  
You may use and share the software **for personal and educational purposes only**.  
**Commercial use is not permitted.**

Bu proje **Creative Commons BY-NC 4.0** lisansı altındadır.  
Yazılımı yalnızca **kişisel ve eğitim amaçlı** kullanabilir ve paylaşabilirsiniz.  
**Ticari kullanım yasaktır.**
