# PySSML

PySSML is an SSML builder for Amazon Alexa inspired by and based on JavaScript project https://github.com/mandnyc/ssml-builder.

A sample Alexa skill may be found here https://github.com/sumsted/alexa_pyssml.

## Installation

```
pip install pyssml
```

## Usage

1. Create a PySSML object

    ```
    from pyssml.PySSML import PySSML

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
    s.to_object() # to retrieve complete speech output object
    ```