# PySSML

PySSML is an SSML generator for Amazon Alexa inspired by and based on https://github.com/mandnyc/ssml-builder.

A sample Alexa skill may be found here (todo).

## Installation

(todo)

```
pip install PySSML
```

## Usage

1. Create a PySSML object
    ```
    s = PySSML()
    ```
2. Add your speech text
    ```
    s.say('Hello')
    ```
3. Retrieve your SSML
    ```
    s.ssml()      # to retrieve ssml with <speak> wrapper
    s.ssml(True)  # to retrieve ssml without <speak> wrapper
    s.to_object() # to retrieve complete speach output object
    ```