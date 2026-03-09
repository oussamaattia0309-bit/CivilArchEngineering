import os
import sys
from pathlib import Path


def generate_project_html(project_folder, text_position, orientation):
    """
    Generate HTML for a project folder containing:
    - old1.jpg, old2.jpg
    - new1.jpg, new2.jpg
    - description.txt
    """

    # Check if folder exists
    if not os.path.exists(project_folder):
        print(f"Error: Folder '{project_folder}' not found!")
        return None

    # Check for required files
    required_files = ['old1.jpg', 'old2.jpg', 'new1.jpg', 'new2.jpg', 'description.txt']
    missing_files = []

    for file in required_files:
        if not os.path.exists(os.path.join(project_folder, file)):
            missing_files.append(file)

    if missing_files:
        print(f"Error: Missing files in {project_folder}:")
        for file in missing_files:
            print(f"  - {file}")
        return None

    # Read description.txt
    desc_file = os.path.join(project_folder, "description.txt")
    with open(desc_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        title = lines[0].strip()  # First line: title
        description = ' '.join([line.strip() for line in lines[1:]])  # Rest: description

    # Get folder name for image path
    folder_name = os.path.basename(project_folder)

    # Build the correct image path
    image_path = f"../Images/Construction/{folder_name}"

    # Determine aspect ratio class based on orientation
    if orientation == "1":  # Square
        aspect_style = "aspect-ratio: 1/1;"
    elif orientation == "2":  # Portrait (532x945 ≈ 9/16)
        aspect_style = "aspect-ratio: 9/16;"
    else:  # Landscape (945x532 ≈ 16/9)
        aspect_style = "aspect-ratio: 16/9;"

    # Generate carousel HTML (same for both left and right layouts)
    carousel_html = f"""
    <div class="row g-3">
      <!-- Before Carousel -->
      <div class="col-md-6">
        <h6 class="text-danger mb-2">Before</h6>
        <div id="beforeCarousel_{folder_name}" class="carousel slide shadow rounded-4 overflow-hidden" data-bs-ride="carousel" data-bs-interval="3000">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="{image_path}/old1.jpg" class="d-block w-100" style="{aspect_style} object-fit: cover;" alt="Before 1">
            </div>
            <div class="carousel-item">
              <img src="{image_path}/old2.jpg" class="d-block w-100" style="{aspect_style} object-fit: cover;" alt="Before 2">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#beforeCarousel_{folder_name}" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#beforeCarousel_{folder_name}" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>

      <!-- After Carousel -->
      <div class="col-md-6">
        <h6 class="text-success mb-2">After</h6>
        <div id="afterCarousel_{folder_name}" class="carousel slide shadow rounded-4 overflow-hidden" data-bs-ride="carousel" data-bs-interval="3000">
          <div class="carousel-inner">
            <div class="carousel-item active">
              <img src="{image_path}/new1.jpg" class="d-block w-100" style="{aspect_style} object-fit: cover;" alt="After 1">
            </div>
            <div class="carousel-item">
              <img src="{image_path}/new2.jpg" class="d-block w-100" style="{aspect_style} object-fit: cover;" alt="After 2">
            </div>
          </div>
          <button class="carousel-control-prev" type="button" data-bs-target="#afterCarousel_{folder_name}" data-bs-slide="prev">
            <span class="carousel-control-prev-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Previous</span>
          </button>
          <button class="carousel-control-next" type="button" data-bs-target="#afterCarousel_{folder_name}" data-bs-slide="next">
            <span class="carousel-control-next-icon" aria-hidden="true"></span>
            <span class="visually-hidden">Next</span>
          </button>
        </div>
      </div>
    </div>
"""

    # Generate text content HTML (same for both layouts)
    text_html = f"""
    <div class="col-lg-5">
      <h4 class="fw-bold mb-3">{title}</h4>
      <p class="text-muted">{description}</p>
      <div class="d-flex gap-2 mb-3">
        <span class="badge bg-secondary">Before: 2 photos</span>
        <span class="badge bg-secondary">After: 2 photos</span>
      </div>
    </div>
"""

    # Generate the full HTML based on text position
    if text_position == "left":
        html = f"""<!-- ===== PROJECT: {folder_name} ===== -->
<div class="row g-5 mb-5 align-items-center">
  {text_html}
  <div class="col-lg-7">
    {carousel_html}
  </div>
</div>
<!-- ===== END PROJECT ===== -->"""
    else:  # text_position == "right"
        html = f"""<!-- ===== PROJECT: {folder_name} ===== -->
<div class="row g-5 mb-5 align-items-center">
  <div class="col-lg-7">
    {carousel_html}
  </div>
  {text_html}
</div>
<!-- ===== END PROJECT ===== -->"""

    return html


def main():
    print("=" * 60)
    print("PROJECT HTML GENERATOR".center(60))
    print("=" * 60)

    # Ask for project folder path
    while True:
        project_folder = input("\n📁 Enter the project folder path: ").strip().strip('"').strip("'")

        if not project_folder:
            print("Please enter a folder path.")
            continue

        if os.path.exists(project_folder):
            break
        else:
            print(f"❌ Folder not found: {project_folder}")
            print("Please check the path and try again.")

    # Ask for text position
    print("\n" + "-" * 60)
    print("TEXT POSITION:")
    print("  1. Left (text on left, images on right)")
    print("  2. Right (text on right, images on left)")
    print("-" * 60)

    while True:
        position_choice = input("Choose position (1 or 2): ").strip()
        if position_choice in ["1", "2"]:
            text_position = "left" if position_choice == "1" else "right"
            break
        else:
            print("❌ Please enter 1 or 2")

    # Ask for image orientation
    print("\n" + "-" * 60)
    print("IMAGE ORIENTATION:")
    print("  1. Square (1:1)")
    print("  2. Portrait (9:16) - like phone portrait mode")
    print("  3. Landscape (16:9) - like TV/phone landscape mode")
    print("-" * 60)

    while True:
        orientation_choice = input("Choose orientation (1, 2, or 3): ").strip()
        if orientation_choice in ["1", "2", "3"]:
            orientation = orientation_choice
            break
        else:
            print("❌ Please enter 1, 2, or 3")

    print(f"\n📂 Processing folder: {project_folder}")
    print(f"📝 Text position: {text_position}")
    print(f"🖼️  Image orientation: {orientation}")

    # Generate HTML
    html_output = generate_project_html(project_folder, text_position, orientation)

    if html_output:
        # Save HTML file in the project folder
        output_file = os.path.join(project_folder, "project.html")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_output)

        print(f"\n✅ SUCCESS! HTML saved to: {output_file}")
        print("\n" + "=" * 60)
        print("📋 PREVIEW (first 300 characters):")
        print("=" * 60)
        print(html_output[:300] + "...")
        print("=" * 60)


if __name__ == "__main__":
    main()