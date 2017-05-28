from unittest import TestCase

from pyssml.AmazonSpeech import AmazonSpeech

class TestPySSML(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maxDiff = None

    def test_pyssml(self):
        pass

    def test_whisper(self):
        s = AmazonSpeech()

        s.whisper('dog cat')
        self.assertEqual(s.ssml(), '<speak><amazon:effect name="whispered">dog cat</amazon:effect></speak>')
        s.clear()

        self.assertRaises(TypeError, s.whisper, **{'words': None})
        self.assertRaises(ValueError, s.whisper, **{'words': ''})
        self.assertRaises(AttributeError, s.whisper, **{'words': {}})

    def test_sub(self):
        s = AmazonSpeech()
        s.sub('dog', 'cat')
        self.assertEqual(s.ssml(), "<speak><sub alias='dog'>cat</sub></speak>")
        s.clear()

        self.assertRaises(TypeError, s.sub, **{'alias': 'cloud', 'word': None})
        self.assertRaises(TypeError, s.sub, **{'alias': None, 'word': 'rain'})
        self.assertRaises(ValueError, s.sub, **{'alias': 'robot', 'word': ''})
        self.assertRaises(ValueError, s.sub, **{'alias': '', 'word': 'wheel'})
        self.assertRaises(AttributeError, s.sub, **{'alias': 'ball', 'word': {}})
        self.assertRaises(AttributeError, s.sub, **{'alias': {}, 'word': 'stick'})