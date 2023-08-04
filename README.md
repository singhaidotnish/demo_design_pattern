<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/singhaidotnish/singhaidotnish/blob/animal_logic/README.md">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Demo Design Patterns</h3>
  <p align="center">
    Object-Oriented Design and Design Patterns Knowledge
    <br />
    <a href="https://refactoring.guru/design-patterns/why-learn-patterns"><strong>Why Learn Patterns »</strong></a>
    <br />
    <br />
    <a href="mailto:singhai.nish@gmail.com">Report Bug</a>
    ·
    <a href="mailto:singhai.nish@gmail.com">Request Feature</a>
  </p>

</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]]()

How to implement a design pattern to make a tool that has SOLID principles.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

This is a simple API allowing you to add new records, filter users. Display data in Json and Yaml. A CLI exists 
to add, display, convert and filter the whole data set. It is written so as to have an extendable system in future. No Validation
is included at this point as the focus is only on patterns.

This can be run from command line or installed as a module
#### 1. Download, from ... 
#### 2. Goto, to folder singhaidotnish
#### 3. Run, pip install -e


### Prerequisites

#### Additional Modules required.
json2html - To convert json to html format to display
pytest - Testing 

### Installation

- Create a python3.9 virtual environment and activate it
```sh
virtualenv .venv
.venv\Scripts\activate.bat
```
- cd into cloned repo and run
```sh
pip install -e .[dev]
```

1. Open new terminal
2. Activate virtual env
3. cd to package directory
4. pip install -e [dev] .


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Scalability - Show that file types can be extended. Where are the changes made ?

To make use of new file type follow these steps

1. Add new file type to class variable ALL_TYPES of class FileFactory
```
    ALL_TYPES = ['Json', 'Yaml']
```

2. Add class description as below. replace "yaml" with new file type. 
   and use its corresponding load and dump methods to read and write.
```
class Yaml(IFile):
    DEMO_YAML = 'demo.yaml'

    def __init__(self):
        super().__init__()
        self.name = 'Yaml'
        self.file = os.path.join(os.path.dirname(__file__), Yaml.DEMO_YAML)

    def read(self, read_from=None):
        _data = None
        try:
            if read_from:
                _data = json.dumps(read_from, indent=4)
                _data = json.loads(_data)
            else:
                with open(self.file, 'r') as yamlFile:
                    _data = yaml.safe_load(yamlFile) or []
        except yaml.YAMLError as e:
            raise Exception('Error Reading Yaml {e}')
        return _data

    def write(self, data):
        try:
            _tmp_data = self.read()
            _tmp_data['data'].append(data)
            with open(self.file, 'w') as stream:
                yaml.safe_dump(_tmp_data, stream, default_flow_style=False)
        except (IOError, ) as e:
            return False
        return _tmp_data
```


Commands:

Add -

```
python -m demo_design_pattern.cli --add --name FF --phone 9090909090 --address "a\\b building no X, floor X, landmark, city, state pincode" --filetype Yaml
```


image 

Display - 
```
python -m demo_design_pattern.cli --display --filetype Yaml
```

image 

Convert -
```
python -m demo_design_pattern.cli --convert --filetype Yaml --filetype_to Json
```


List all file types - 
```
python -m demo_design_pattern.cli --all_types
```


## Tests:

First go to tests folder 
Command : pytest -k add -v

[![Test Add][test-add]]()

Command : pytest -k convert -v

[![Test Convert][test-convert]]()

Command : pytest -k filter -v

[![Test Convert][test-filter]]()

Command : pytest -k display -v

[![Test Convert][test-display]]()

<!--_For more examples, please refer to the [Documentation](https://example.com)_-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CHALLENGES -->
## Challenges
1. Converting json to yaml is not working. It shows json format instead of yaml format on terminal
2. 

<!-- CONTACT -->
## Contact

Your Name - [@knishua](https://twitter.com/knishua) - singhai.nish@gmail.com

Project Link: [https://github.com/singhaidotnish/singhaidotnish](https://github.com/singhaidotnish/singhaidotnish)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [![Animal Logic Pipeline ][animal-logic]]() - I am grateful to the pipeline team at Animal Logic for giving this task.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/singhaidotnish/singhaidotnish.svg?style=for-the-badge
[contributors-url]: https://github.com/singhaidotnish/singhaidotnish/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/singhaidotnish/singhaidotnish.svg?style=for-the-badge
[forks-url]: https://github.com/singhaidotnish/singhaidotnish/network/members
[stars-shield]: https://img.shields.io/github/stars/singhaidotnish/singhaidotnish.svg?style=for-the-badge
[stars-url]: https://github.com/singhaidotnish/singhaidotnish/stargazers
[issues-shield]: https://img.shields.io/github/issues/singhaidotnish/singhaidotnish.svg?style=for-the-badge
[issues-url]: https://github.com/singhaidotnish/singhaidotnish/issues
[license-shield]: https://img.shields.io/github/license/singhaidotnish/singhaidotnish.svg?style=for-the-badge
[license-url]: https://github.com/singhaidotnish/singhaidotnish/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[test-add]: images/test_add.png
[test-convert]: images/test_convert.png
[test-display]: images/test_display.png
[test-filter]: images/test_filter.png
[animal-logic]: images/animal_logic.jpg