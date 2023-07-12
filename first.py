



####By Mustafa Alsalmi,Thuraya Alsalmi, Siham Alkalbani, Hana Alyaqoobi ###


import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, messagebox

class CardiacAnalyzer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EVCardiovascular Analyzer")
        self.geometry("700x700")


        #widgets
        self.lb3_devs = tk.Label(self, text="Developed by: Mustafa Alsalmi,Siham Alkalnani ,Thuraya Alsalmi, Hana Alyaqoobi", font=("Nexa", 12),highlightbackground='coral',highlightcolor='yellow',highlightthickness=2,bg='AntiqueWhite2')
        self.btn_browse = tk.Button(self, text="Browse", command=self.browse_image,font=("Nexa", 12),bg='AntiqueWhite2')
        self.lbl_image = tk.Label(self, text="No image selected", font=("Arial", 12),bg='cornsilk')
        self.btn_analyze = tk.Button(self, text="Analyze", command=self.analyze_image,font=("Nexa", 12),bg='AntiqueWhite2')
        self.lbl_result_ef = tk.Label(self, text="Ejection Fraction: ", font=("Arial", 12))
        self.lbl_result_vv = tk.Label(self, text="Ventricular Volume: ", font=("Arial", 12))
        self.result_ef = tk.Label(self, text="MUSTAFA Fraction: ", font=("Arial", 12))
        #widgets to layout
        self.lb3_devs.pack(pady=5)
        self.btn_browse.pack(pady=10)
        self.lbl_image.pack(pady=10)
        self.btn_analyze.pack(pady=10)
        self.lbl_result_ef.pack(pady=10)
        self.lbl_result_vv.pack(pady=10)







        #Initialize variables
        self.image_path = None
        self.ejection_fraction = None
        self.ventricular_volume = None

    def browse_image(self):
        # Open file dialog to select an image
        self.image_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg *.jpeg *.png")])

        if self.image_path:
            self.lbl_image.config(text=self.image_path)

    def analyze_image(self):
        if self.image_path:
            # Load the image  ---not sure about it---
            img = cv2.imread(self.image_path)

            # Then we convert the image to grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Apply thresholding to binarize the image
            _, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

            # Find contours in the binary image
            contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            # Find the contour with the largest area- here I prefer we subtract highest from lowest
            largest_contour = max(contours, key=cv2.contourArea)

            # Compute the area and perimeter of the contour #need more loop#
            area = cv2.contourArea(largest_contour)
            perimeter = cv2.arcLength(largest_contour, True)

            # Compute the cardiac ejection fraction and ventricular both without any loop#



            self.ejection_fraction = (area / (perimeter**2)) * 1000
            self.ventricular_volume = (area**1.2) / perimeter

            # Update result labels
            self.lbl_result_ef.config(text="Ejection Fraction: {:.2f}%".format(self.ejection_fraction))
            self.lbl_result_vv.config(text="Ventricular Volume: {:.2f}".format(self.ventricular_volume))
        else:
            tk.messagebox.showwarning("No Image", "Please select an image first.")

if __name__ == "__main__":
    app = CardiacAnalyzer()
    app.mainloop()
