---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class="anchor" id="about"></span>

I am a Master of Engineering student at the University of Chinese Academy of Sciences, working on medical imaging and physiological signal processing. My current focus is on robust learning from noisy data, especially for prostate ultrasound segmentation and ECG evolution forecasting.

I am interested in building models that are practical, interpretable, and useful in real clinical and engineering settings. My background also includes underwater acoustics, signal processing, and underwater vehicle design.

<span class="anchor" id="news"></span>

# News
- *2025.08*: Started work on individualized ECG evolution forecasting.
- *2024.09*: Started research on prostate ultrasound segmentation with MRI-derived privileged information.
- *2024.09*: Joined UCAS as an M.Eng. student in Electronic Information.
- *2024.06*: Received B.Eng. from Sun Yat-sen University.

<span class="anchor" id="publications"></span>

# Publications
- **Zeming Huang**, Haixin Chen, Chuanzhen Cao, Tao Wang, Zhipei Huang, and Fei Qin. **Privileged Representation Informed Synergistic Model for Enhanced Transrectal Ultrasound Prostate Segmentation**. *IEEE Transactions on Medical Imaging*, under review.
- Tao Wang, **Zeming Huang**, Zhipei Huang, Chenhao Wu, and Fei Qin. **STAGE: Single-Timepoint Age-Conditioned Gaussian Memory for Individual ECG Evolution Forecasting**. *NeurIPS*, submitted.

<span class="anchor" id="experiences"></span>

# Research and Engineering Experience
- *2024.09 -- Present*, **Privileged Learning for Prostate Ultrasound Segmentation** - developed a deep learning framework for prostate segmentation in transrectal ultrasound images using MRI-derived privileged information; contributed to manuscript writing and grant proposal preparation for a NSFC Regional Science Fund project.
- *2025.08 -- Present*, **Individualized ECG Evolution Forecasting** - worked on long-term ECG forecasting from single-timepoint recordings; implemented ECG preprocessing, representation learning, latent factor decoupling, and age-conditioned progression modeling; contributed to manuscript preparation and a NSFC General Program proposal.
- *2024*, **Deep Learning-Based Underwater Acoustic Channel Estimation** - investigated deep learning methods for underwater acoustic channel estimation in noisy and time-varying conditions, with a focus on signal processing and experimental evaluation.
- *2023.08 -- 2023.09*, **South China Sea Survey Center, Ministry of Natural Resources** - assisted buoy operations, including GPS and CTD sensor deployment and recovery, data reception, and cloud-based data uploading.
- *2023 -- 2024*, **National Marine Vehicle Design and Manufacturing Competition** - participated in AUV modification, underwater testing, troubleshooting, and competition presentation; received Third Prize in the South China regional contest.
- *2022*, **Tracked ROV Mechanical Design** - led the design of a tracked remotely operated vehicle; completed 3D modeling, motion simulation, and prototype fabrication using SolidWorks, COMSOL, CATIA, and 3D printing.

<span class="anchor" id="education"></span>

# Education
- *2024.09 -- Present*, Master of Engineering in Electronic Information, University of Chinese Academy of Sciences, Beijing, China. GPA: 3.82/4.00.
- *2020.09 -- 2024.06*, Bachelor of Engineering in Marine Engineering and Technology, Sun Yat-sen University, Guangdong, China. GPA: 3.36/4.00.

<span class="anchor" id="honors"></span>

# Honors and Awards
- *2024*: Third Prize, South China Division, 12th National Marine Vehicle Design and Manufacturing Contest.
- *2021*: Outstanding Prize, SYSU Experimental Skills Competition.
- *2021*: Excellent Member, SYSU Admissions Publicity Association.

<span class="anchor" id="skills"></span>

# Skills
- Programming: Python, MATLAB
- Research: Deep learning, ECG signal processing, time-series modeling, medical image analysis
- Engineering: SolidWorks, AutoCAD, CATIA, COMSOL, Arduino, 3D printing
- Languages: Mandarin Chinese (Native); English (CET-6, Intermediate)
