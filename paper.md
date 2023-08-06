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

EV Cardiovascular Analyzer is an open-source Python software package designed to provide a user-friendly interface for analyzing cardiovascular magnetic resonance imaging (MRI) and computed tomography (CT) images. It allows clinicians and researchers to assess heart function parameters such as ejection fraction and ventricular volumes with high accuracy and reproducibility.



# Summary

Cardiovascular diseases are a major cause of morbidity and mortality worldwide. Accurate assessment of heart function is crucial for diagnosing and managing these conditions. Cardiovascular Magnetic Resonance Imaging (CVMRI) and Computed Tomography (CT) imaging are widely used modalities for evaluating cardiac function. However, manual analysis of these images is time-consuming and subjective, leading to potential variability and errors. Therefore, there is a need for a reliable, automated, and user-friendly tool for analyzing cardiovascular images and calculating heart function parameters. The purpose of EV Cardiovascular Analyzer is to provide a Python Graphical User Interface (GUI) tool for analyzing cardiovascular MRI/CT images and calculating heart function parameters such as ejection fraction and ventricular volumes. The tool will assist clinicians and researchers in obtaining accurate and reliable measurements of cardiac function, thereby improving patient care and outcomes. The tool allow importing CVMRI and CT images in standard formats such as DICOM, JPEG, etc and, then the tool  automatically segment the heart chambers and vessels from the imported images. Finally, the tool measure heart function parameters such as ejection fraction and ventricular volumes in which the tool perform calculations based on the measured parameters to provide detailed information about cardiac function.
Ejection fraction (EF) is a measure of how well the heart pumps blood. It is calculated as the percentage of blood that is pumped out of the left ventricle (LV) during each contraction. A normal EF is about 50-70%. A lower EF indicates that the heart is not pumping as well as it should, which can be a sign of heart disease.
Ventricular volumes are the measurements of the size of the LV and right ventricle (RV). The end-diastolic volume (EDV) is the amount of blood in the LV at the end of a relaxation phase. The end-systolic volume (ESV) is the amount of blood in the LV at the end of a contraction phase. A higher EDV or ESV indicates that the LV is not contracting as efficiently as it should. By analyzing cardiac MRI/CT images to measure EF and ventricular volumes, doctors can get an indication of how well the heart is functioning. This information can be used to diagnose and manage heart disease.


# Citations

Citations to entries in paper.bib should be in
[rMarkdown](http://rmarkdown.rstudio.com/authoring_bibliographies_and_citations.html)
format.

If you want to cite a software repository URL (e.g. something on GitHub without a preferred
citation) then you can do it with the example BibTeX entry below for @fidgit.

For a quick reference, the following citation commands can be used:
- `@author:2001`  ->  "Author et al. (2001)"
- `[@author:2001]` -> "(Author et al., 2001)"
- `[@author1:2001; @author2:2001]` -> "(Author1 et al., 2001; Author2 et al., 2002)"

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }


# References
