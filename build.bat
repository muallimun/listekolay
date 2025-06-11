@echo off
setlocal

:: .bat dosyasının bulunduğu klasöre geç
cd /d "%~dp0"

:: 1. Sanal ortamı oluştur (zaten varsa atla)
if not exist env_listekolay (
    python -m venv env_listekolay
)

:: 2. Ortamı aktive et
call env_listekolay\Scripts\activate.bat

:: 3. pip'i güncelle
python -m pip install --upgrade pip

:: 4. Gerekli kütüphaneleri kur
pip install requests pillow openpyxl python-docx pdf2image PyMuPDF psd-tools Wand cairosvg cssselect2 tinycss2 pyinstaller

:: 5. PyInstaller ile derle (ikon ve veri dosyasını ayarla)
pyinstaller --onefile --windowed --name=ListeKolay --icon=myicon.ico --add-data "listekolay.png;." main.py

:: 6. Derlenen dosya çıktısını göster
echo.
echo ✅ Derleme tamamlandı: dist\ListeKolay.exe
pause

endlocal
