# CE1-Framework  

## Overview  
CE1-Framework hosts documentation and tutorials for the CE1/CE123 family of languages. It aims to provide a unified framework for learning, prototyping, and experimenting with the CE series of languages.  

## Architecture  
The repository is organised into several sections:  
- `docs/` – contains tutorials, language references, and conceptual guides. Each language version (CE1, CE123, etc.) has its own subfolder.  
- `examples/` – includes runnable interpreter examples and sample code demonstrating core features of the CE languages.  
- `site/` – the static site for GitHub Pages, generated from the content in `docs/` and used to host the public documentation.  
- `tools/` – helper scripts for building the site, testing interpreter examples, and automating documentation generation.  
  
The aim is to keep code and content modular so that updates to one part do not break others. Tutorials live alongside code samples to make it easy for learners to navigate from description to runnable examples.  

## Licensing  
This project is licensed under the MIT License. See the `LICENSE` file in the repository for the full license text. By contributing to this repository you agree that your contributions will be licensed under the MIT License.  

## Contribution Guidelines  
We welcome contributions! To get started:  
1. Fork the repository and create a new branch for your changes.  
2. If you are contributing documentation, place markdown files under the appropriate folder in `docs/` and ensure they follow the existing style and structure.  
3. For code examples or interpreter improvements, add files under `examples/` or `tools/` as appropriate. Include clear comments and documentation.  
4. Before submitting a pull request, run any tests or build scripts to ensure your changes do not break the build.  
5. Open a pull request with a clear description of your changes.  
  
Please also review the Contributor Guide (to be added in `CONTRIBUTING.md`) for more detailed information about our workflow, coding standards, and code of conduct.  

## Getting Started  
An initial tutorial for the CE1 language can be found in `docs/CE1/01_intro.md`. To run the sample CE1 interpreter, see `examples/ce1_interpreter.py`. Both are included as a starting point and will evolve as the project grows.  

---  

Happy coding!
