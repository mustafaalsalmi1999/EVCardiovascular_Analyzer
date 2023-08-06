---
title: 'EVCardiovascular Analyzer: A Python GUI tool for cardiovascular image analysis'
tags:
  - Python
  - GUI
  - Cardiology
  - Cardiovascular 
authors:
  - name: Mustafa Al Salmi
    orcid: 0009-0003-8909-1243
    equal-contrib: No
    affiliation: "1, 2"
    corresponding: true
  - name: Thuraya Al Salmi # Author Without ORCID and no affiliation
    equal-contrib: no 
  - name: Siham Al kalbani # Author Without ORCID and no affiliation
    equal-contrib: no
  - name: Hana Al Yaqoobi # Author Without ORCID and no affiliation
    equal-contrib: no
affiliations:
 - name: University of Nizwa, Oman
   index: 1
 - name: The ISIS Neutron and Muon Source is a pulsed neutron and muon source, UK
   index: 2
date: 06 August 2023
bibliography: paper.bib

# Optional fields if submitting to a AAS journal too, see this blog post:
# https://blog.joss.theoj.org/2018/12/a-new-collaboration-with-aas-publishing
aas-doi: 10.3847/xxxxx <- update this with the DOI from AAS once you know it.
aas-journal: Astrophysical Journal <- The name of the AAS journal.
---

# Summary

Cardiovascular diseases are a major cause of morbidity and mortality worldwide. Accurate assessment of heart function is crucial for diagnosing and managing these conditions. Cardiovascular Magnetic Resonance Imaging (CVMRI) and Computed Tomography (CT) imaging are widely used modalities for evaluating cardiac function. However, manual analysis of these images is time-consuming and subjective, leading to potential variability and errors. Therefore, there is a need for a reliable, automated, and user-friendly tool for analyzing cardiovascular images and calculating heart function parameters. The purpose of EV Cardiovascular Analyzer is to provide a Python Graphical User Interface (GUI) tool for analyzing cardiovascular MRI/CT images and calculating heart function parameters such as ejection fraction and ventricular volumes. The tool will assist clinicians and researchers in obtaining accurate and reliable measurements of cardiac function, thereby improving patient care and outcomes. The tool allow importing CVMRI and CT images in standard formats such as DICOM, JPEG, etc and, then the tool  automatically segment the heart chambers and vessels from the imported images. Finally, the tool measure heart function parameters such as ejection fraction and ventricular volumes in which the tool perform calculations based on the measured parameters to provide detailed information about cardiac function.
Ejection fraction (EF) is a measure of how well the heart pumps blood (Murphy, Ibrahim, and Januzzi 2020). It is calculated as the percentage of blood that is pumped out of the left ventricle (LV) during each contraction (Borlaug 2020). A normal EF is about 50-70%. A lower EF indicates that the heart is not pumping as well as it should, which can be a sign of heart disease(Borlaug 2020).
Ventricular volumes are the measurements of the size of the LV and right ventricle (RV) (Addetia et al. 2023). The end-diastolic volume (EDV) is the amount of blood in the LV at the end of a relaxation phase (Surkova et al. 2022). The end-systolic volume (ESV) is the amount of blood in the LV at the end of a contraction phase. A higher EDV or ESV indicates that the LV is not contracting as efficiently as it should. By analyzing cardiac MRI/CT images to measure EF and ventricular volumes, doctors can get an indication of how well the heart is functioning. This information can be used to diagnose and manage heart disease (Surkova et al. 2022).


# References
Addetia, K., Miyoshi, T., Amuthan, V., Citro, R., Daimon, M., Gutierrez Fajardo, P., Kasliwal, R. R., Kirkpatrick, J. N., Monaghan, M. J., Muraru, D., et al. (2023). Normal values of three-dimensional right ventricular size and function measurements: Results of the World Alliance Societies of Echocardiography Study. Journal of the American Society of Echocardiography 36. 
Borlaug, B.A. (2020) ‘Evaluation and management of heart failure with preserved ejection fraction’, Nature Reviews Cardiology, 17(9), pp. 559–573. doi:10.1038/s41569-020-0363-2. 
Murphy, S.P., Ibrahim, N.E. and Januzzi, J.L. (2020) ‘Heart failure with reduced ejection fraction’, JAMA, 324(5), p. 488. doi:10.1001/jama.2020.10262. 
Surkova, E., Cosyns, B., Gerber, B., Gimelli, A., La Gerche, A., and Ajmone Marsan, N. (2022). The dysfunctional right ventricle: The importance of multi-modality imaging. European Heart Journal - Cardiovascular Imaging 23, 885–897. 
