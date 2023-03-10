![python automation framework](https://user-images.githubusercontent.com/52358947/218895277-a7dffc87-909b-4ae8-828d-59a26541d512.png)


Fixtures - define functions that we can pass and can be used only in test_ scenarios to verify processes or to pass configuration parameters usually its the fist steps of the testing cycle. or open a session or hold on processes like sql and requests

```
import pytest


@pytest.fixture
def fixture_func_hi():
    return 'hi'


@pytest.fixture
def fixture_func_bye():
    return 'bye'


def test_somthing(fixture_func_hi, fixture_func_bye):
    assert fixture_func_hi == 'hi', 'Was expected to get hi'
    assert fixture_func_bye == 'hello', 'Was expected to get bye'
```


# Environment setup:
# Local
- Download latest python version
- Download latest Pycharm version
- Configure project test runner to be pytest
- Download required packages (pip install)


# Create folders inside the project:
### functions:
- Imoprt packeges
- General functions
- General Classes
- BDD tagging
- parameters
- Dictionaries
- Lists
- Links
- Environments
- APIs
- SoapUI
- Requests
- APP scenarios

### tests:
- from functions import *
- test_ senario01()
- test_scenario02()

### YAML:
- Yaml-pipeline-file.yml , Create YAML pipeline and execute the jobs by steps via Azure devops
  setting up the branch the pool of the VM and the steps for execution downloading pythong then installing the packages then executing the scenarios with pytest
- Requirments.txt - list of all required packages and their versions to use in automation

- Execute scenarios locally and review all works

# Cloud
- Upload the code to github repo
- Create and configure Agent in Azure pools and the VM (windows, MAC, linux)
- Create the pipeline run and debug make sure all working
- Execute jobs and review the results in Azure pipelines logs or HTML report

### Extra:
- BDD add bdd folder and the bdd scenarios.sql file
- tag the functions with the BDD steps "Given When And Then And"

# Projects:
1) Python Automation framework - python + pytest + Azure pipelines integration
2) Python Mobile Automation framework - python + pytest + appium + Android emulator


