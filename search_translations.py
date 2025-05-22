"""
Search text translations for all languages in the ListeKolay application.
"""

# Create a dictionary of search translations for all languages
search_translations = {
    "tr": "Dosyaları ara...",
    "en": "Search files...",
    "de": "Dateien suchen...",
    "fr": "Rechercher des fichiers...",
    "ru": "Поиск файлов...",
    "es": "Buscar archivos...",
    "it": "Cerca file...",
    "fa": "جستجوی فایل‌ها...",
    "ur": "فائلیں تلاش کریں...",
    "hi": "फ़ाइलें खोजें...",
    "zh": "搜索文件...",
    "ja": "ファイルを検索...",
    "ar": "البحث عن الملفات..."
}

# Toggle panel translations for all languages
toggle_panel_translations = {
    "tr": "Sol paneli aç/kapat",
    "en": "Show/hide left panel",
    "de": "Linkes Panel ein-/ausblenden",
    "fr": "Afficher/masquer le panneau gauche",
    "ru": "Показать/скрыть левую панель",
    "es": "Mostrar/ocultar panel izquierdo",
    "it": "Mostra/nascondi pannello sinistro",
    "fa": "نمایش/مخفی کردن پنل چپ",
    "ur": "بائیں پینل دکھائیں/چھپائیں",
    "hi": "बाएं पैनल दिखाएं/छुपाएं",
    "zh": "显示/隐藏左侧面板",
    "ja": "左パネルの表示/非表示",
    "ar": "إظهار/إخفاء اللوحة اليسرى"
}

