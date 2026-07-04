# E-portfolio 3 – Robotic Process Automation and Process Cybersecurity

## Artefact 1 – YouTube Video: What is RPA? Robotic Process Automation

[![What Is RPA? | Robotic Process Automation Explained in 60 Seconds](Images/0.jpg)](https://www.youtube.com/watch?v=k_egKi8zREw)

```Inmar Intelligence, August 2025. Duration: 60 seconds. Click image to watch. ```

This one-minute video introduces Robotic Process Automation by showing software bots mimicking human interactions with computer systems to automate repetitive tasks like data entry and report generation — without requiring changes to existing IT infrastructure (Inmar Intelligence 2025).

I selected this because it directly addressed a misconception I held — that "robotic" automation meant physical machinery. Seeing bots described as working through the same user interface a human uses made the concept clearer and also it matches with the core RPA concepts from the week 8 lecture. More significantly, it made me question where human accountability sits when a bot performs a task incorrectly. This shifted how I approached the rest of the topic — not just asking what RPA does, but who is responsible when it fails.

---

## Artefact 2 – What is Process Cybersecurity?

[What is Cybersecurity? — CISA](https://www.cisa.gov/news-events/news/what-cybersecurity)
```Click the link to read```
 
This page from CISA defines cybersecurity as protecting networks, devices, and data from unauthorised access while ensuring confidentiality, integrity, and availability (CISA 2025). It identifies common threats — malware, phishing, denial of service, and insider threats — and notes that successful attacks cause operational disruption and financial loss.

I chose this artefact because it directly challenged an assumption I had never examined: that cybersecurity is an IT responsibility, separate from how business processes are designed. Reading CISA's breakdown of how phishing and denial-of-service attacks disrupt operations taught me that process cybersecurity means building protection into the process itself, not bolting it on later. Our unit defines this as the practices and strategies that protect organisational processes and systems from such threats (Humayun et al. 2020; Parker et al. 2023, p. 14). This matters to BPM because the process lifecycle — analyse, design, implement, monitor — must treat security as a design requirement at every stage. This was a genuinely surprising learning experience. Going forward, I will approach process design with security embedded from the first step.


---

## Artefact 3 – Self-Created Diagram: How RPA is Applied to Process Cybersecurity

[![How RPA and Process Cybersecurity Work Together](Images/RPA.png)](https://drive.google.com/file/d/1MFW0XjtwhBJpcw2rX5Nno8QujyYA1xWP/view?usp=sharing)

```Click the diagram to view the diagram in Draw.io```

The diagram is my own work, created to synthesise the connection between RPA and process cybersecurity. Diagram  maps three cyber threats from our lecture — phishing, malware/unpatched vulnerabilities, and insider threats — to specific RPA bot responses, then to the CIA outcome each response achieves (Humayun et al. 2020, p. 3172) and below the CIA Triad itself, showing how confidentiality, integrity, and availability are interconnected principles, not independent concepts.

This was a challenging but rewarding learning experience. Creating this took three attempts. My first version placed CIA responses beside threats — two separate ideas with no real link. My second became cluttered trying to show everything at once. The third worked only when I forced one question per row: what does the bot do, and which CIA principle does that protect? That discipline made the connection clear — a bot detecting a suspicious login and blocking access is confidentiality in action, automated. I could not have explained that from reading slides alone. As a future BPM professional, I now understand that secure process design means mapping CIA outcomes into each stage of the process lifecycle, not treating security as something added after a process is built.

---

## Artefact 4 –  Self-Created Diagram: How RPA Tackles Process Cybersecurity Risks in real life example (Agoda 2025)

[![How RPA helped Agoda in Process Cybersecurity](Images/Agoda.png)](https://drive.google.com/file/d/1MFW0XjtwhBJpcw2rX5Nno8QujyYA1xWP/view?usp=sharing)

After reading the Agoda Engineering (2025) case study — which describes how Agoda redesigned its security incident response using automated bots, reducing phishing response to under 25 seconds and report drafting from several hours to under ten minutes — I created this diagram to map how RPA addresses the three core cybersecurity risks from our lecture: phishing attacks, malware vulnerabilities, and insider threats (Humayun et al. 2020, p. 3172).

This was the most clarifying learning experience in this topic. Until then, I had treated RPA and process cybersecurity as separate subjects. Seeing Agoda's bots autonomously triage alerts, classify phishing emails, and generate reports made me realise they are deeply connected — RPA is how organisations operationalise process cybersecurity in practice (Wlosinski 2023, p. 2). Creating the diagram tested that understanding concretely: mapping each threat to a bot response, then to a CIA Triad outcome, forced precision. A bot flagging anomalous staff behaviour is not just automating a task — it is protecting integrity. That distinction between automating for efficiency and automating for security will shape how I approach process design as a future BPM professional.


## References

Agoda Engineering 2025, *Improving security incident response at Agoda with large language models*, Medium, Agoda Engineering & Design, 20 August, viewed 15 May 2026, \<https://medium.com/agoda-engineering/improving-security-incident-response-at-agoda-with-large-language-models-78b1f33151e0\>.

CISA 2025, *What is cybersecurity?*, Cybersecurity and Infrastructure Security Agency, viewed 15 May 2026, \<https://www.cisa.gov/news-events/news/what-cybersecurity\>.

Humayun, M, Niazi, M, Jhanjhi, NZ, Alshayeb, M & Mahmood, S 2020, 'Cyber security threats and vulnerabilities: a systematic mapping study', *Arabian Journal for Science and Engineering*, vol. 45, no. 4, pp. 3171–3189.

Inmar Intelligence 2025, *What is RPA? | robotic process automation explained in 60 seconds*, YouTube, viewed 28 April 2026, \<https://www.youtube.com/watch?v=k_egKi8zREw\>.

Parker, S, Wu, Z & Christofides, PD 2023, 'Cybersecurity in process control, operations, and supply chain', *Computers & Chemical Engineering*, p. 14.

Wlosinski, LG 2023, 'Cybersecurity and robotic process automation', *ISACA Journal*, vol. 1, pp. 1–5.





