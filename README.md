
# Color Space Transformations and Pseudo Coloring

## 📌 Project Overview
This repository demonstrates fundamental **Color Image Processing Techniques** using **Python** and **OpenCV**.  
The project focuses on color space manipulation, pseudo coloring, and color channel extraction techniques commonly used in Digital Image Processing (DIP) and Computer Vision applications.

The implemented topics include:

- Pseudo Coloring
- Color Extraction
- RGB to CMY Conversion
- CMY to RGB Conversion

These techniques are important in:
- Image Visualization
- Medical Imaging
- Satellite Imaging
- Object Recognition
- Computer Vision Systems

---

# 🧠 Objectives
The main objectives of this repository are:

- To understand color space transformations
- To implement pseudo coloring techniques
- To perform color channel extraction
- To explore RGB and CMY color models
- To strengthen practical concepts of Digital Image Processing

---

# 🛠️ Technologies Used

- Python 3
- OpenCV
- NumPy

---

# 📂 Project Structure

```bash
Color-Space-Transformations-and-Pseudo-Coloring/
│
├── Pseudo-Coloring/
│   ├── pseudo_coloring.py
│   └── input.jpg
│
├── Color-Extraction/
│   ├── color_extraction.py
│   └── input.jpg
│
├── RGB-to-CMY/
│   ├── rgb_to_cmy.py
│   └── input.jpg
│
├── CMY-to-RGB/
│   ├── cmy_to_rgb.py
│   └── input.jpg
│
└── README.md
````

---

# 🔍 Implemented Techniques

## 1️⃣ Pseudo Coloring

Pseudo coloring converts grayscale images into colored images to improve visualization and interpretation.

### ✔️ Process

* Read grayscale image
* Apply OpenCV color map
* Display enhanced pseudo-colored output

### ✔️ Applications

* Medical image analysis
* Heatmap visualization
* Satellite image enhancement
* Scientific imaging

---

## 2️⃣ Color Extraction

Color extraction isolates a specific color channel from an image.

### ✔️ Process

* Split RGB channels
* Keep required color channel
* Merge extracted channel for visualization

### ✔️ Applications

* Object tracking
* Image segmentation
* Color-based detection systems
* Computer vision applications

---

## 3️⃣ RGB to CMY Conversion

RGB images are converted into the CMY color model using color inversion.

### ✔️ Process

* Read RGB image
* Apply inverse transformation:

```math id="q0btxj"
CMY = 255 - RGB
```

### ✔️ Applications

* Printing systems
* Image preprocessing
* Graphic design workflows

---

## 4️⃣ CMY to RGB Conversion

CMY images are converted back into RGB format using inverse operations.

### ✔️ Process

* Read CMY image
* Apply inverse transformation:

```math id="tdw9dx"
RGB = 255 - CMY
```

### ✔️ Applications

* Digital displays
* Color correction
* Image restoration

---

# ▶️ How to Run the Project

## Step 1: Clone Repository

```bash id="e0ocxt"
git clone https://github.com/your-username/Color-Space-Transformations-and-Pseudo-Coloring.git
```

## Step 2: Install Required Libraries

```bash id="pf8yhg"
pip install opencv-python numpy
```

## Step 3: Run Python Files

### Pseudo Coloring

```bash id="5s2rj8"
python pseudo_coloring.py
```

### Color Extraction

```bash id="6c7nrd"
python color_extraction.py
```

### RGB to CMY

```bash id="8vwr2d"
python rgb_to_cmy.py
```

### CMY to RGB

```bash id="j9t7zv"
python cmy_to_rgb.py
```

---

# 📸 Output Visualization

The project displays:

* Original images
* Converted color models
* Extracted color channels
* Pseudo-colored outputs

using OpenCV visualization windows.

---

# 🎯 Learning Outcomes

Through this project, the following concepts were learned:

* Color space conversion
* RGB and CMY color models
* Color channel manipulation
* Pseudo coloring techniques
* OpenCV image visualization
* Practical DIP implementation

---

# 🚀 Future Improvements

Possible future enhancements include:

* HSV color space implementation
* Real-time webcam color detection
* GUI-based color manipulation tool
* Advanced image enhancement techniques
* Interactive color analysis system

---

# 👨‍💻 Author

**Ghayoor Khan**
Computer Science Student | Digital Image Processing Enthusiast | Computer Vision Learner

---

# ⭐ Repository Purpose

This repository was developed as part of academic learning in the subject of **Digital Image Processing (DIP)** to strengthen practical understanding of color image processing and color space transformation techniques.

---

# 📜 License

This project is developed for educational and research purposes.