# Context menu translations - Complete for all 13 languages
context_menu_translations = {
    # Translations for preview updating process
    "updating_preview": {
        "tr": "Önizleme güncelleniyor...",
        "en": "Updating preview...",
        "de": "Vorschau wird aktualisiert...",
        "fr": "Mise à jour de l'aperçu...",
        "ru": "Обновление предварительного просмотра...",
        "es": "Actualizando vista previa...",
        "it": "Aggiornamento anteprima...",
        "fa": "به‌روزرسانی پیش‌نمایش...",
        "ur": "پیش منظر اپ ڈیٹ ہو رہا ہے...",
        "hi": "पूर्वावलोकन अपडेट हो रहा है...",
        "zh": "正在更新预览...",
        "ja": "プレビューを更新中...",
        "ar": "جاري تحديث المعاينة..."
    },
    
    # Translations for delete confirmation
    "do_you_want_to_delete": {
        "tr": "Bu dosyayı silmek istediğinizden emin misiniz",
        "en": "Are you sure you want to delete this file",
        "de": "Sind Sie sicher, dass Sie diese Datei löschen möchten",
        "fr": "Êtes-vous sûr de vouloir supprimer ce fichier",
        "ru": "Вы уверены, что хотите удалить этот файл",
        "es": "¿Está seguro de que desea eliminar este archivo",
        "it": "Sei sicuro di voler eliminare questo file",
        "fa": "آیا مطمئن هستید که می‌خواهید این فایل را حذف کنید",
        "ur": "کیا آپ واقعی یہ فائل ڈیلیٹ کرنا چاہتے ہیں",
        "hi": "क्या आप वाकई इस फ़ाइल को हटाना चाहते हैं",
        "zh": "您确定要删除此文件吗",
        "ja": "このファイルを削除してもよろしいですか",
        "ar": "هل أنت متأكد من أنك تريد حذف هذا الملف"
    },
    
    # Translations for clipboard operations
    "copied_to_clipboard": {
        "tr": "Panoya kopyalandı",
        "en": "Copied to clipboard",
        "de": "In die Zwischenablage kopiert",
        "fr": "Copié dans le presse-papiers",
        "ru": "Скопировано в буфер обмена",
        "es": "Copiado al portapapeles",
        "it": "Copiato negli appunti",
        "fa": "در کلیپ‌بورد کپی شد",
        "ur": "کلپ بورڈ میں کاپی کر دیا گیا",
        "hi": "क्लिपबोर्ड में कॉपी किया गया",
        "zh": "已复制到剪贴板",
        "ja": "クリップボードにコピーしました",
        "ar": "تم النسخ إلى الحافظة"
    },
    
    # Translations for rename errors
    "rename_error": {
        "tr": "Yeniden adlandırma hatası",
        "en": "Rename error",
        "de": "Umbenennungsfehler",
        "fr": "Erreur de renommage",
        "ru": "Ошибка переименования",
        "es": "Error de cambio de nombre",
        "it": "Errore di rinomina",
        "fa": "خطا در تغییر نام",
        "ur": "نام تبدیل کرنے میں خرابی",
        "hi": "नाम बदलने में त्रुटि",
        "zh": "重命名错误",
        "ja": "名前変更エラー",
        "ar": "خطأ في إعادة التسمية"
    },
    
    # Translations for large file warnings
    "large_file_warning": {
        "tr": "Büyük dosya uyarısı",
        "en": "Large file warning",
        "de": "Große Datei Warnung",
        "fr": "Avertissement fichier volumineux",
        "ru": "Предупреждение о большом файле",
        "es": "Advertencia de archivo grande",
        "it": "Avviso file di grandi dimensioni",
        "fa": "هشدار فایل بزرگ",
        "ur": "بڑی فائل کی تنبیہ",
        "hi": "बड़ी फ़ाइल की चेतावनी",
        "zh": "大文件警告",
        "ja": "大きなファイルの警告",
        "ar": "تحذير ملف كبير"
    },
    
    "large_file_slow": {
        "tr": "Bu dosya çok büyük ve yüklenmesi zaman alabilir",
        "en": "This file is very large and may take time to load",
        "de": "Diese Datei ist sehr groß und das Laden kann dauern",
        "fr": "Ce fichier est très volumineux et peut prendre du temps à charger",
        "ru": "Этот файл очень большой и загрузка может занять время",
        "es": "Este archivo es muy grande y puede tardar en cargarse",
        "it": "Questo file è molto grande e il caricamento potrebbe richiedere tempo",
        "fa": "این فایل بسیار بزرگ است و بارگیری آن ممکن است زمان ببرد",
        "ur": "یہ فائل بہت بڑی ہے اور لوڈ ہونے میں وقت لگ سکتا ہے",
        "hi": "यह फ़ाइल बहुत बड़ी है और लोड होने में समय लग सकता है",
        "zh": "此文件非常大，加载可能需要时间",
        "ja": "このファイルは非常に大きく、読み込みに時間がかかる場合があります",
        "ar": "هذا الملف كبير جداً وقد يستغرق وقتاً للتحميل"
    },
    
    "loading_large_file": {
        "tr": "Büyük dosya yükleniyor...",
        "en": "Loading large file...",
        "de": "Große Datei wird geladen...",
        "fr": "Chargement du fichier volumineux...",
        "ru": "Загрузка большого файла...",
        "es": "Cargando archivo grande...",
        "it": "Caricamento file di grandi dimensioni...",
        "fa": "در حال بارگیری فایل بزرگ...",
        "ur": "بڑی فائل لوڈ ہو رہی ہے...",
        "hi": "बड़ी फ़ाइल लोड हो रही है...",
        "zh": "正在加载大文件...",
        "ja": "大きなファイルを読み込み中...",
        "ar": "جاري تحميل ملف كبير..."
    },
    
    "view_changed_to_list": {
        "tr": "Görünüm liste moduna değiştirildi",
        "en": "View changed to list mode",
        "de": "Ansicht zu Listenmodus geändert",
        "fr": "Vue changée en mode liste",
        "ru": "Вид изменен на режим списка",
        "es": "Vista cambiada a modo lista",
        "it": "Vista cambiata in modalità elenco",
        "fa": "نمایش به حالت لیست تغییر یافت",
        "ur": "فہرست موڈ میں تبدیل کر دیا گیا",
        "hi": "दृश्य सूची मोड में बदला गया",
        "zh": "视图已更改为列表模式",
        "ja": "表示がリストモードに変更されました",
        "ar": "تم تغيير العرض إلى وضع القائمة"
    },
    
    # No preview translations
    "preview_not_available": {
        "tr": "Önizleme Mevcut Değil",
        "en": "No Preview Available",
        "de": "Keine Vorschau verfügbar",
        "fr": "Aucun aperçu disponible",
        "ru": "Предварительный просмотр недоступен",
        "es": "Vista previa no disponible",
        "it": "Anteprima non disponibile",
        "fa": "پیش‌نمایش در دسترس نیست",
        "ur": "پیش منظر دستیاب نہیں",
        "hi": "पूर्वावलोकन उपलब्ध नहीं",
        "zh": "预览不可用",
        "ja": "プレビューが利用できません",
        "ar": "المعاينة غير متوفرة"
    },
    
    # Dosya işlemleri için mesajlar
    "file_deleted": {
        "tr": "Dosya silindi",
        "en": "File deleted",
        "de": "Datei gelöscht",
        "fr": "Fichier supprimé",
        "ru": "Файл удален",
        "es": "Archivo eliminado",
        "it": "File eliminato",
        "fa": "فایل حذف شد",
        "ur": "فائل ڈیلیٹ کر دی گئی",
        "hi": "फ़ाइल हटाई गई",
        "zh": "文件已删除",
        "ja": "ファイルが削除されました",
        "ar": "تم حذف الملف"
    },
    
    "current_name": {
        "tr": "Mevcut Ad",
        "en": "Current Name",
        "de": "Aktueller Name",
        "fr": "Nom actuel",
        "ru": "Текущее имя",
        "es": "Nombre actual",
        "it": "Nome attuale",
        "fa": "نام فعلی",
        "ur": "موجودہ نام",
        "hi": "वर्तमान नाम",
        "zh": "当前名称",
        "ja": "現在の名前",
        "ar": "الاسم الحالي"
    },
    
    "new_name": {
        "tr": "Yeni Ad",
        "en": "New Name",
        "de": "Neuer Name",
        "fr": "Nouveau nom",
        "ru": "Новое имя",
        "es": "Nuevo nombre",
        "it": "Nuovo nome",
        "fa": "نام جدید",
        "ur": "نیا نام",
        "hi": "नया नाम",
        "zh": "新名称",
        "ja": "新しい名前",
        "ar": "الاسم الجديد"
    },
    
    "error_deleting_file": {
        "tr": "Dosya silme hatası",
        "en": "Error deleting file",
        "de": "Fehler beim Löschen der Datei",
        "fr": "Erreur lors de la suppression du fichier",
        "ru": "Ошибка удаления файла",
        "es": "Error al eliminar archivo",
        "it": "Errore nell'eliminazione del file",
        "fa": "خطا در حذف فایل",
        "ur": "فائل ڈیلیٹ کرنے میں خرابی",
        "hi": "फ़ाइल हटाने में त्रुटि",
        "zh": "删除文件时出错",
        "ja": "ファイル削除エラー",
        "ar": "خطأ في حذف الملف"
    },
    
    "confirm_move": {
        "tr": "taşımak istediğinizden emin misiniz",
        "en": "are you sure you want to move",
        "de": "sind Sie sicher, dass Sie verschieben möchten",
        "fr": "êtes-vous sûr de vouloir déplacer",
        "ru": "вы уверены, что хотите переместить",
        "es": "¿está seguro de que desea mover",
        "it": "sei sicuro di voler spostare",
        "fa": "آیا مطمئن هستید که می‌خواهید انتقال دهید",
        "ur": "کیا آپ واقعی منتقل کرنا چاہتے ہیں",
        "hi": "क्या आप वाकई स्थानांतरित करना चाहते हैं",
        "zh": "您确定要移动吗",
        "ja": "移動してもよろしいですか",
        "ar": "هل أنت متأكد من أنك تريد النقل"
    },
    
    "information": {
        "tr": "Bilgi",
        "en": "Information",
        "de": "Information",
        "fr": "Information",
        "ru": "Информация",
        "es": "Información",
        "it": "Informazioni",
        "fa": "اطلاعات",
        "ur": "معلومات",
        "hi": "जानकारी",
        "zh": "信息",
        "ja": "情報",
        "ar": "معلومات"
    },
    
    "select_target_folder": {
        "tr": "Hedef Klasör Seçin",
        "en": "Select Target Folder",
        "de": "Zielordner auswählen",
        "fr": "Sélectionner le dossier cible",
        "ru": "Выберите целевую папку",
        "es": "Seleccionar carpeta de destino",
        "it": "Seleziona cartella di destinazione",
        "fa": "پوشه مقصد را انتخاب کنید",
        "ur": "ہدف فولڈر منتخب کریں",
        "hi": "लक्ष्य फ़ोल्डर चुनें",
        "zh": "选择目标文件夹",
        "ja": "対象フォルダを選択",
        "ar": "اختر المجلد المستهدف"
    },
    
    "operation_complete": {
        "tr": "İşlem Tamamlandı",
        "en": "Operation Complete",
        "de": "Vorgang abgeschlossen",
        "fr": "Opération terminée",
        "ru": "Операция завершена",
        "es": "Operación completada",
        "it": "Operazione completata",
        "fa": "عملیات تکمیل شد",
        "ur": "آپریشن مکمل",
        "hi": "संचालन पूर्ण",
        "zh": "操作完成",
        "ja": "操作が完了しました",
        "ar": "اكتملت العملية"
    },
    
    "copying_files": {
        "tr": "Dosyalar kopyalanıyor",
        "en": "Copying files",
        "de": "Dateien werden kopiert",
        "fr": "Copie des fichiers",
        "ru": "Копирование файлов",
        "es": "Copiando archivos",
        "it": "Copia dei file",
        "fa": "در حال کپی فایل‌ها",
        "ur": "فائلیں کاپی ہو رہی ہیں",
        "hi": "फ़ाइलें कॉपी की जा रही हैं",
        "zh": "正在复制文件",
        "ja": "ファイルをコピー中",
        "ar": "جاري نسخ الملفات"
    },
    
    "file_copy_error": {
        "tr": "Dosya kopyalama hatası",
        "en": "File copy error",
        "de": "Datei-Kopierfehler",
        "fr": "Erreur de copie de fichier",
        "ru": "Ошибка копирования файла",
        "es": "Error al copiar archivo",
        "it": "Errore di copia file",
        "fa": "خطا در کپی فایل",
        "ur": "فائل کاپی کرنے میں خرابی",
        "hi": "फ़ाइल कॉपी त्रुटि",
        "zh": "文件复制错误",
        "ja": "ファイルコピーエラー",
        "ar": "خطأ في نسخ الملف"
    },
    
    "copy_complete": {
        "tr": "Kopyalama tamamlandı. {} dosya başarıyla kopyalandı.",
        "en": "Copy operation completed. {} files successfully copied."
    },
    
    "warning": {
        "tr": "Uyarı",
        "en": "Warning",
        "de": "Warnung",
        "fr": "Avertissement",
        "ru": "Предупреждение",
        "es": "Advertencia",
        "it": "Avviso",
        "fa": "هشدار",
        "ur": "انتباہ",
        "hi": "चेतावनी",
        "zh": "警告",
        "ja": "警告",
        "ar": "تحذير"
    },
    
    # Button texts for dialogs
    "cancel": {
        "tr": "İptal",
        "en": "Cancel",
        "de": "Abbrechen",
        "fr": "Annuler",
        "ru": "Отмена",
        "es": "Cancelar",
        "it": "Annulla",
        "fa": "لغو",
        "ur": "منسوخ",
        "hi": "रद्द करें",
        "zh": "取消",
        "ja": "キャンセル",
        "ar": "إلغاء"
    },
    
    "ok": {
        "tr": "Tamam",
        "en": "OK",
        "de": "OK",
        "fr": "OK",
        "ru": "ОК",
        "es": "Aceptar",
        "it": "OK",
        "fa": "تأیید",
        "ur": "ٹھیک ہے",
        "hi": "ठीक है",
        "zh": "确定",
        "ja": "OK",
        "ar": "موافق"
    },
    
    # Action messages
    "attention": {
        "tr": "DİKKAT",
        "en": "ATTENTION",
        "de": "ACHTUNG",
        "fr": "ATTENTION",
        "ru": "ВНИМАНИЕ",
        "es": "ATENCIÓN",
        "it": "ATTENZIONE",
        "fa": "توجه",
        "ur": "توجہ",
        "hi": "ध्यान",
        "zh": "注意",
        "ja": "注意",
        "ar": "انتباه"
    },
    
    "action_irreversible": {
        "tr": "Bu işlem geri alınamaz",
        "en": "This action is irreversible",
        "de": "Diese Aktion ist unumkehrbar",
        "fr": "Cette action est irréversible",
        "ru": "Это действие необратимо",
        "es": "Esta acción es irreversible",
        "it": "Questa azione è irreversibile",
        "fa": "این عمل غیرقابل برگشت است",
        "ur": "یہ عمل واپس نہیں ہو سکتا",
        "hi": "यह क्रिया अपरिवर्तनीय है",
        "zh": "此操作不可逆",
        "ja": "この操作は元に戻せません",
        "ar": "هذا الإجراء غير قابل للإلغاء"
    },
    
    "confirm_move_files": {
        "tr": "taşınacak. Devam etmek istiyor musunuz",
        "en": "will be moved. Do you want to continue",
        "de": "werden verschoben. Möchten Sie fortfahren",
        "fr": "seront déplacés. Voulez-vous continuer",
        "ru": "будут перемещены. Хотите продолжить",
        "es": "serán movidos. ¿Desea continuar",
        "it": "saranno spostati. Vuoi continuare",
        "fa": "منتقل خواهند شد. آیا می‌خواهید ادامه دهید",
        "ur": "منتقل ہوں گی۔ کیا آپ جاری رکھنا چاہتے ہیں",
        "hi": "स्थानांतरित हो जाएंगी। क्या आप जारी रखना चाहते हैं",
        "zh": "将被移动。您想继续吗",
        "ja": "移動されます。続行しますか",
        "ar": "سيتم نقلها. هل تريد المتابعة"
    },
    
    "file_renamed_successfully": {
        "tr": "Dosya başarıyla yeniden adlandırıldı",
        "en": "File renamed successfully",
        "de": "Datei erfolgreich umbenannt",
        "fr": "Fichier renommé avec succès",
        "ru": "Файл успешно переименован",
        "es": "Archivo renombrado exitosamente",
        "it": "File rinominato con successo",
        "fa": "فایل با موفقیت تغییر نام یافت",
        "ur": "فائل کامیابی سے نام تبدیل ہو گئی",
        "hi": "फ़ाइल सफलतापूर्वक नाम बदला गया",
        "zh": "文件重命名成功",
        "ja": "ファイルの名前が正常に変更されました",
        "ar": "تم إعادة تسمية الملف بنجاح"
    },
    
    # Error messages for file operations
    "selection_error": {
        "tr": "Seçim Hatası",
        "en": "Selection Error"
    },
    "view_changed_to_list": {
        "tr": "Görünüm liste moduna çevrildi",
        "en": "View changed to list mode"
    },
    "no_file_selected": {
        "tr": "Seçilecek dosya yok.",
        "en": "No file selected."
    },
    "rename_error": {
        "tr": "Yeniden Adlandırma Hatası",
        "en": "Rename Error"
    },
    "select_only_one_file": {
        "tr": "Lütfen yalnızca bir dosya seçin.",
        "en": "Please select only one file."
    },
    
    # FILE OPERATIONS
    "copying_files": {
        "tr": "Dosyalar kopyalanıyor...",
        "en": "Copying files...",
        "de": "Dateien werden kopiert...",
        "fr": "Copie de fichiers...",
        "ru": "Копирование файлов...",
        "es": "Copiando archivos...",
        "it": "Copia di file...",
        "zh": "正在复制文件...",
        "ja": "ファイルをコピー中...",
        "ar": "جارٍ نسخ الملفات..."
    },
    "moving_files": {
        "tr": "Dosyalar taşınıyor...",
        "en": "Moving files...",
        "de": "Dateien werden verschoben...",
        "fr": "Déplacement de fichiers...",
        "ru": "Перемещение файлов...",
        "es": "Moviendo archivos...",
        "it": "Spostamento di file...",
        "zh": "正在移动文件...",
        "ja": "ファイルを移動中...",
        "ar": "جارٍ نقل الملفات..."
    },
    "deleting_files": {
        "tr": "Dosyalar siliniyor...",
        "en": "Deleting files...",
        "de": "Dateien werden gelöscht...",
        "fr": "Suppression de fichiers...",
        "ru": "Удаление файлов...",
        "es": "Eliminando archivos...",
        "it": "Eliminazione di file...",
        "zh": "正在删除文件...",
        "ja": "ファイルを削除中...",
        "ar": "جارٍ حذف الملفات..."
    },
    "selection_error": {
        "tr": "Seçim Hatası",
        "en": "Selection Error",
        "de": "Auswahlfehlier",
        "fr": "Erreur de sélection",
        "ru": "Ошибка выбора",
        "es": "Error de selección",
        "it": "Errore di selezione",
        "zh": "选择错误",
        "ja": "選択エラー",
        "ar": "خطأ في الاختيار"
    },
    "no_files_to_select": {
        "tr": "Seçili dosya yok",
        "en": "No files selected",
        "de": "Keine Dateien ausgewählt",
        "fr": "Aucun fichier sélectionné",
        "ru": "Нет выбранных файлов",
        "es": "No hay archivos seleccionados",
        "it": "Nessun file selezionato",
        "zh": "未选择文件",
        "ja": "ファイルが選択されていません",
        "ar": "لم يتم تحديد أي ملفات"
    },
    "select_target_folder": {
        "tr": "Hedef Klasörü Seçin",
        "en": "Select Target Folder",
        "de": "Zielordner auswählen",
        "fr": "Sélectionner le dossier cible",
        "ru": "Выберите целевую папку",
        "es": "Seleccionar carpeta de destino",
        "it": "Seleziona cartella di destinazione",
        "zh": "选择目标文件夹",
        "ja": "対象フォルダを選択",
        "ar": "حدد المجلد الهدف"
    },
    "copy_complete": {
        "tr": "Kopyalama işlemi tamamlandı.\n{} dosya başarıyla kopyalandı.",
        "en": "Copy operation completed.\n{} files successfully copied.",
        "de": "Kopiervorgang abgeschlossen.\n{} Dateien erfolgreich kopiert.",
        "fr": "Opération de copie terminée.\n{} fichiers copiés avec succès.",
        "ru": "Операция копирования завершена.\n{} файлов успешно скопировано.",
        "es": "Operación de copia completada.\n{} archivos copiados con éxito.",
        "it": "Operazione di copia completata.\n{} file copiati con successo.",
        "zh": "复制操作已完成。\n已成功复制 {} 个文件。",
        "ja": "コピー操作が完了しました。\n{} 個のファイルが正常にコピーされました。",
        "ar": "اكتملت عملية النسخ.\nتم نسخ {} ملف بنجاح."
    },
    "move_complete": {
        "tr": "Taşıma işlemi tamamlandı.\n{} dosya başarıyla taşındı.",
        "en": "Move operation completed.\n{} files successfully moved.",
        "de": "Verschiebevorgang abgeschlossen.\n{} Dateien erfolgreich verschoben.",
        "fr": "Opération de déplacement terminée.\n{} fichiers déplacés avec succès.",
        "ru": "Операция перемещения завершена.\n{} файлов успешно перемещено.",
        "es": "Operación de movimiento completada.\n{} archivos movidos con éxito.",
        "it": "Operazione di spostamento completata.\n{} file spostati con successo.",
        "zh": "移动操作已完成。\n已成功移动 {} 个文件。",
        "ja": "移動操作が完了しました。\n{} 個のファイルが正常に移動されました。",
        "ar": "اكتملت عملية النقل.\nتم نقل {} ملف بنجاح."
    },
    "delete_complete": {
        "tr": "Dosya silme işlemi tamamlandı.\n{} dosya başarıyla silindi.",
        "en": "Delete operation completed.\n{} files successfully deleted.",
        "de": "Löschvorgang abgeschlossen.\n{} Dateien erfolgreich gelöscht.",
        "fr": "Opération de suppression terminée.\n{} fichiers supprimés avec succès.",
        "ru": "Операция удаления завершена.\n{} файлов успешно удалено.",
        "es": "Operación de eliminación completada.\n{} archivos eliminados con éxito.",
        "it": "Operazione di eliminazione completata.\n{} file eliminati con successo.",
        "zh": "删除操作已完成。\n已成功删除 {} 个文件。",
        "ja": "削除操作が完了しました。\n{} 個のファイルが正常に削除されました。",
        "ar": "اكتملت عملية الحذف.\nتم حذف {} ملف بنجاح."
    },
    "copy_error": {
        "tr": "Kopyalama Hatası",
        "en": "Copy Error",
        "de": "Kopierfehler",
        "fr": "Erreur de copie",
        "ru": "Ошибка копирования",
        "es": "Error de copia",
        "it": "Errore di copia",
        "zh": "复制错误",
        "ja": "コピーエラー",
        "ar": "خطأ في النسخ"
    },
    "move_error": {
        "tr": "Taşıma Hatası",
        "en": "Move Error",
        "de": "Verschiebefehler",
        "fr": "Erreur de déplacement",
        "ru": "Ошибка перемещения",
        "es": "Error de movimiento",
        "it": "Errore di spostamento",
        "zh": "移动错误",
        "ja": "移動エラー",
        "ar": "خطأ في النقل"
    },
    "delete_error": {
        "tr": "Silme Hatası",
        "en": "Delete Error",
        "de": "Löschfehler",
        "fr": "Erreur de suppression",
        "ru": "Ошибка удаления",
        "es": "Error de eliminación",
        "it": "Errore di eliminazione",
        "zh": "删除错误",
        "ja": "削除エラー",
        "ar": "خطأ في الحذف"
    },
    "confirm_copy": {
        "tr": "dosyayı kopyalamak istediğinizden emin misiniz",
        "en": "Are you sure you want to copy",
        "de": "Sind Sie sicher, dass Sie kopieren möchten",
        "fr": "Êtes-vous sûr de vouloir copier",
        "ru": "Вы уверены, что хотите скопировать",
        "es": "¿Está seguro de que desea copiar",
        "it": "Sei sicuro di voler copiare",
        "zh": "您确定要复制",
        "ja": "コピーしてもよろしいですか",
        "ar": "هل أنت متأكد أنك تريد نسخ"
    },
    "confirm_move": {
        "tr": "dosyayı taşımak istediğinizden emin misiniz",
        "en": "Are you sure you want to move",
        "de": "Sind Sie sicher, dass Sie verschieben möchten",
        "fr": "Êtes-vous sûr de vouloir déplacer",
        "ru": "Вы уверены, что хотите переместить",
        "es": "¿Está seguro de que desea mover",
        "it": "Sei sicuro di voler spostare",
        "zh": "您确定要移动",
        "ja": "移動してもよろしいですか",
        "ar": "هل أنت متأكد أنك تريد نقل"
    },
    "preview_file": {
        "tr": "Dosyayı Önizle",
        "en": "Preview File",
        "de": "Datei-Vorschau",
        "fr": "Aperçu du fichier",
        "ru": "Предварительный просмотр файла",
        "es": "Vista previa del archivo",
        "it": "Anteprima file",
        "zh": "预览文件",
        "ja": "ファイルプレビュー",
        "ar": "معاينة الملف"
    },
    "delete_files": {
        "tr": "Dosyayı Sil",
        "en": "Delete File",
        "de": "Datei löschen",
        "fr": "Supprimer le fichier",
        "ru": "Удалить файл",
        "es": "Eliminar archivo",
        "it": "Elimina file",
        "zh": "删除文件",
        "ja": "ファイルを削除",
        "ar": "حذف الملف"
    },
    "copy_files": {
        "tr": "Dosyayı Kopyala",
        "en": "Copy File",
        "de": "Datei kopieren",
        "fr": "Copier le fichier",
        "ru": "Копировать файл",
        "es": "Copiar archivo",
        "it": "Copia file",
        "zh": "复制文件",
        "ja": "ファイルをコピー",
        "ar": "نسخ الملف"
    },
    "move_files": {
        "tr": "Dosyayı Taşı",
        "en": "Move File",
        "de": "Datei verschieben",
        "fr": "Déplacer le fichier",
        "ru": "Переместить файл",
        "es": "Mover archivo",
        "it": "Sposta file",
        "zh": "移动文件",
        "ja": "ファイルを移動",
        "ar": "نقل الملف"
    },
    "rename_file": {
        "tr": "Yeniden Adlandır",
        "en": "Rename",
        "de": "Umbenennen",
        "fr": "Renommer",
        "ru": "Переименовать",
        "es": "Renombrar",
        "it": "Rinomina",
        "zh": "重命名",
        "ja": "名前を変更",
        "ar": "إعادة تسمية"
    },
    "select_all_files": {
        "tr": "Tümünü Seç",
        "en": "Select All",
        "de": "Alle auswählen",
        "fr": "Tout sélectionner",
        "ru": "Выбрать все",
        "es": "Seleccionar todo",
        "it": "Seleziona tutto",
        "zh": "全选",
        "ja": "すべて選択",
        "ar": "تحديد الكل"
    },
    "confirm_delete": {
        "tr": "Silme Onayı",
        "en": "Confirm Delete",
        "de": "Löschen bestätigen",
        "fr": "Confirmer la suppression",
        "ru": "Подтвердите удаление",
        "es": "Confirmar eliminación",
        "it": "Conferma eliminazione",
        "zh": "确认删除",
        "ja": "削除の確認",
        "ar": "تأكيد الحذف"
    },
    "confirm_delete_file": {
        "tr": "dosyasını silmek istediğinize emin misiniz",
        "en": "Are you sure you want to delete the file",
        "de": "Sind Sie sicher, dass Sie die Datei löschen möchten",
        "fr": "Êtes-vous sûr de vouloir supprimer le fichier",
        "ru": "Вы уверены, что хотите удалить файл",
        "es": "¿Está seguro de que desea eliminar el archivo",
        "it": "Sei sicuro di voler eliminare il file",
        "zh": "您确定要删除文件吗",
        "ja": "ファイルを削除してもよろしいですか",
        "ar": "هل أنت متأكد أنك تريد حذف الملف"
    },
    "warning": {
        "tr": "Uyarı",
        "en": "Warning",
        "de": "Warnung",
        "fr": "Avertissement",
        "ru": "Предупреждение",
        "es": "Advertencia",
        "it": "Avviso",
        "zh": "警告",
        "ja": "警告",
        "ar": "تحذير"
    },
    "action_irreversible": {
        "tr": "Bu işlem geri alınamaz",
        "en": "This action cannot be undone",
        "de": "Diese Aktion kann nicht rückgängig gemacht werden",
        "fr": "Cette action ne peut pas être annulée",
        "ru": "Это действие нельзя отменить",
        "es": "Esta acción no se puede deshacer",
        "it": "Questa azione non può essere annullata",
        "zh": "此操作无法撤消",
        "ja": "このアクションは元に戻せません",
        "ar": "لا يمكن التراجع عن هذا الإجراء"
    },
    "permanent_delete": {
        "tr": "kalıcı olarak silinecek",
        "en": "will be permanently deleted",
        "de": "wird dauerhaft gelöscht",
        "fr": "sera supprimé définitivement",
        "ru": "будет удален навсегда",
        "es": "se eliminará permanentemente",
        "it": "verrà eliminato permanentemente",
        "zh": "将被永久删除",
        "ja": "完全に削除されます",
        "ar": "سيتم حذفه نهائيًا"
    },
    "files": {
        "tr": "dosya",
        "en": "file(s)",
        "de": "Datei(en)",
        "fr": "fichier(s)",
        "ru": "файл(ы)",
        "es": "archivo(s)",
        "it": "file",
        "zh": "个文件",
        "ja": "ファイル",
        "ar": "ملف(ات)"
    },
    "operation_complete": {
        "tr": "İşlem Tamamlandı",
        "en": "Operation Complete",
        "de": "Vorgang abgeschlossen",
        "fr": "Opération terminée",
        "ru": "Операция завершена",
        "es": "Operación completada",
        "it": "Operazione completata",
        "zh": "操作完成",
        "ja": "操作完了",
        "ar": "اكتملت العملية"
    },
    "rename_error": {
        "tr": "Yeniden Adlandırma Hatası",
        "en": "Rename Error",
        "de": "Umbenennungsfehler",
        "fr": "Erreur de renommage",
        "ru": "Ошибка переименования",
        "es": "Error de renombrado",
        "it": "Errore di ridenominazione",
        "zh": "重命名错误",
        "ja": "名前変更エラー",
        "ar": "خطأ في إعادة التسمية"
    },
    "renaming_file": {
        "tr": "Dosya yeniden adlandırılıyor",
        "en": "Renaming file",
        "de": "Datei wird umbenannt",
        "fr": "Renommage du fichier",
        "ru": "Переименование файла",
        "es": "Renombrando archivo",
        "it": "Rinominando file",
        "zh": "正在重命名文件",
        "ja": "ファイルの名前を変更中",
        "ar": "جارٍ إعادة تسمية الملف"
    },
    "file_copy_error": {
        "tr": "Dosya kopyalanamadı",
        "en": "File could not be copied",
        "de": "Datei konnte nicht kopiert werden",
        "fr": "Le fichier n'a pas pu être copié",
        "ru": "Не удалось скопировать файл",
        "es": "No se pudo copiar el archivo",
        "it": "Impossibile copiare il file",
        "zh": "无法复制文件",
        "ja": "ファイルをコピーできませんでした",
        "ar": "تعذر نسخ الملف"
    },
    "file_move_error": {
        "tr": "Dosya taşınamadı",
        "en": "File could not be moved",
        "de": "Datei konnte nicht verschoben werden",
        "fr": "Le fichier n'a pas pu être déplacé",
        "ru": "Не удалось переместить файл",
        "es": "No se pudo mover el archivo",
        "it": "Impossibile spostare il file",
        "zh": "无法移动文件",
        "ja": "ファイルを移動できませんでした",
        "ar": "تعذر نقل الملف"
    },
    "error": {
        "tr": "Hata",
        "en": "Error",
        "de": "Fehler",
        "fr": "Erreur",
        "ru": "Ошибка",
        "es": "Error",
        "it": "Errore",
        "zh": "错误",
        "ja": "エラー",
        "ar": "خطأ"
    },
    "attention": {
        "tr": "DİKKAT",
        "en": "ATTENTION",
        "de": "ACHTUNG",
        "fr": "ATTENTION",
        "ru": "ВНИМАНИЕ",
        "es": "ATENCIÓN", 
        "it": "ATTENZIONE",
        "zh": "注意",
        "ja": "注意",
        "ar": "انتباه"
    },
    "confirm_continue": {
        "tr": "Devam etmek istiyor musunuz",
        "en": "Do you want to continue",
        "de": "Möchten Sie fortfahren",
        "fr": "Voulez-vous continuer",
        "ru": "Хотите продолжить",
        "es": "¿Desea continuar",
        "it": "Vuoi continuare",
        "zh": "您想继续吗",
        "ja": "続行しますか",
        "ar": "هل تريد المتابعة"
    },
    "file_exists": {
        "tr": "Bu isimde bir dosya zaten var. Üzerine yazmak istiyor musunuz",
        "en": "A file with this name already exists. Do you want to overwrite it",
        "de": "Eine Datei mit diesem Namen existiert bereits. Möchten Sie sie überschreiben",
        "fr": "Un fichier portant ce nom existe déjà. Voulez-vous l'écraser",
        "ru": "Файл с таким именем уже существует. Вы хотите перезаписать его",
        "es": "Ya existe un archivo con este nombre. ¿Desea sobrescribirlo",
        "it": "Esiste già un file con questo nome. Vuoi sovrascriverlo",
        "zh": "同名文件已存在。您想覆盖它吗",
        "ja": "同じ名前のファイルが既に存在します。上書きしますか",
        "ar": "يوجد بالفعل ملف بهذا الاسم. هل تريد استبداله"
    }
}