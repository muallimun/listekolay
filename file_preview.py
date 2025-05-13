"""
File preview handling for ListeKolay application.
Provides preview generation for supported file types.
"""

import os
import io
import logging
import tkinter as tk
from tkinter import ttk, messagebox
import platform
import threading
import tempfile
from PIL import Image, ImageTk
import fitz  # PyMuPDF
import pdf2image
import warnings

# Disable DecompressionBombWarning (for EPS and large images)
warnings.simplefilter('ignore', Image.DecompressionBombWarning)
# Increase PIL maximum size limit
Image.MAX_IMAGE_PIXELS = None

# Supported preview extensions
PREVIEWABLE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.pdf', '.eps', '.ai', '.psd', '.tif', '.tiff', '.bmp', '.ico', '.svg', '.webp']

def is_previewable_file(file_path):
    """
    Check if a file can be previewed.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        bool: True if the file can be previewed, False otherwise
    """
    if not os.path.exists(file_path):
        return False
        
    # Get file extension (lowercase)
    _, file_ext = os.path.splitext(file_path.lower())
    
    return file_ext in PREVIEWABLE_EXTENSIONS

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

def get_thumbnail(file_path, size=(200, 200)):
    """
    Generate a thumbnail for a file.
    
    Args:
        file_path (str): Path to the file
        size (tuple): Thumbnail size (width, height)
        
    Returns:
        PIL.Image or None: Thumbnail image or None if thumbnail cannot be generated
    """
    try:
        if not os.path.exists(file_path):
            logging.error(f"File not found: {file_path}")
            return None
            
        # Get file extension (lowercase)
        _, file_ext = os.path.splitext(file_path.lower())
        
        # Handle different file types
        if file_ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff', '.ico', '.webp']:
            # Regular image files
            with Image.open(file_path) as img:
                # Handle animated GIFs - just use the first frame
                if hasattr(img, 'is_animated') and img.is_animated:
                    img.seek(0)
                
                # Create thumbnail
                img.thumbnail(size, get_pil_resize_method())
                return img.convert('RGB') if img.mode == 'RGBA' else img
                
        elif file_ext == '.svg':
            # SVG files - try to use a library if available or create a placeholder icon
            try:
                from cairosvg import svg2png
                png_data = svg2png(url=file_path, output_width=size[0], output_height=size[1])
                return Image.open(io.BytesIO(png_data))
            except (ImportError, Exception):
                # Create a placeholder icon for SVG files
                return create_placeholder_icon("SVG", size)
                
        elif file_ext == '.pdf':
            # PDF files
            return get_pdf_thumbnail(file_path, size)
            
        elif file_ext in ['.eps', '.ai']:
            # EPS/AI files - try using Ghostscript via PIL
            try:
                with Image.open(file_path) as img:
                    img.thumbnail(size, get_pil_resize_method())
                    return img
            except Exception as e:
                logging.error(f"Error creating EPS/AI thumbnail: {e}")
                return create_placeholder_icon("EPS/AI", size)
                
        elif file_ext == '.psd':
            # PSD files
            try:
                with Image.open(file_path) as img:
                    img.thumbnail(size, get_pil_resize_method())
                    return img
            except Exception as e:
                logging.error(f"Error creating PSD thumbnail: {e}")
                return create_placeholder_icon("PSD", size)
                
        else:
            # Unsupported file type
            return None
            
    except Exception as e:
        logging.error(f"Error generating thumbnail for {file_path}: {e}")
        return None

