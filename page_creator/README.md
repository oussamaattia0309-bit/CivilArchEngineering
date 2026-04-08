# Project HTML Generator - User Guide

## Overview

The Project HTML Generator is a Python script that helps you create professional HTML content for showcasing construction and renovation projects with "Before and After" comparisons. It generates responsive Bootstrap-based HTML with image carousels.

## Prerequisites

- Python 3.x installed on your system
- Basic understanding of file paths and folders

## How It Works

The script (`main.py`) generates HTML code that displays:
- Project title and description
- Two side-by-side carousels showing "Before" and "After" images
- Responsive layout that works on all screen sizes
- Auto-rotating images (3-second intervals)

## Required Files

For each project, create a folder containing these files:

### Image Files (Required)
- `old1.jpg` - First "Before" image
- `old2.jpg` - Second "Before" image
- `new1.jpg` - First "After" image
- `new2.jpg` - Second "After" image

**Note:** Images should be in JPG format. If you have PNG images, convert them to JPG first.

### Description File (Required)
- `description.txt` - Text file containing:
  - **Line 1**: Project title
  - **Lines 2+**: Project description (can be multiple lines)

Example `description.txt`:
```
Modern Kitchen Renovation
Complete transformation of a traditional kitchen into a modern space with new cabinets, countertops, and appliances. The project included electrical upgrades and plumbing work.
```

## Folder Structure

Your project folder should be organized like this:

```
Images/
└── Construction/
    └── ProjectName/
        ├── old1.jpg
        ├── old2.jpg
        ├── new1.jpg
        ├── new2.jpg
        └── description.txt
```

## How to Use

### Step 1: Prepare Your Project Folder
1. Create a folder for your project inside `Images/Construction/`
2. Add all required files (4 images + description.txt)
3. Ensure all files are named exactly as specified

### Step 2: Run the Script
Open a command prompt or terminal and navigate to the `page_creator` directory:

```bash
cd path/to/CivilArchEngineering-main/page_creator
```

Run the script:

```bash
python main.py
```

### Step 3: Follow the Prompts

#### 1. Enter Project Folder Path
The script will ask:
```
📁 Enter the project folder path:
```

Enter the full path to your project folder. For example:
- Windows: `C:\Users\USER\Desktop\stuff\web\CivilArchEngineering-main\Images\Construction\MyProject`
- Mac/Linux: `/Users/USER/Desktop/stuff/web/CivilArchEngineering-main/Images/Construction/MyProject`

**Tips:**
- You can copy the path from File Explorer/Finder
- The script automatically removes quotes from the path
- If the folder doesn't exist, you'll be asked to try again

#### 2. Choose Text Position
The script will ask:
```
TEXT POSITION:
  1. Left (text on left, images on right)
  2. Right (text on right, images on left)

Choose position (1 or 2):
```

Enter `1` for left-aligned text or `2` for right-aligned text.

#### 3. Choose Image Orientation
The script will ask:
```
IMAGE ORIENTATION:
  1. Square (1:1)
  2. Portrait (9:16) - like phone portrait mode
  3. Landscape (16:9) - like TV/phone landscape mode

Choose orientation (1, 2, or 3):
```

Choose the option that best matches your images:
- **Option 1**: Square images (same width and height)
- **Option 2**: Portrait/tall images (like phone photos)
- **Option 3**: Landscape/wide images (like TV screens)

### Step 4: Get Your HTML

After processing, the script will:
1. Create a file named `project.html` in your project folder
2. Display a success message with the file path
3. Show a preview of the generated HTML

Example output:
```
✅ SUCCESS! HTML saved to: C:\...\ProjectName\project.html

============================================================
📋 PREVIEW (first 300 characters):
============================================================
<!-- ===== PROJECT: ProjectName ===== -->
<div class="row g-5 mb-5 align-items-center">
  <div class="col-lg-5">
    <h4 class="fw-bold mb-3">Modern Kitchen Renovation</h4>
    <p class="text-muted">Complete transformation...</p>
  </div>
  <div class="col-lg-7">
    <div class="row g-3">
      <!-- Before Carousel -->
      <div class="col-6 col-md-6">
...
============================================================
```

