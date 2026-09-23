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

I am a Master of Engineering student at the University of Chinese Academy of Sciences, working on AI for Health. My research focuses on learning reliable representations from complex, noisy, heterogeneous, and incomplete biomedical data, and developing methods that are useful in real clinical settings.

I work on medical imaging and physiological signals, including prostate ultrasound segmentation and measurement, longitudinal ECG forecasting, and paroxysmal atrial fibrillation episode localization. Across these projects, I aim to connect robust learning with clinical needs, meaningful validation, and practical deployment. My engineering background in signal processing, physical modeling, and hands-on system building shapes how I approach these problems.

<span class="anchor" id="publications"></span>

# Manuscripts
- **Zeming Huang**, Tao Wang, Ning Liu, Yiquan Wang, Zhicheng Hu, Lei Wang, Gong Su, Zhipei Huang, and Fei Qin. **NOR-TL: Normal-Reference Temporal Learning with Decoupled Detection and Temporal Supervision for Paroxysmal AF Episode Localization**. Manuscript. *First author.* [[PDF]]({{ '/files/papers/nor-tl.pdf' | relative_url }})
- **Zeming Huang**, Haixin Chen, Chuanzhen Cao, Tao Wang, Zhipei Huang, and Fei Qin. **MIRAUS: MRI-Informed Residual Adaptation for Single-Frame TRUS Prostate Boundary Measurement**. In preparation for submission to *Measurement*. *Co-first author (listed first).* [[PDF]]({{ '/files/papers/miraus.pdf' | relative_url }}) [[Code]](https://github.com/Zeming-Huang/MIRAUS) [[Project Page]](https://zeming-huang.github.io/MIRAUS/)
- **Zeming Huang**, Haixin Chen, Chuanzhen Cao, Tao Wang, Zhipei Huang, and Fei Qin. **PRISM: A Privileged Representation-Informed Synergistic Model for Transrectal Ultrasound-Only Prostate Segmentation**. Manuscript. *Co-first author (listed first).* [[PDF]]({{ '/files/papers/prism.pdf' | relative_url }}) [[Code]](https://github.com/Zeming-Huang/PRISM)
- Tao Wang, **Zeming Huang**, Yiquan Wang, Ning Liu, Zhicheng Hu, Lei Wang, Gong Su, Zhipei Huang, Ming Yin, and Fei Qin. **Individualized ECG Waveform Forecasting Enables Testable Predictions of Longitudinal Morphology**. Manuscript. *Second author.*
- Tao Wang, Zhicheng Hu, Gong Su, **Zeming Huang**, Zhipei Huang, Ming Yin, Chenhao Wu, Xiangao Meng, and Fei Qin. **A Cross-Temporal Latent Evolution Framework for Year-Scale ECG Waveform Forecasting from Historical Records**. *Information Sciences*, under review. *Fourth author.*
- **BioShoulder: A Large-Scale Biomechanical Dataset for Shoulder Muscle Activations**. Manuscript. *Third author.* [[PDF]]({{ '/files/papers/bioshoulder.pdf' | relative_url }})

<span class="anchor" id="experiences"></span>

# Research and Engineering Experience
- *2024.09 -- Present*, **Privileged Learning for Prostate Ultrasound Segmentation and Measurement** - developed PRISM and MIRAUS to use MRI-derived information during training while retaining TRUS-only inference; evaluated patient-disjoint segmentation, external generalization, and model-derived calipers for conventional ellipsoid volume estimation; contributed to manuscript writing and grant proposal preparation for a NSFC Regional Science Fund project.
- *2025.08 -- Present*, **Individualized ECG Waveform Forecasting** - worked on long-term ECG forecasting from baseline and historical recordings; built preprocessing and representation-learning pipelines and contributed to data curation, waveform evaluation, and longitudinal follow-up analysis; contributed to manuscript preparation and research proposals for applications to the NSFC General Program and the Beijing Natural Science Foundation.
- **NOR-TL: Paroxysmal AF Episode Localization** - developed normal-reference temporal learning with separate recording-level detection and dense temporal supervision; evaluated single-lead AF localization on AFDB and external LTAFDB and CPSC2021 cohorts, reaching 97.98% temporal AUROC and 0.838 MCC on CPSC2021.
- *2025.04 -- Present*, **Biomechanical Simulation and Physical Orthopedic Modeling** - constructed an ANSYS model of humeral motion using physiological movement constraints; compared simulated kinematics and force responses with collaborator measurements; designed and built a physical orthopedic model to reproduce humeral motion for bench-scale validation.
- *2024*, **Deep Learning-Based Underwater Acoustic Channel Estimation** - investigated deep learning methods for underwater acoustic channel estimation in noisy and time-varying conditions, with a focus on signal processing and experimental evaluation.
- *2023.08 -- 2023.09*, **South China Sea Survey Center, Ministry of Natural Resources** - assisted buoy operations, including GPS and CTD sensor deployment and recovery, data reception, and cloud-based data uploading.
- *2023 -- 2024*, **National Marine Vehicle Design and Manufacturing Competition** - participated in AUV modification, underwater testing, troubleshooting, and competition presentation; received Third Prize in the South China regional contest.
- *2022*, **Tracked ROV Mechanical Design** - led the design of a tracked remotely operated vehicle; completed 3D modeling, motion simulation, and prototype fabrication using SolidWorks, COMSOL, CATIA, and 3D printing.

<span class="anchor" id="education"></span>

# Education
- *2024.09 -- Present*, Master of Engineering in Electronic Information, University of Chinese Academy of Sciences, Beijing, China.
- *2020.09 -- 2024.06*, Bachelor of Engineering in Marine Engineering and Technology, Sun Yat-sen University, Guangdong, China.

<aside class="phd-opportunity" aria-labelledby="phd-opportunity-title">
  <h2 id="phd-opportunity-title">Seeking PhD Opportunities · Fall 2027</h2>
  <p>I am seeking PhD opportunities in Health AI, with interests in physiological signal learning, multimodal learning, and making AI more practical in real-world healthcare settings.</p>
  <p>I would welcome the opportunity to discuss potential research fit. <a href="mailto:huangzeming24@mails.ucas.ac.cn">Get in touch</a>.</p>
</aside>

<span class="anchor" id="honors"></span>

# Honors and Awards
- *2026*: Second-Class Academic Scholarship, University of Chinese Academy of Sciences.
- *2026*: Merit Student, University of Chinese Academy of Sciences.
- *2024*: Third Prize, South China Division, 12th National Marine Vehicle Design and Manufacturing Contest.
- *2021*: Outstanding Prize, SYSU Experimental Skills Competition.
- *2021*: Excellent Member, SYSU Admissions Publicity Association.

<span class="anchor" id="skills"></span>

# Skills
- Programming: Python, MATLAB
- Research: Deep learning, ECG signal processing, time-series modeling, medical image analysis
- Engineering: SolidWorks, AutoCAD, CATIA, COMSOL, Arduino, 3D printing
- Languages: Mandarin Chinese (Native); English (CET-6, Intermediate)