def get_pdf_thumbnail(file_path, size=(200, 200)):
    """
    Generate a thumbnail for a PDF file.
    
    Args:
        file_path (str): Path to the PDF file
        size (tuple): Thumbnail size (width, height)
        
    Returns:
        PIL.Image or None: Thumbnail image or None if thumbnail cannot be generated
    """
    try:
        # First attempt: Use PyMuPDF (faster)
        try:
            pdf_document = fitz.open(file_path)
            if pdf_document.page_count > 0:
                page = pdf_document[0]  # First page
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Increase quality with matrix
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                img.thumbnail(size, get_pil_resize_method())
                pdf_document.close()
                return img
        except Exception as e:
            logging.error(f"PyMuPDF error for {file_path}: {e}")
            
        # Second attempt: Use pdf2image (poppler-based)
        try:
            pages = pdf2image.convert_from_path(
                file_path, 
                first_page=1, 
                last_page=1, 
                size=max(size)
            )
            if pages:
                img = pages[0]
                img.thumbnail(size, get_pil_resize_method())
                return img
        except Exception as e:
            logging.error(f"pdf2image error for {file_path}: {e}")
            
        # If all methods fail, create a placeholder
        return create_placeholder_icon("PDF", size)
        
    except Exception as e:
        logging.error(f"Error generating PDF thumbnail for {file_path}: {e}")
        return create_placeholder_icon("PDF", size)