## Using the Generated HTML

### Option 1: Copy to Your Website
1. Open `project.html` in a text editor
2. Copy the HTML content
3. Paste it into your website where you want to display the project

### Option 2: Include in Existing Page
If you're using this with the CivilArchEngineering website:
1. The generated HTML is designed to work with Bootstrap 5
2. It uses the existing CSS classes from your website
3. Simply paste the HTML into your projects section

## Customization Options

### Text Position
- **Left**: Good for starting a new section or when you want text first
- **Right**: Good for alternating layouts in a list of projects

### Image Orientation
The script automatically sets the aspect ratio based on your choice:
- Square: `aspect-ratio: 1/1`
- Portrait: `aspect-ratio: 9/16`
- Landscape: `aspect-ratio: 16/9`

This ensures your images display correctly without distortion.

## Common Issues and Solutions

### Issue: "Folder not found" error
**Solution:** 
- Check that the path is correct
- Make sure you're using forward slashes (/) or double backslashes (\\) on Windows
- Verify the folder exists in File Explorer/Finder

### Issue: "Missing files" error
**Solution:**
- Ensure all 5 required files are in the folder
- Check that filenames match exactly (case-sensitive)
- Verify files are in JPG format (not PNG)

### Issue: Images don't display correctly
**Solution:**
- Choose the correct orientation option that matches your images
- Ensure images are properly sized for web use
- Check that image paths in the generated HTML are correct

### Issue: Description doesn't appear
**Solution:**
- Make sure description.txt has content
- Ensure the first line is the title
- Check that the file is saved in UTF-8 encoding

## Best Practices

1. **Image Quality**: Use high-quality images (at least 1200px wide for best results)
2. **Image Size**: Compress images before use to improve page load speed
3. **Consistent Orientation**: Use images with the same orientation in a project
4. **Clear Descriptions**: Write concise, informative descriptions
5. **Organized Folders**: Use descriptive names for project folders

## Example Workflow

Here's a complete example of creating a project:

1. **Create folder**: `Images/Construction/KitchenRenovation2024`

2. **Add files**:
   - `old1.jpg` - Kitchen before renovation
   - `old2.jpg` - Kitchen before renovation (different angle)
   - `new1.jpg` - Kitchen after renovation
   - `new2.jpg` - Kitchen after renovation (different angle)
   - `description.txt`:
     ```
     Modern Kitchen Renovation 2024
     Complete transformation of a traditional kitchen into a modern space with new cabinets, countertops, and appliances. The project included electrical upgrades and plumbing work.
     ```

3. **Run script**: `python main.py`

4. **Enter prompts**:
   - Path: `C:\...\Images\Construction\KitchenRenovation2024`
   - Position: `1` (left)
   - Orientation: `3` (landscape)

5. **Copy HTML** from `project.html` to your website

## Technical Details

### Generated HTML Structure
The script creates Bootstrap 5 compatible HTML with:
- Responsive grid system (col-lg-5 and col-lg-7)
- Carousel components with auto-rotation
- Proper accessibility attributes
- Shadow and rounded corners for modern look

### Image Paths
Generated paths follow this pattern:
```
../Images/Construction/{folder_name}/{filename}
```

This assumes the HTML will be placed in the website root or a page one level above the Images folder.

## Support

If you encounter issues:
1. Check that all required files are present
2. Verify file names match exactly
3. Ensure Python is properly installed
4. Review the error messages for specific guidance

## Version History

- Version 1.0: Initial release with basic HTML generation
- Supports: Bootstrap 5, responsive design, multiple orientations

---

For questions or improvements, please refer to the main project documentation.
