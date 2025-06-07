# -*- mode: python ; coding: utf-8 -*-
block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('translations.py', '.'),
        ('listekolay.png', '.')
    ],
    hiddenimports=[
        'fitz', 'pdf2image', 'PIL.Image', 'openpyxl', 'python-docx', 'requests'
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[
        'unittest', 'tkinter.test', 'xmlrpc', 'sqlite3', 'asyncio', 'numpy', 'scipy'
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='ListeKolay',
    debug=False,
    strip=False,
    upx=True,
    console=False,
    icon='myicon.ico',
    onefile=True
)
