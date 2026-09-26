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

<aside class="phd-opportunity" aria-labelledby="phd-opportunity-title">
  <h2 id="phd-opportunity-title">Seeking PhD Opportunities · Fall 2027</h2>
  <p>I am seeking PhD opportunities in <strong>AI for Health</strong>, including medical image analysis, physiological signal modeling, and multimodal learning. I have a particular interest in cardiovascular applications.</p>
  <p>I would welcome the opportunity to discuss potential research fit. <a href="mailto:huangzeming24@mails.ucas.ac.cn">Get in touch</a>.</p>
</aside>

I am a master's student in Electronic Information at the University of Chinese Academy of Sciences, working on AI for Health with a particular interest in cardiovascular AI. My research focuses on learning reliable representations from complex, noisy, heterogeneous, and incomplete biomedical data, and developing methods that are useful in real clinical settings.

I work on medical imaging and physiological signals, including prostate ultrasound segmentation and measurement, longitudinal ECG forecasting, and paroxysmal atrial fibrillation episode localization. Across these projects, I aim to connect robust learning with clinical needs, meaningful validation, and practical deployment. My engineering background in signal processing, physical modeling, and hands-on system building shapes how I approach these problems.

<span class="anchor" id="publications"></span>

# Publications and Manuscripts

{% include manuscript-cards.html %}

<span class="anchor" id="experiences"></span>

# Research and Engineering Experience
- *2025.08 -- Present*, **Individualized ECG Waveform Forecasting** - University of Chinese Academy of Sciences; clinical collaborators: **Fuwai Hospital and Aerospace Center Hospital, Beijing**. Built preprocessing and representation-learning pipelines for over one million public ECG records and over 100,000 hospital recordings; contributed to waveform evaluation and follow-up analysis across two longitudinal forecasting studies, including a clinical subset of 959 participants; contributed to NSFC General Program and Beijing Natural Science Foundation proposal preparation.
- *2026.04 -- 2026.09*, **NOR-TL: Paroxysmal AF Episode Localization** - University of Chinese Academy of Sciences; clinical collaborators: **Fuwai Hospital and Aerospace Center Hospital, Beijing**. Developed a dual-stream framework to address scarce time-point rhythm annotations, combining normal-reference and AF-specific ECG representations. Designed separate supervision for recording-level detection and temporal localization to use coarse and dense labels without treating them as interchangeable. Evaluated on AFDB and external LTAFDB and CPSC2021 cohorts with patient- or recording-disjoint partitions, achieving 97.98% temporal AUROC and 0.838 MCC on 1,425 CPSC2021 recordings. First-author manuscript submitted to ICASSP 2027.
- *2024.09 -- Present*, **Privileged Learning for Prostate Ultrasound Segmentation and Measurement** - developed PRISM and MIRAUS to use MRI-derived information during training while retaining TRUS-only inference; evaluated patient-disjoint segmentation, external generalization, and model-derived calipers for conventional ellipsoid volume estimation; contributed to manuscript writing and grant proposal preparation for a NSFC Regional Science Fund project.
- *2025.04 -- Present*, **Biomechanical Simulation and Physical Orthopedic Modeling** - constructed an ANSYS model of humeral motion using physiological movement constraints; compared simulated kinematics and force responses with collaborator measurements; designed and built a physical orthopedic model to reproduce humeral motion for bench-scale validation. Co-authored **BioShoulder**, a dataset of simulated shoulder muscle activations, as part of this broader shoulder-biomechanics collaboration (third author).
- *2024*, **Deep Learning-Based Underwater Acoustic Channel Estimation** - investigated deep learning methods for underwater acoustic channel estimation in noisy and time-varying conditions, with a focus on signal processing and experimental evaluation.
- *2023.08 -- 2023.09*, **South China Sea Survey Center, Ministry of Natural Resources of the People's Republic of China** - assisted buoy operations, including GPS and CTD sensor deployment and recovery, data reception, and cloud-based data uploading.
- *2023 -- 2024*, **National Marine Vehicle Design and Manufacturing Competition** - participated in AUV modification, underwater testing, troubleshooting, and competition presentation; received Third Prize in the South China regional contest.
- *2022*, **Tracked ROV Mechanical Design** - led the design of a tracked remotely operated vehicle; completed 3D modeling, motion simulation, and prototype fabrication using SolidWorks, COMSOL, CATIA, and 3D printing.

<span class="anchor" id="education"></span>

# Education
- *2024.09 -- Present*, Master's studies in Electronic Information, **University of Chinese Academy of Sciences**, Beijing, China. Research university of China's national academy of sciences; ranked **54th globally and 5th in China** ([U.S. News Best Global Universities, 2025–2026](https://www.usnews.com/education/best-global-universities/university-of-chinese-academy-of-sciences-529679)).
- *2020.09 -- 2024.06*, Bachelor of Engineering in Marine Engineering and Technology, **Sun Yat-sen University**, Guangdong, China. National research university under China's Ministry of Education; ranked **85th globally and 8th in China** ([U.S. News Best Global Universities, 2025–2026](https://www.usnews.com/education/best-global-universities/sun-yat-sen-university-506062)).

<span class="anchor" id="honors"></span>

# Honors and Awards
- *2026*: Second-Class Academic Scholarship, University of Chinese Academy of Sciences.
- *2026*: Merit Student, University of Chinese Academy of Sciences.
- *2024*: Third Prize, South China Regional Contest, 12th National Marine Vehicle Design and Manufacturing Competition.
- *2021*: Merit Award, Sun Yat-sen University Experimental Skills Competition.
- *2021*: Outstanding Team Member, Sun Yat-sen University Admissions Outreach Association.

<span class="anchor" id="skills"></span>

# Skills
- Programming: Python, MATLAB
- Research: Deep learning, ECG signal processing, time-series modeling, medical image analysis
- Engineering: SolidWorks, AutoCAD, CATIA, COMSOL, Arduino, 3D printing
- Languages: Mandarin Chinese (Native); English (CET-6, Intermediate)
