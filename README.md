# Tracing Bias for Fairer Content Based Misinformation Detection

![License](https://img.shields.io/badge/License-ISC-blue.svg) ![Python 3.9](https://badgen.net/pypi/python/black)

Developed with 💙 at [Expert.ai Research Lab](https://github.com/expertailab)

- License: ISC
- Paper: [ACM Digital Library](https://dl.acm.org/doi/10.1145/3701716.3717534)

## Content

This repository contains the code and resources for the paper [Tracing Bias for Fairer Content Based Misinformation Detection](https://dl.acm.org/doi/10.1145/3701716.3717534) accepted at [BeyondFacts 2025: 5th International Workshop on Computational Methods for Online Discourse Analysis](https://dl.acm.org/doi/10.1145/3701716.3717540) @ [TheWebConf 2025](https://dl.acm.org/doi/proceedings/10.1145/3696410). 

The work investigates bias tracing in AI systems for content-based misinformation detection. It introduces a hybrid approach that integrates semantic modeling (using boxology design patterns) with deep learning to identify and mitigate biases originating from input data. Using fine-tuned language models, the work evaluates fairness across demographic axes (e.g., gender, nationality) by applying bias detection and mitigation techniques.

The findings reveal that widely used datasets exhibit significant demographic biases. However, models trained on demographically transformed data demonstrate improved fairness. These results highlight the importance of curated, diverse datasets and systematic bias management strategies to achieve fairer content-based misinformation detection.


## Repository Structure
```
├── data/                # Datasets used in the project
├── heterogeneity/       # Code to study demographic distributions across demographic axes
├── models/              # Trained models (populated after training)
├── notebooks/           # Jupyter notebooks to run experiments
│   ├── analyse/         # Data statistics and fairness metrics
│   ├── evaluate/        # Evaluation along demographic axes
│   ├── process/         # Data processing, including perturbation
│   └── train/           # Train models across demographic axes
```


## Installation and Reproducibility

To run the experiments, first create a Conda environment with:

```
conda create -n ENV_NAME python=3.9
```

Next, activate the environment:

```
conda activate ENV_NAME
```

Then, install the required dependencies with:

```
pip install -r requirements.txt
```

Finally, open and execute the notebooks in the `notebooks` folder.


## How to cite

To cite this research please use the following:

```bibtex
@inproceedings{10.1145/3701716.3717534,
    author = {Russo, Mayra and Merenda, Flavio and Gomez-Perez, Jose Manuel and Vidal, Maria-Esther},
    title = {Tracing Bias for Fairer Content-Based Misinformation Detection},
    year = {2025},
    isbn = {9798400713316},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/3701716.3717534},
    doi = {10.1145/3701716.3717534},
    abstract = {Despite the benefits attributed to AI systems, their deployment across domains still present challenges to society. In the case of automated misinformation detection, research has uncovered that benefits derived from their application are unequally distributed amongst different stakeholders, calling to attention the need to audit these AI systems for biases and other sources of harm. We present a hybrid AI system designed to trace biases from input data, enriched with semantic descriptions. Using boxology design patterns, we illustrate the integration of a semantic model with an AI system to enable bias tracing. In our case study, we assess fine-tuned language models for content-based misinformation detection, and adapt existing bias detection and mitigation techniques to transform data based on demographic signifiers and measure model fairness. Our findings show evidence that, on average, the evaluated datasets demonstrate a stark gender and geographical biases. Further, we observe that models trained on demographically transformed data demonstrate higher fairness. These results underscore the importance of curated and diverse data and of managing biases plaguing language models at task level.},
    booktitle = {Companion Proceedings of the ACM on Web Conference 2025},
    pages = {2670–2679},
    numpages = {10},
    keywords = {automated misinformation detection, bias, model robustness, nlp},
    location = {Sydney NSW, Australia},
    series = {WWW '25}
}
```

## ![Expert.ai favicon](https://www.expert.ai/wp-content/uploads/2020/09/favicon-1.png) Expert.ai

At Expert.ai we turn language into data so humans can make better decisions. Take a look [here](https://expert.ai)!