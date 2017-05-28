""" AmazonSpeech is an add on for PySSML to support tags unique to Amazon

1. Create a AmazonSpeech(PySSML) object
    s = AmazonSpeech()

2. Add your speech text
    s.say('Hello')
    s.whisper('Brad')

3. Retrieve your SSML
    s.ssml()      # to retrieve ssml with <speak> wrapper
    s.ssml(True)  # to retrieve ssml without <speak> wrapper
    s.to_object() # to retrieve complete speach output object

"""
from pyssml.PySSML import PySSML


class AmazonSpeech(PySSML):

    def __init__(self):
        super().__init__()

    def whisper(self, words):
        if words is None:
            raise TypeError('Parameter words must not be None')
        try:
            words = words.strip()
            if len(words) == 0:
                raise ValueError('Parameter words must not be empty')
            self.ssml_list.append('<amazon:effect name="whispered">%s</amazon:effect>' % self._escape(words))
        except AttributeError:
            raise AttributeError('Parameters words must be strings')