+++
title = "Pyjamas 2021: Using GitHub Actions for your Python projects"
outputs = ["Reveal"]
+++

# Using GitHub Actions for your Python projects
Harsh Mishra

{{< social >}}
{{< talk-link >}}

---

# $whoami

- {{< frag c="Software Developer at Quansight Labs" >}}
- {{< frag c="Google Summer of Code '21 Student at MetaCall" >}}
- {{< frag c="Google Season of Docs '21 Writer & Outreachy Mentor at moja global" >}}
- {{< frag c="Find me on: harshcasper.com" >}}

---

# Agenda

- {{< frag c="Understanding CI/CD" >}}
- {{< frag c="Introduction to GitHub Actions" >}}
- {{< frag c="Writing a simple workflow" >}}
- {{< frag c="Running GitHub Actions locally" >}}
- {{< frag c="Self hosted runners and marketplace" >}}
- {{< frag c="Q&A" >}}

---

# What is CI/CD?

CI/CD is an acronym for continuous integration/continuous deployment.
<br><br>
Through CI/CD you automate your:

- {{< frag c="Build process" >}}
- {{< frag c="Test process" >}}
- {{< frag c="Deployment process" >}}

---

# Why is CI/CD important?

- {{< frag c="Mitigates staging and production errors." >}}
- {{< frag c="Improves team productivity, code reviews and feedback loop." >}}
- {{< frag c="Deploy your code continuously and make immediate rollbacks." >}}
- {{< frag c="Plugin various CI toolings for code quality checks and more." >}}

---

# Popular CI/CD tools

- GitHub Actions
- Travis CI
- Circle CI
- AppVeyor
- Gitlab CI

In this talk, we will cover GitHub Actions.

---

# Introduction to GitHub Actions

- {{< frag c="Event-driven automation framework to trigger workflows" >}}
- {{< frag c="Native CI/CD offered by GitHub for building, testing and deployment." >}}
- {{< frag c="Offers free usage for open-source projects with a generous pricing for private projects." >}}
- {{< frag c="Brings forward a marketplace of custom actions to run on your CI/CD pipeline." >}}
---

# Example workflow

```yml
name: Python CI Workflow

on:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: 3.9
      - name: Upgrade pip version
      - run: |
          python3 -m pip install --upgrade pip
      - name: Installs all the Dependencies
        run: |
          python3 setup.py install
      - name: Checks the Application Build
        run: |
          pip3 install wheel
          python3 setup.py sdist bdist_wheel
      - name: Tests the Application
        run: |
          pip3 install -r tests/test-requirements.txt
          nosetests --with-coverage --cover-package=webedge tests.unit
```

---

# Why use GitHub Actions?

- {{< frag c="Capitalize on a wide number of operating systems and architecture." >}}
- {{< frag c="Plugin-based architecture to utilize wide number of third-party actions." >}}
- {{< frag c="Ease of development and customizable development and deployment." >}}
- {{< frag c="Create your own action for specific use-cases, local emulation or host your own runners!" >}}

---

# Writing a simple workflow

We will write a simple workflow to install, run and test a Flask application on GitHub Actions. Through GitHub Actions, we will:

- {{< frag c="Setup Python on a GitHub runner." >}}
- {{< frag c="Install the project along with all the dependenices." >}}
- {{< frag c="Run the tests." >}}
- {{< frag c="Lint the code using Flake8." >}}
- {{< frag c="Build the Docs." >}}

---

# Running GitHub Actions locally

You can run GitHub Actions locally using the `act`, a tool by Nektos to emulate local runs using Docker.

{{< figure src="images/scipy-github-actions-act-usage.png" height="400px" >}}
> Building SciPy on GitHub Actions using `act`

---

# Self hosted runners

- {{< frag c="Self hosted runners offer more control of hardware, operating system, and software tools" >}}
- {{< frag c="Self hosted runners can be integrated with toolings already offered by your cloud providers." >}}
- {{< frag c="Self hosted runners are free to use with GitHub Actions with only payable cost against the server use." >}}
- {{< frag c="Example of a managed self-hosted runner for GitHub Actions: cirun.io" >}}

---

# GitHub Actions Marketplace

{{< figure src="images/github-marketplace.png" height="400px" >}}

> Marketplace today hosts over 10,000+ GitHub Actions.

---

# Q&A

## Any questions?

---

# Thanks!

Harsh Bardhan Mishra
{{< social >}}
{{< talk-link >}}
