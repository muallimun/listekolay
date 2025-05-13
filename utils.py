"""
Utility functions for ListeKolay application.
"""

import os
import sys
import logging
import logging.handlers
from PIL import Image

def setup_logging():
    """
    Set up rotating log system.
    This ensures log files are archived when they reach a certain size,
    and a new log file is started, preventing disk space issues.
    """
    log_file = "ListeKolay.log"
    
    # Check if application is running in EXE mode
    if getattr(sys, 'frozen', False):
        # EXE mode, use application directory
        exe_dir = os.path.dirname(sys.executable)
        log_file = os.path.join(exe_dir, log_file)
    
    # Rotating log configuration
    log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    
    # Create file handler, max size 5MB, keep 3 old files
    file_handler = logging.handlers.RotatingFileHandler(
        log_file, 
        maxBytes=5*1024*1024,  # 5MB
        backupCount=3,  # Keep 3 old log files
        encoding='utf-8'
    )
    file_handler.setFormatter(log_formatter)
    
    # Root logger configuration
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    
    # Remove previous handlers (if any)
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # Add new handler
    root_logger.addHandler(file_handler)
    
    # Log that the logging system is started
    logging.info("Program started - Rotating log system active (max 5MB, 3 archives)")

def get_pil_resize_method():
    """
    Get the appropriate PIL resizing method based on the installed version.
    
    Returns:
        Object: PIL resampling filter
    """
    try:
        return Image.Resampling.LANCZOS  # PIL 9.0 and later
    except (AttributeError, TypeError):
        try:
            return Image.LANCZOS  # PIL 4.0 to 8.x
        except (AttributeError, TypeError):
            try:
                return Image.ANTIALIAS  # PIL 1.1.3 to 3.x
            except (AttributeError, TypeError):
                return Image.BICUBIC  # Fallback

def get_file_size_str(size_in_bytes):
    """
    Convert file size in bytes to a human-readable string.
    
    Args:
        size_in_bytes (int): File size in bytes
        
    Returns:
        str: Human-readable file size string
    """
    if size_in_bytes < 1024:
        return f"{size_in_bytes} B"
    elif size_in_bytes < 1024 * 1024:
        return f"{size_in_bytes / 1024:.1f} KB"
    elif size_in_bytes < 1024 * 1024 * 1024:
        return f"{size_in_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_in_bytes / (1024 * 1024 * 1024):.2f} GB"

def get_file_count_in_folder(folder_path, include_subfolders=True):
    """
    Count files in a folder.
    
    Args:
        folder_path (str): Path to the folder
        include_subfolders (bool): Whether to include subfolders
        
    Returns:
        tuple: (total_files, folder_count, total_size)
    """
    total_files = 0
    folder_count = 0
    total_size = 0
    
    try:
        if include_subfolders:
            # Walk through all directories
            for root, dirs, files in os.walk(folder_path):
                folder_count += len(dirs)
                total_files += len(files)
                
                # Calculate size of all files
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        total_size += os.path.getsize(file_path)
                    except:
                        pass
        else:
            # Only count files in the current directory
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                
                if os.path.isdir(item_path):
                    folder_count += 1
                elif os.path.isfile(item_path):
                    total_files += 1
                    try:
                        total_size += os.path.getsize(item_path)
                    except:
                        pass
    except Exception as e:
        logging.error(f"Error counting files: {e}")
    
    return total_files, folder_count, total_size

def create_directory_if_not_exists(directory_path):
    """
    Create a directory if it doesn't exist.
    
    Args:
        directory_path (str): Directory path to create
        
    Returns:
        bool: True if directory exists or was created, False on error
    """
    try:
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)
        return True
    except Exception as e:
        logging.error(f"Error creating directory {directory_path}: {e}")
        return False

def get_desktop_path():
    """
    Get the path to the user's desktop.
    
    Returns:
        str: Path to desktop
    """
    return os.path.join(os.path.expanduser("~"), "Desktop")

def is_file_accessible(file_path, mode='r'):
    """
    Check if a file is accessible with the given mode.
    
    Args:
        file_path (str): Path to the file
        mode (str): Access mode ('r' for read, 'w' for write)
        
    Returns:
        bool: True if file is accessible, False otherwise
    """
    try:
        with open(file_path, mode):
            return True
    except:
        return False

def safe_filename(filename):
    """
    Make a filename safe for all operating systems by removing invalid characters.
    
    Args:
        filename (str): Original filename
        
    Returns:
        str: Safe filename
    """
    # Characters that are invalid in most file systems
    invalid_chars = '<>:"/\\|?*'
    
    # Replace invalid characters with underscore
    for char in invalid_chars:
        filename = filename.replace(char, '_')
    
    # Trim leading/trailing whitespace and periods
    filename = filename.strip(' .')
    
    # Ensure the filename isn't empty or just whitespace
    if not filename or filename.isspace():
        filename = "unnamed_file"
        
    return filename

def safe_path_join(*paths):
    """
    Safely join paths with proper handling of separators.
    
    Args:
        *paths: Path components to join
        
    Returns:
        str: Joined path
    """
    # Replace backslashes with forward slashes for consistency
    normalized_paths = [p.replace('\\', '/') for p in paths]
    
    # Join paths and normalize separators
    result = os.path.normpath(os.path.join(*normalized_paths))
    
    return result