def create_placeholder_icon(text, size=(200, 200)):
    """
    Create a placeholder image with text.
    
    Args:
        text (str): Text to display on the placeholder
        size (tuple): Image size (width, height)
        
    Returns:
        PIL.Image: Placeholder image
    """
    img = Image.new('RGB', size, color=(240, 240, 240))
    from PIL import ImageDraw, ImageFont
    
    draw = ImageDraw.Draw(img)
    
    # Draw border
    draw.rectangle([(0, 0), (size[0]-1, size[1]-1)], outline=(200, 200, 200))
    
    # Try to get a font
    try:
        # Try to use a default font
        font_size = size[0] // 10
        font = ImageFont.truetype("arial.ttf", font_size)
    except Exception:
        # If that fails, use the default
        font = None
    
    # Draw text
    text_width, text_height = draw.textsize(text, font=font) if hasattr(draw, 'textsize') else (size[0]//2, size[1]//2)
    position = ((size[0] - text_width) // 2, (size[1] - text_height) // 2)
    
    # Draw text with shadow for better visibility
    shadow_position = (position[0]+2, position[1]+2)
    draw.text(shadow_position, text, fill=(180, 180, 180), font=font)
    draw.text(position, text, fill=(80, 80, 80), font=font)
    
    return img

def create_preview(parent_frame, file_path):
    """
    Create a preview of a file and place it in the parent frame.
    
    Args:
        parent_frame (ttk.Frame): Frame to place the preview in
        file_path (str): Path to the file to preview
        
    Returns:
        bool: True if preview was created, False otherwise
    """
    try:
        if not os.path.exists(file_path):
            show_error_message(parent_frame, "File not found")
            return False
            
        # Get file extension (lowercase)
        _, file_ext = os.path.splitext(file_path.lower())
        
        # Check if file type is supported
        if not is_previewable_file(file_path):
            label = ttk.Label(parent_frame, text="Preview not supported for this file type.")
            label.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
            return False
            
        # Handle different file types
        if file_ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tif', '.tiff', '.ico', '.webp']:
            return create_image_preview(parent_frame, file_path)
            
        elif file_ext == '.svg':
            return create_svg_preview(parent_frame, file_path)
            
        elif file_ext == '.pdf':
            return create_pdf_preview(parent_frame, file_path)
            
        elif file_ext in ['.eps', '.ai']:
            return create_eps_preview(parent_frame, file_path)
            
        elif file_ext == '.psd':
            return create_psd_preview(parent_frame, file_path)
            
        else:
            # Unsupported file type
            label = ttk.Label(parent_frame, text="Preview not supported for this file type.")
            label.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
            return False
            
    except Exception as e:
        logging.error(f"Error creating preview for {file_path}: {e}")
        show_error_message(parent_frame, f"Error creating preview: {str(e)}")
        return False

def create_image_preview(parent_frame, file_path):
    """
    Create an image preview.
    
    Args:
        parent_frame (ttk.Frame): Frame to place the preview in
        file_path (str): Path to the image file
        
    Returns:
        bool: True if preview was created, False otherwise
    """
    try:
        # Create a canvas for the image
        canvas_frame = ttk.Frame(parent_frame)
        canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add scrollbars
        h_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL)
        v_scrollbar = ttk.Scrollbar(canvas_frame, orient=tk.VERTICAL)
        
        preview_canvas = tk.Canvas(
            canvas_frame,
            xscrollcommand=h_scrollbar.set,
            yscrollcommand=v_scrollbar.set
        )
        
        h_scrollbar.config(command=preview_canvas.xview)
        v_scrollbar.config(command=preview_canvas.yview)
        
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        preview_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Load the image
        with Image.open(file_path) as img:
            # Store reference to avoid garbage collection
            parent_frame.image = ImageTk.PhotoImage(img)
            
            # Adjust scrollregion to image size
            preview_canvas.create_image(0, 0, image=parent_frame.image, anchor=tk.NW)
            preview_canvas.config(scrollregion=preview_canvas.bbox(tk.ALL))
            
            # Add zoom controls
            zoom_frame = ttk.Frame(parent_frame)
            zoom_frame.pack(fill=tk.X, pady=5)
            
            zoom_out_btn = ttk.Button(
                zoom_frame, 
                text="Zoom Out", 
                command=lambda: zoom_image(preview_canvas, img, 0.8)
            )
            zoom_out_btn.pack(side=tk.LEFT, padx=5)
            
            zoom_in_btn = ttk.Button(
                zoom_frame, 
                text="Zoom In", 
                command=lambda: zoom_image(preview_canvas, img, 1.2)
            )
            zoom_in_btn.pack(side=tk.LEFT, padx=5)
            
            # Add image info
            info_label = ttk.Label(
                parent_frame,
                text=f"Dimensions: {img.width} × {img.height} pixels | Format: {img.format} | Mode: {img.mode}"
            )
            info_label.pack(fill=tk.X, pady=5)
            
            return True
            
    except Exception as e:
        logging.error(f"Error creating image preview for {file_path}: {e}")
        show_error_message(parent_frame, f"Error creating image preview: {str(e)}")
        return False

def zoom_image(canvas, original_img, factor):
    """
    Zoom an image on a canvas.
    
    Args:
        canvas (tk.Canvas): Canvas containing the image
        original_img (PIL.Image): Original image
        factor (float): Zoom factor (> 1 for zoom in, < 1 for zoom out)
    """
    # Get current image size from canvas
    current_width = canvas.winfo_width()
    
    # Calculate new size
    new_width = int(current_width * factor)
    
    # Resize the image
    resized_img = original_img.copy()
    
    # Maintain aspect ratio
    aspect_ratio = original_img.height / original_img.width
    new_height = int(new_width * aspect_ratio)
    
    # Resize image
    resized_img = resized_img.resize((new_width, new_height), get_pil_resize_method())
    
    # Update canvas
    canvas.delete("all")
    canvas.image = ImageTk.PhotoImage(resized_img)
    canvas.create_image(0, 0, image=canvas.image, anchor=tk.NW)
    canvas.config(scrollregion=canvas.bbox(tk.ALL))

def create_svg_preview(parent_frame, file_path):
    """
    Create an SVG preview.
    
    Args:
        parent_frame (ttk.Frame): Frame to place the preview in
        file_path (str): Path to the SVG file
        
    Returns:
        bool: True if preview was created, False otherwise
    """
    try:
        # Try to convert SVG to PNG using cairosvg if available
        try:
            from cairosvg import svg2png
            
            # Create a temporary PNG file
            with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
                tmp_path = tmp_file.name
            
            # Convert SVG to PNG
            svg2png(url=file_path, write_to=tmp_path, output_width=800)
            
            # Create image preview from the converted PNG
            result = create_image_preview(parent_frame, tmp_path)
            
            # Clean up the temporary file
            try:
                os.unlink(tmp_path)
            except:
                pass
                
            return result
            
        except ImportError:
            # If cairosvg is not available, show a message
            label = ttk.Label(
                parent_frame,
                text="SVG preview requires additional libraries.\n\nPlease install cairosvg for SVG preview support."
            )
            label.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
            return False
            
    except Exception as e:
        logging.error(f"Error creating SVG preview for {file_path}: {e}")
        show_error_message(parent_frame, f"Error creating SVG preview: {str(e)}")
        return False

def create_pdf_preview(parent_frame, file_path):
    """
    Create a PDF preview with page navigation.
    
    Args:
        parent_frame (ttk.Frame): Frame to place the preview in
        file_path (str): Path to the PDF file
        
    Returns:
        bool: True if preview was created, False otherwise
    """
    try:
        # Load the PDF document
        pdf_document = fitz.open(file_path)
        
        # If PDF has no pages, show an error
        if pdf_document.page_count == 0:
            show_error_message(parent_frame, "The PDF file has no pages.")
            pdf_document.close()
            return False
        
        # Create a frame for the PDF viewer
        pdf_frame = ttk.Frame(parent_frame)
        pdf_frame.pack(fill=tk.BOTH, expand=True)
        
        # Add a canvas with scrollbars
        h_scrollbar = ttk.Scrollbar(pdf_frame, orient=tk.HORIZONTAL)
        v_scrollbar = ttk.Scrollbar(pdf_frame, orient=tk.VERTICAL)
        
        preview_canvas = tk.Canvas(
            pdf_frame,
            xscrollcommand=h_scrollbar.set,
            yscrollcommand=v_scrollbar.set
        )
        
        h_scrollbar.config(command=preview_canvas.xview)
        v_scrollbar.config(command=preview_canvas.yview)
        
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        preview_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Create navigation controls
        control_frame = ttk.Frame(parent_frame)
        control_frame.pack(fill=tk.X, pady=5)
        
        # Add page navigation
        current_page = tk.IntVar(value=1)
        
        def update_page_display():
            page_label.config(text=f"Page {current_page.get()} of {pdf_document.page_count}")
            
        def render_page():
            # Clear canvas
            preview_canvas.delete("all")
            
            # Get the page
            page_index = current_page.get() - 1
            page = pdf_document[page_index]
            
            # Render the page at higher resolution
            pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
            
            # Convert to PIL Image
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # Store reference to avoid garbage collection
            pdf_frame.current_image = ImageTk.PhotoImage(img)
            
            # Display on canvas
            preview_canvas.create_image(0, 0, image=pdf_frame.current_image, anchor=tk.NW)
            preview_canvas.config(scrollregion=preview_canvas.bbox(tk.ALL))
            
            # Update page display
            update_page_display()
            
        def prev_page():
            if current_page.get() > 1:
                current_page.set(current_page.get() - 1)
                render_page()
                
        def next_page():
            if current_page.get() < pdf_document.page_count:
                current_page.set(current_page.get() + 1)
                render_page()
        
        # Create control buttons
        prev_btn = ttk.Button(control_frame, text="◀ Previous", command=prev_page)
        prev_btn.pack(side=tk.LEFT, padx=5)
        
        page_label = ttk.Label(control_frame, text=f"Page {current_page.get()} of {pdf_document.page_count}")
        page_label.pack(side=tk.LEFT, padx=5)
        
        next_btn = ttk.Button(control_frame, text="Next ▶", command=next_page)
        next_btn.pack(side=tk.LEFT, padx=5)
        
        # Add zoom controls
        zoom_out_btn = ttk.Button(
            control_frame, 
            text="🔍-", 
            command=lambda: zoom_pdf(0.8)
        )
        zoom_out_btn.pack(side=tk.RIGHT, padx=5)
        
        zoom_in_btn = ttk.Button(
            control_frame, 
            text="🔍+", 
            command=lambda: zoom_pdf(1.2)
        )
        zoom_in_btn.pack(side=tk.RIGHT, padx=5)
        
        # Zoom function
        current_zoom = [1.0]  # Use list to allow modification inside nested function
        
        def zoom_pdf(factor):
            current_zoom[0] *= factor
            render_page_with_zoom()
            
        def render_page_with_zoom():
            # Clear canvas
            preview_canvas.delete("all")
            
            # Get the page
            page_index = current_page.get() - 1
            page = pdf_document[page_index]
            
            # Render the page with zoom
            zoom_matrix = fitz.Matrix(2 * current_zoom[0], 2 * current_zoom[0])
            pix = page.get_pixmap(matrix=zoom_matrix)
            
            # Convert to PIL Image
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            
            # Store reference to avoid garbage collection
            pdf_frame.current_image = ImageTk.PhotoImage(img)
            
            # Display on canvas
            preview_canvas.create_image(0, 0, image=pdf_frame.current_image, anchor=tk.NW)
            preview_canvas.config(scrollregion=preview_canvas.bbox(tk.ALL))
        
        # Add cleanup handler
        def cleanup():
            # Close the PDF document when the preview is closed
            pdf_document.close()
        
        parent_frame.bind("<Destroy>", lambda e: cleanup())
        
        # Render the first page
        render_page()
        
        return True
        
    except Exception as e:
        logging.error(f"Error creating PDF preview for {file_path}: {e}")
        show_error_message(parent_frame, f"Error creating PDF preview: {str(e)}")
        return False

def create_eps_preview(parent_frame, file_path):
    """
    Create an EPS/AI preview.
    
    Args:
        parent_frame (ttk.Frame): Frame to place the preview in
        file_path (str): Path to the EPS/AI file
        
    Returns:
        bool: True if preview was created, False otherwise
    """
    try:
        # Try to render using PIL
        try:
            with Image.open(file_path) as img:
                # Create image preview
                return create_image_preview(parent_frame, file_path)
        except Exception as e:
            logging.error(f"Error rendering EPS/AI with PIL: {e}")
            
            # If PIL fails, try using Ghostscript directly if available
            try:
                # Create a temporary PNG file
                with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
                    tmp_path = tmp_file.name
                
                # Use ghostscript to convert EPS to PNG
                import subprocess
                
                # Check operating system for the correct ghostscript command
                if platform.system() == 'Windows':
                    gs_cmd = 'gswin64c'  # or 'gswin32c' for 32-bit
                else:
                    gs_cmd = 'gs'
                
                # Run ghostscript
                subprocess.run([
                    gs_cmd,
                    '-dSAFER',
                    '-dBATCH',
                    '-dNOPAUSE',
                    '-sDEVICE=pngalpha',
                    '-r300',
                    f'-sOutputFile={tmp_path}',
                    file_path
                ], check=True)
                
                # Create image preview from the converted PNG
                result = create_image_preview(parent_frame, tmp_path)
                
                # Clean up the temporary file
                try:
                    os.unlink(tmp_path)
                except:
                    pass
                    
                return result
                
            except Exception as e:
                logging.error(f"Error converting EPS/AI with Ghostscript: {e}")
                
                # If all methods fail, show a message
                label = ttk.Label(
                    parent_frame,
                    text="EPS/AI preview requires Ghostscript to be installed.\n\nPlease install Ghostscript for better preview support."
                )
                label.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
                return False
                
    except Exception as e:
        logging.error(f"Error creating EPS/AI preview for {file_path}: {e}")
        show_error_message(parent_frame, f"Error creating EPS/AI preview: {str(e)}")
        return False

def create_psd_preview(parent_frame, file_path):
    """
    Create a PSD preview.
    
    Args:
        parent_frame (ttk.Frame): Frame to place the preview in
        file_path (str): Path to the PSD file
        
    Returns:
        bool: True if preview was created, False otherwise
    """
    try:
        # Try to render PSD using PIL
        try:
            with Image.open(file_path) as img:
                # Create image preview
                return create_image_preview(parent_frame, file_path)
        except Exception as e:
            logging.error(f"Error rendering PSD with PIL: {e}")
            
            # If PIL fails, show a message
            label = ttk.Label(
                parent_frame,
                text="PSD preview requires additional libraries.\n\nPlease ensure PIL has PSD support."
            )
            label.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)
            return False
            
    except Exception as e:
        logging.error(f"Error creating PSD preview for {file_path}: {e}")
        show_error_message(parent_frame, f"Error creating PSD preview: {str(e)}")
        return False

def show_error_message(parent_frame, message):
    """
    Show an error message in the parent frame.
    
    Args:
        parent_frame (ttk.Frame): Frame to place the error message in
        message (str): Error message to display
    """
    # Create error label
    error_frame = ttk.Frame(parent_frame)
    error_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    error_label = ttk.Label(
        error_frame,
        text=f"Error: {message}",
        foreground="red"
    )
    error_label.pack(pady=10)
