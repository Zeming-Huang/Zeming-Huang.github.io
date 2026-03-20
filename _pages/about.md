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

<!--
TODO: You mainly edit this file (`_pages/about.md`).
If you haven't published yet, it's totally fine to keep the Publications section as "coming soon".
-->

<span class='anchor' id='about'></span>

My research interests focus on machine learning and its corresponding applications, such as AI for health and audio processing. I enjoy exploring new areas and learning new things, both in research and in life.

Currently, I am working on medical imaging of the prostate and intelligent diagnosis of electrocardiogram (ECG), including latent-space modeling of ECG signals.

<!--
TODO(optional): Google Scholar link + citation badge
Replace YOUR_GOOGLE_SCHOLAR_ID below when you have one.
-->
<!--
I have a <a href='https://scholar.google.com/citations?user=YOUR_GOOGLE_SCHOLAR_ID'>Google Scholar profile</a>
(badge: <a href='https://scholar.google.com/citations?user=YOUR_GOOGLE_SCHOLAR_ID'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).
-->

<span class='anchor' id='news'></span>

# News
- *2025.08*: Started a new project on ECG representation learning and latent feature mining.
- *2024.09*: Started research on prostate cancer imaging segmentation (ultrasound with privileged MRI information).
- *2024.09*: Started M.Eng. at University of Chinese Academy of Sciences (UCAS), Beijing.
- *2024.06*: Received B.Eng. from Sun Yat-sen University (SYSU), Guangzhou.
- *2023.08 - 2023.09*: Internship at South China Sea Survey Center, Ministry of Natural Resources.

<span class='anchor' id='projects'></span>

# Projects
- *2025.08 - Present*: **ECG Latent Feature Mining** — preprocessing ECG signals and exploring early model designs to improve prediction and interpretability.
- *2024.09 - 2025.10*: **Prostate Cancer Imaging Segmentation** — ultrasound enhancement/segmentation with privileged MRI information during training; ultrasound-only inference (manuscript in preparation).
- *2023.01 - 2023.12*: **AUV Formation Obstacle Avoidance (MADDPG)** — combined leader–follower formation with LOS guidance; built ROS + PyTorch environments; achieved stable obstacle-avoidance trajectories in simulation.
- *2022.01 - 2022.12*: **Tracked ROV Design** — 3D modeling (SolidWorks), dynamics simulation, 3D printing & assembly, Arduino-based control, and water testing.
- *2023.05 - 2024.07*: **National Marine Vehicle Design & Production Contest (Team Member)** — participated in AUV modification and underwater tests; served as presenter in competition and defense.

<span class='anchor' id='publications'></span>

# Publications
<!-- TODO: Add your papers here when available. -->
Coming soon.

<span class='anchor' id='honors'></span>

# Honors and Awards
- *2021*: Outstanding Prize, SYSU Experimental Skills Competition.
- *2021*: Excellent Member, SYSU Admissions Publicity Association.
- *2024*: Third Prize (South China Division), 12th National Marine Vehicle Design & Production Contest.

<span class='anchor' id='education'></span>

# Education
- *2024.09 - Present*, Master of Engineering (Electronic, Electrical and Communication Engineering), University of Chinese Academy of Sciences, Beijing, China.
- *2020.09 - 2024.06*, Bachelor of Engineering (Ocean Engineering and Technology), Sun Yat-sen University, Guangzhou, Guangdong, China.

<span class='anchor' id='internships'></span>

# Internships
- *2023.08 - 2023.09*, South China Sea Survey Center, Ministry of Natural Resources — assisted buoy operations (deployment/recovery of GPS & CTD sensors) and processed/uploaded received data.

# Activities
- *2020 - 2022*, SYSU Admissions Publicity Association — Finance Department member; regional lead (Luohe) for winter outreach.
