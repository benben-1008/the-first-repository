Here's a `README.md` file for your Python project that uses NVIDIA Jetson to classify blood cancer types from an image and provide medical guidance. This README explains how to use the code, its features, and warnings:

---

# Blood Cancer Image Classifier using Jetson Inference

This project uses NVIDIA Jetson's `jetson-inference` framework to classify blood cell images and determine the likelihood of **benign** or **malignant leukemia** types such as:

* Benign
* \[Malignant] Pre-B
* \[Malignant] Early Pre-B
* \[Malignant] Pro-B

Based on the classification result, the script provides prevention tips or treatment information accordingly.


## 🔧 Requirements

* **Hardware**: NVIDIA Jetson device (e.g., Nano, Xavier, etc.)
* **Python**: 3.x
* **Libraries**:

  * `jetson-inference`
  * `jetson-utils`
* ONNX model file: `resnet18.onnx`
* Label file: `./dataset/labels.txt`

---

## 📁 File Structure

```
.
├── my-recognition.py                # This script (classifier and guide)
├── resnet18.onnx          # Trained model for classification
├── dataset/
│   └──val
│   └──train
│   └──test
│   └── labels.txt# Label definitions (e.g., Benign, [Malignant] Pre-B, etc.)
└── Sample/
    └── a lot of images    # Input image
```

---

## 🚀 How to Run

```bash
python3 my-recognition.py Samples/your_image.jpg 
```

* Replace `images/your_image.jpg` with the path to your blood cell image.
* You can customize the model name using `--network`, but default is `resnet-18`.

---

## 💡 Features

* **Image classification** using Jetson's optimized model.
* **Medical information output** based on classification:

  * Prevention tips for benign cases.
  * Interactive explanations of treatments for malignant leukemia subtypes:

    * Chemotherapy
    * Targeted therapy
    * Stem cell transplant
    * Clinical trials
    * Induction therapy
    * Maintenance therapy
* **Looped question interface**: User can ask about each treatment individually.

---



## ✅ Example Output

```
image is recognized as [Malignant] Pre-B (class #2) with 91.2% confidence

You are diagnosed with blood cancer, Pre-B cell acute lymphoblastic leukemia (Pre-B ALL)...

If you want, type the treatment you want to know among this list:
[Chemotherapy, Targeted therapy, Stem cell transplant, Clinical trials, Induction therapy, Maintenance therapy]
```

---
