"""
Theme manager for ListeKolay application.
Provides support for light and dark themes with consistent colors.
"""

import tkinter as tk
from tkinter import ttk

# Light Mode Colors
LIGHT_MODE_COLORS = {
    "bg": "#e9ecef",             # Light gray background
    "text": "#000000",           # Black for all text and labels
    "secondary_text": "#000000", # Secondary text also black
    "accent": "#007bff",         # Blue accent

    # Button Colors (Light mode)
    "folder_button": "#007bff",  # Folder select button: Blue
    "exit_button": "#6c757d",    # Exit button: Gray
    "cancel_button": "#dc3545",  # Cancel button: Red  
    "start_button": "#28a745",   # Start button: Green
    "filter_button": "#17a2b8",  # Filter button: Turquoise

    # View mode buttons
    "active_view_button": "#17a2b8",   # Active view button: Turquoise
    "inactive_view_button": "#6c757d", # Inactive view button: Dark gray

    # Common colors
    "button_text": "#ffffff",     # Button text white in light theme
    "highlight": "#f8f9fa",       # Very light gray highlight
    "border": "#ced4da",          # Light gray border
    "error": "#dc3545",           # Red error
    "success": "#28a745",         # Green success
    "warning": "#ffc107"          # Yellow warning
}

# Dark Mode Colors
DARK_MODE_COLORS = {
    "bg": "#212529",             # Dark background
    "text": "#ffffff",           # White for all text and labels
    "secondary_text": "#ffffff", # Secondary text also white
    "accent": "#0d6efd",         # Bright blue accent

    # Button Colors (Dark mode)
    "folder_button": "#007bff",  # Folder select button: Blue
    "exit_button": "#6c757d",    # Exit button: Gray
    "cancel_button": "#dc3545",  # Cancel button: Red
    "start_button": "#28a745",   # Start button: Green
    "filter_button": "#17a2b8",  # Filter button: Turquoise

    # View mode buttons
    "active_view_button": "#17a2b8",   # Active view button: Turquoise
    "inactive_view_button": "#6c757d", # Inactive view button: Dark gray

    # Common colors
    "button_text": "#ffffff",     # Button text white in dark theme
    "highlight": "#2b3035",       # Slightly lighter dark gray highlight
    "border": "#495057",          # Medium dark gray border
    "error": "#dc3545",           # Red error
    "success": "#28a745",         # Green success
    "warning": "#ffc107"          # Yellow warning
}

def apply_theme(theme_name):
    """
    Apply the selected theme to the ttk styles.
    
    Args:
        theme_name (str): 'light' or 'dark'
    """
    # Get the appropriate color scheme
    colors = LIGHT_MODE_COLORS if theme_name == "light" else DARK_MODE_COLORS
    
    # Create style object
    style = ttk.Style()
    
    # Configure ttk themes (use 'clam' as it's most customizable)
    style.theme_use('clam')
    
    # Configure common styles
    style.configure('TFrame', background=colors["bg"])
    style.configure('TLabel', background=colors["bg"], foreground=colors["text"])
    style.configure('TButton', background=colors["border"], foreground=colors["button_text"],
                   padding=(10, 5), relief=tk.RAISED)
    
    # Configure special button styles
    style.configure('Folder.TButton', background=colors["folder_button"], foreground=colors["button_text"])
    style.configure('Start.TButton', background=colors["start_button"], foreground=colors["button_text"])
    style.configure('Cancel.TButton', background=colors["cancel_button"], foreground=colors["button_text"])
    style.configure('Exit.TButton', background=colors["exit_button"], foreground=colors["button_text"])
    style.configure('Filter.TButton', background=colors["filter_button"], foreground=colors["button_text"])
    
    # Configure active view button style
    style.configure('Active.TButton', background=colors["active_view_button"], foreground=colors["button_text"])
    
    # Configure checkbutton and radiobutton
    style.configure('TCheckbutton', background=colors["bg"], foreground=colors["text"])
    style.configure('TRadiobutton', background=colors["bg"], foreground=colors["text"])
    
    # Configure notebook
    style.configure('TNotebook', background=colors["bg"])
    style.configure('TNotebook.Tab', background=colors["border"], foreground=colors["text"],
                   padding=(10, 5))
    style.map('TNotebook.Tab', background=[('selected', colors["accent"])],
              foreground=[('selected', colors["button_text"])])
    
    # Configure listbox and combobox
    style.configure('TCombobox', background=colors["bg"], fieldbackground=colors["bg"],
                   foreground=colors["text"], arrowcolor=colors["text"])
    
    # Configure treeview
    style.configure('Treeview', background=colors["bg"], foreground=colors["text"],
                   fieldbackground=colors["bg"])
    style.map('Treeview', background=[('selected', colors["accent"])],
             foreground=[('selected', colors["button_text"])])
    
    # Configure scrollbar
    style.configure('TScrollbar', background=colors["border"], troughcolor=colors["bg"],
                   arrowcolor=colors["text"])
    
    # Configure progressbar
    style.configure('TProgressbar', background=colors["accent"], troughcolor=colors["border"])
    
    # Configure labelframe
    style.configure('TLabelframe', background=colors["bg"], foreground=colors["text"])
    style.configure('TLabelframe.Label', background=colors["bg"], foreground=colors["text"])
    
    # Configure entry
    style.configure('TEntry', background=colors["bg"], foreground=colors["text"],
                   fieldbackground=colors["bg"], insertcolor=colors["text"])
    
    # Map hover and pressed states for buttons
    style.map('TButton', 
             background=[('active', colors["accent"]), 
                        ('pressed', colors["border"])],
             foreground=[('active', colors["button_text"]),
                        ('pressed', colors["button_text"])])
    
    # Map hover states for special buttons
    for button_style in ['Folder.TButton', 'Start.TButton', 'Cancel.TButton', 
                         'Exit.TButton', 'Filter.TButton', 'Active.TButton']:
        base_color = style.lookup(button_style, 'background')
        style.map(button_style, 
                 background=[('active', lighten_color(base_color)),
                            ('pressed', darken_color(base_color))],
                 foreground=[('active', colors["button_text"]),
                            ('pressed', colors["button_text"])])

def lighten_color(hex_color, factor=0.2):
    """Lighten a hex color by a factor (between 0 and 1)"""
    try:
        # Convert hex to RGB
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        
        # Increase each component
        r = min(255, r + int((255 - r) * factor))
        g = min(255, g + int((255 - g) * factor))
        b = min(255, b + int((255 - b) * factor))
        
        # Convert back to hex
        return f'#{r:02x}{g:02x}{b:02x}'
    except Exception:
        return hex_color

def darken_color(hex_color, factor=0.2):
    """Darken a hex color by a factor (between 0 and 1)"""
    try:
        # Convert hex to RGB
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        
        # Decrease each component
        r = max(0, r - int(r * factor))
        g = max(0, g - int(g * factor))
        b = max(0, b - int(b * factor))
        
        # Convert back to hex
        return f'#{r:02x}{g:02x}{b:02x}'
    except Exception:
        return hex_color
