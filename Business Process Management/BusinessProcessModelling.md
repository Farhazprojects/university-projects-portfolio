# E Portfolio 2: Business Process Modelling

## Artefact 1 – YouTube Video: Business Process Modeling Lecture
[Watch: Business Process Modeling Lecture – January 2025](https://www.youtube.com/watch?v=wliGu7rjI7s)

This 2025 lecture-style YouTube video provides a structured introduction to Business Process Modeling (BPM), covering what process modeling is, why organisations use it, and how it fits within the broader BPM lifecycle. The video explains that business process modeling is the activity of representing an organisation's processes visually so that they can be analysed, communicated, and improved (Dumas et al., 2018, p. 11). It introduces key concepts such as process scope, stakeholders, and the distinction between as-is models — which capture current-state processes — and to-be models, which represent a desired future state after improvement.

I selected this artefact as my introductory resource because it provided me with the foundational context I needed before exploring specific modelling notations like BPMN. Before watching this video, I had a narrow view of process modeling as simply drawing flowcharts. This lecture shifted my understanding significantly — I came to appreciate that modeling is a deliberate analytical practice aimed at exposing inefficiencies and aligning stakeholders on how work is actually performed (Dumas et al., 2018, p. 9). This is meaningful evidence of my BPM learning because it represents the starting point of my engagement with the topic, helping me frame everything else I studied — notation, tools, and quality criteria — within the broader purpose of why process modeling matters in organisations.

---

## Artefact 2 – Scholarly Article: A Simulation-Driven Business Process Reengineering Framework for Teaching Assignment Optimization in Higher Education

[Read: Renna and Colonnese (2025) – Applied Sciences, Vol. 15, No. 5, Article 2756 (Fully open access — freely available online without a login or institutional subscription)](https://doi.org/10.3390/app15052756)

This peer-reviewed open-access article published in Applied Sciences presents a real-world application of Business Process Reengineering (BPR) using BPMN 2.0 at the University of Basilicata in Italy. The authors employ a dual-phase methodology: first, an AS-IS analysis that uses BPMN 2.0 diagrams to map existing administrative workflows, and second, a TO-BE redesign validated through discrete event simulation. The study demonstrates that applying process modelling and simulation together achieved a 35% reduction in end-to-end processing time and a 22% improvement in staff utilisation, directly illustrating the practical value of structured process modelling (Renna and Colonnese, 2025, p. 1).

I selected this artefact because it provided a concrete, real-world example of how business process modelling is applied to identify inefficiencies and drive meaningful organisational improvement. Before reading this article, I understood BPMN primarily as a diagramming notation. However, Renna and Colonnese (2025, p. 3) demonstrate that process modelling, when combined with simulation, becomes a powerful analytical tool that allows organisations to test redesigned processes before committing to implementation. This shifted my thinking significantly — I now appreciate that the value of a process model lies not in the diagram itself but in the analytical decisions it enables. This connects directly to the AS-IS and TO-BE modelling concepts discussed in our unit content, and reinforced my understanding that effective BPM practice requires modelling with a clear improvement purpose in mind.

---

## Artefact 3 – Website: Camunda BPM Platform – BPMN Modelling Guide

[Explore: Camunda BPMN Symbol Reference (2025)](https://camunda.com/bpmn/reference/)

The Camunda BPMN Symbol Reference Guide (2025) is an authoritative, practitioner-focused resource that documents every BPMN 2.0 element with interactive examples, use cases, and common modelling mistakes to avoid. Unlike static textbook descriptions, the guide allows users to hover over symbols and see live diagram examples, which makes learning notation significantly more intuitive. Camunda is one of the most widely adopted open-source BPM platforms globally, and its documentation reflects current industry standards for how BPMN models are built and executed in real systems (Camunda, 2025).

I selected this resource because it shifted my perspective on process modelling from an academic exercise to an operational discipline. A key insight I gained was understanding the distinction between a descriptive model — which captures how a process currently works — and an executable model — which can be deployed directly into a process engine to automate workflow (Dumas et al., 2018, p. 9). This distinction matters enormously in practice: a diagram missing a single gateway definition may look complete visually but fail entirely when executed. Engaging with Camunda's documentation made me far more attentive to modelling completeness and correctness, and it highlighted that BPM practitioners must think not only about how a process looks on paper, but how it will behave in a live system.

---

## Artefact 4 – Self-Created BPMN Swimlane Diagram Using MS Visio: Making Instant Noodles

[Click to view: MS Visio file](https://cqu365-my.sharepoint.com/:u:/g/personal/farhaz_khondoker_cqumail_com/IQDSNnKxM-iMR4JzTFt3TYmDAfI6gt4HLGK6bWt2wolD39M?e=0EImGZ)

![Instant Noodles Swimlane Diagram Screenshot](Images/Noodle.png)

To apply and consolidate my understanding of BPMN 2.0 notation, I created an original swimlane process diagram modelling the everyday task of making instant noodles. The diagram is structured across three swimlanes — Preparation, Cooking, and Serving — and incorporates key BPMN 2.0 elements including a start event, task boxes, XOR (exclusive) gateway, and an end event. The XOR gateway includes both a “Yes” path progressing the process forward and a “No” path routing back to the previous step, which accurately reflects real-world conditional logic in process flows.

Constructing this diagram was the most instructive learning experience across all four artefacts. I initially omitted the “No” paths on my gateways entirely — a fundamental modelling error, as an XOR gateway without a defined alternative path produces an incomplete and logically incorrect model. Correcting this forced me to think carefully about every decision point and its real-world consequence. I now understand that a process model must account for exceptions and loops, not just the ideal path. This artefact is meaningful evidence of my BPM development because it demonstrates that I can independently apply BPMN notation to construct a complete, correct process model — moving beyond theoretical knowledge into authentic, hands-on practice.

## References
- Andrew Miller 2025, Business process modeling lecture, YouTube, Available at: https://www.youtube.com/watch?v=wliGu7rjI7s, (Accessed: 22 April 2026)
- Camunda 2025, BPMN reference guide, Camunda Services GmbH, Available at: https://camunda.com/bpmn/reference/, (Accessed: 22 April 2026)
- Dumas, M, La Rosa, M, Mendling, J & Reijers, HA 2018, Fundamentals of business process management, 2nd edn, Springer, Heidelberg.
- Renna, P & Colonnese, C 2025, ‘A simulation-driven business process reengineering framework for teaching assignment optimization in higher education’, Applied Sciences, vol. 15, no. 5, article 2756, doi: 10.3390/app15052756, (Accessed: 23 April 2026)
