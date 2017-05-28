from unittest import TestCase
from pyssml.PySSML import PySSML


class TestPySSML(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.maxDiff = None

    def test_say(self):
        s = PySSML()
        s.say('star')
        self.assertEqual(s.ssml(), "<speak>star</speak>")

        s.clear()
        s.say("star's")
        self.assertEqual(s.ssml(), "<speak>stars</speak>")

        s.clear()
        s.say('star"s')
        self.assertEqual(s.ssml(), "<speak>stars</speak>")

        s.clear()
        s.say('hi')
        self.assertEqual(s.ssml(), "<speak>hi</speak>")

    def test_paragraph(self):
        s = PySSML()
        s.paragraph('hi')
        self.assertEqual(s.ssml(), "<speak><p>hi</p></speak>")

    def test_sentence(self):
        s = PySSML()
        s.sentence("<h'i>")
        self.assertEqual(s.ssml(), "<speak><s>hi</s></speak>")

    def test_pause(self):
        s = PySSML()
        s.pause('100ms')
        self.assertEqual(s.ssml(), "<speak><break time='100ms'/></speak>")

    def test_audio(self):
        s = PySSML()
        s.audio('https://www.audio.com/sound.mp3')
        self.assertEqual(s.ssml(), "<speak><audio src='https://www.audio.com/sound.mp3'/></speak>")

    def test_spell(self):
        s = PySSML()
        s.spell('nick')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='spell-out'>nick</say-as></speak>")

        s.clear()
        s.spell("<nick's>")
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='spell-out'>nicks</say-as></speak>")

    def test_spell_slowly(self):
        s = PySSML()
        s.spell_slowly('nick', "500ms")
        self.assertEqual(s.ssml(),
                         "<speak><say-as interpret-as='spell-out'>n</say-as> <break time='500ms'/> <say-as interpret-as='spell-out'>i</say-as> <break time='500ms'/> <say-as interpret-as='spell-out'>c</say-as> <break time='500ms'/> <say-as interpret-as='spell-out'>k</say-as> <break time='500ms'/></speak>")

        s.clear()
        s.spell_slowly("<nick's>", "500ms")
        self.assertEqual(s.ssml(),
                         "<speak><say-as interpret-as='spell-out'>n</say-as> <break time='500ms'/> <say-as interpret-as='spell-out'>i</say-as> <break time='500ms'/> <say-as interpret-as='spell-out'>c</say-as> <break time='500ms'/> <say-as interpret-as='spell-out'>k</say-as> <break time='500ms'/> <say-as interpret-as='spell-out'>s</say-as> <break time='500ms'/></speak>")

    def test_say_as(self):
        s = PySSML()
        s.say_as("five", "number")
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='number'>five</say-as></speak>")

        s.clear()
        s.say_as('1', 'ordinal')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='ordinal'>1</say-as></speak>")

        s.clear()
        s.say_as('123', 'digits')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='digits'>123</say-as></speak>")

        s.clear()
        s.say_as('2/9', 'fraction')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='fraction'>2/9</say-as></speak>")

        s.clear()
        s.say_as("3+1/2", 'fraction')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='fraction'>3+1/2</say-as></speak>")

        s.clear()
        s.say_as('2N', 'unit')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='unit'>2N</say-as></speak>")

        s.clear()
        s.say_as("+1-800-555-234 ex. 23", 'telephone')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='telephone'>+1-800-555-234 ex. 23</say-as></speak>")

        s.clear()
        s.say_as('*53#', 'telephone')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='telephone'>*53#</say-as></speak>")

        s.clear()
        self.assertRaises(ValueError, s.say_as,
                          **{'word': '+39(011)777-7777', 'interpret': 'telephone', 'interpret_format': '39'})

        s.clear()
        self.assertRaises(ValueError, s.say_as,
                          **{'word': '+1-800-EXAMPLE', 'interpret': 'telephone', 'interpret_format': '39'})

        s.clear()
        s.say_as('320 W Mt Willson Ct', 'address')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='address'>320 W Mt Willson Ct</say-as></speak>")

        s.clear()
        s.say_as('rm. 103', 'address')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='address'>rm. 103</say-as></speak>")

        s.clear()
        s.say_as('Ft Worth, TX 12345', 'address')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='address'>Ft Worth, TX 12345</say-as></speak>")

        s.clear()
        self.assertRaises(ValueError, s.say_as,
                          **{'word': 'CO', 'interpret': 'address', 'interpret_format': 'us-state'})

    def test_say_as_date(self):
        s = PySSML()
        s.say_as('20070102', 'date')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='date'>20070102</say-as></speak>")

        s.clear()
        s.say_as('????0102', 'date')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='date'>????0102</say-as></speak>")

        s.clear()
        s.say_as('01/02/2007', 'date', 'mdy')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='date' format='mdy'>01/02/2007</say-as></speak>")

        s.clear()
        s.say_as('01/02/2007', 'date', 'dmy')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='date' format='dmy'>01/02/2007</say-as></speak>")

        s.clear()
        s.say_as('2007/01/02', 'date', 'ymd')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='date' format='ymd'>2007/01/02</say-as></speak>")

        s.clear()
        s.say_as('01/02', 'date', 'md')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='date' format='md'>01/02</say-as></speak>")

        s.clear()
        s.say_as('01/02', 'date', 'dm')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='date' format='dm'>01/02</say-as></speak>")

        s.clear()
        s.say_as('2007/01', 'date', 'ym')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='date' format='ym'>2007/01</say-as></speak>")

        s.clear()
        s.say_as('01/2007', 'date', 'my')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='date' format='my'>01/2007</say-as></speak>")

        s.clear()
        s.say_as('1', 'date', 'd')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='date' format='d'>1</say-as></speak>")

        s.clear()
        s.say_as('2007', 'date', 'y')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='date' format='y'>2007</say-as></speak>")

    def test_say_as_time(self):
        s = PySSML()
        s.say_as("2'10\"", 'time')
        self.assertEqual(s.ssml(), "<speak><say-as interpret-as='time'>2'10\"</say-as></speak>")

        s.clear()
        self.assertRaises(ValueError, s.say_as,
                          **{'word': '19:21:30', 'interpret': 'time', 'interpret_format': 'hms24'})
        s.clear()
        self.assertRaises(ValueError, s.say_as,
                          **{'word': '09:21:15', 'interpret': 'time', 'interpret_format': 'hms12'})

    def test_parts_of_speech(self):
        s = PySSML()
        p = {
            "word": "read",
            "role": "ivona:VB"
        }
        s.parts_of_speech(**p)
        e = "<speak><w role='ivona:VB'>read</w></speak>"
        self.assertEqual(s.ssml(), e)

        p = {
            "word": "read",
            "role": "ivona:VBD"
        }
        s.clear()
        s.parts_of_speech(**p)
        e = "<speak><w role='ivona:VBD'>read</w></speak>"
        self.assertEqual(s.ssml(), e)

        p = {
            "word": "conduct",
            "role": "ivona:NN"
        }
        s.clear()
        s.parts_of_speech(**p)
        e = "<speak><w role='ivona:NN'>conduct</w></speak>"
        self.assertEqual(s.ssml(), e)

        p = {
            "word": "bass",
            "role": "ivona:SENSE_1"
        }
        s.clear()
        s.parts_of_speech(**p)
        e = "<speak><w role='ivona:SENSE_1'>bass</w></speak>"
        self.assertEqual(s.ssml(), e)

    def test_phoneme(self):
        s = PySSML()
        s.phoneme("pecan", "ipa", "pɪˈkɑːn")
        self.assertEqual(s.ssml(), "<speak><phoneme alphabet='ipa' ph='pɪˈkɑːn'>pecan</phoneme></speak>")

        s.clear()
        s.phoneme("pecan", "ipa", "pi.kæn")
        self.assertEqual(s.ssml(), "<speak><phoneme alphabet='ipa' ph='pi.kæn'>pecan</phoneme></speak>")

        # s.clear()
        # s.phoneme("pecan", "ipa", "pɪ'kɑːn")
        # self.assertEqual(s.ssml(), "<speak><phoneme alphabet='ipa' ph='pɪ&apos;kɑːn'>pecan</phoneme></speak>")

    def test_compound_examples(self):
        s = PySSML()
        s.say("Hello")
        s.paragraph("Nick")
        self.assertEqual(s.ssml(), "<speak>Hello <p>Nick</p></speak>")

        s.clear()
        s.say("How")
        s.paragraph("are")
        s.say("you")
        self.assertEqual(s.ssml(), "<speak>How <p>are</p> you</speak>")

    def test_to_object(self):
        s = PySSML()
        s.say("Hello")
        s.paragraph("Nick")
        self.assertEqual(s.to_object(), {"type": 'SSML', "speech": "<speak>Hello <p>Nick</p></speak>"})

    def test_input_validation(self):
        s = PySSML()

        self.assertRaises(TypeError, s.say, None)
        self.assertRaises(TypeError, s.say)

        self.assertRaises(TypeError, s.paragraph, None)
        self.assertRaises(TypeError, s.paragraph)

        self.assertRaises(TypeError, s.sentence, None)
        self.assertRaises(TypeError, s.sentence)

        self.assertRaises(TypeError, s.pause, None)
        self.assertRaises(TypeError, s.pause)
        self.assertRaises(ValueError, s.pause, '1sec')
        self.assertRaises(ValueError, s.pause, '11s')
        self.assertRaises(ValueError, s.pause, '-1s')
        self.assertRaises(ValueError, s.pause, '10001ms')

        self.assertRaises(TypeError, s.audio, None)
        self.assertRaises(TypeError, s.audio)
        self.assertRaises(ValueError, s.audio, 'bad')

        self.assertRaises(TypeError, s.spell, None)
        self.assertRaises(TypeError, s.spell)

        self.assertRaises(TypeError, s.spell_slowly, **{'text': None, 'duration': None})
        self.assertRaises(TypeError, s.spell_slowly)
        self.assertRaises(ValueError, s.spell_slowly, **{'text': 'bike', 'duration': '10001ms'})

        self.assertRaises(TypeError, s.say_as, **{'word': None, 'interpret': None, 'interpret_format': None})
        self.assertRaises(TypeError, s.say_as, **{'word': 'cup', 'interpret': None, 'interpret_format': None})
        self.assertRaises(ValueError, s.say_as, **{'word': 'cup', 'interpret': 'date', 'interpret_format': 'bad'})
        self.assertRaises(TypeError, s.say_as)

        self.assertRaises(TypeError, s.parts_of_speech, **{'word': None, 'role': None})
        self.assertRaises(TypeError, s.parts_of_speech, **{'word': 'cat', 'role': None})
        self.assertRaises(TypeError, s.parts_of_speech)

        self.assertRaises(TypeError, s.phoneme, **{'word': None, 'alphabet': None, 'ph': None})
        self.assertRaises(TypeError, s.phoneme, **{'word': 'cat', 'alphabet': None, 'ph': None})
        self.assertRaises(TypeError, s.phoneme, **{'word': 'cat', 'alphabet': 'ipa', 'ph': None})
        self.assertRaises(ValueError, s.phoneme, **{'word': 'cat', 'alphabet': 'bad', 'ph': 'p'})
        self.assertRaises(TypeError, s.phoneme)

    def test_ssml(self):
        s = PySSML()

        s.say('Hello')
        self.assertEqual(s.ssml(True), "Hello")
        self.assertEqual(s.ssml(False), "<speak>Hello</speak>")

        s.clear()
        s.say("<Cat's> & <Dog's>")
        self.assertEqual(s.ssml(False), "<speak>Cats and Dogs</speak>")

    def test_pause_by_strength(self):
        s = PySSML()

        s.pause_by_strength('weak')
        self.assertEqual(s.ssml(), "<speak><break strength='weak'/></speak>")

        s.clear()
        s.pause_by_strength(' STRONG')
        self.assertEqual(s.ssml(), "<speak><break strength='strong'/></speak>")

        s.clear()
        s.pause_by_strength('x-STrong ')
        self.assertEqual(s.ssml(), "<speak><break strength='x-strong'/></speak>")

        self.assertRaises(TypeError, s.pause_by_strength, None)
        self.assertRaises(TypeError, s.pause_by_strength)
        self.assertRaises(ValueError, s.pause_by_strength, 'bad')
        self.assertRaises(AttributeError, s.pause_by_strength, {})

    def test_emphasis(self):
        s = PySSML()
        s.emphasis('strong', 'helicopter')
        self.assertEqual(s.ssml(), "<speak><emphasis level='strong'>helicopter</emphasis></speak>")
        s.clear()
        s.emphasis(' MODERATE ', 'helicopter')
        self.assertEqual(s.ssml(), "<speak><emphasis level='moderate'>helicopter</emphasis></speak>")
        s.clear()
        s.emphasis('Reduced ', 'helicopter')
        self.assertEqual(s.ssml(), "<speak><emphasis level='reduced'>helicopter</emphasis></speak>")

        self.assertRaises(TypeError, s.emphasis, **{'level': None, 'word': None})
        self.assertRaises(TypeError, s.emphasis, **{'level': 'reduced', 'word': None})
        self.assertRaises(ValueError, s.emphasis, **{'level': 'bad', 'word': 'clown'})
        self.assertRaises(AttributeError, s.emphasis, **{'level': {}, 'word': 'clown'})

    def test_prosody(self):
        good_attributes = {'rate': 'slow', 'pitch': 'high', 'volume': 'loud'}
        bad_attribute = {'rate': 'slow', 'pitcher': 'high', 'volume': 'loud'}
        bad_attribute2 = {'rate': {}, 'pitch': 'high', 'volume': 'loud'}
        bad_value = {'rate': 'slow', 'pitch': 'Frank', 'volume': 'loud'}
        good_rate_percentage = {'rate': '  + 40 %'}
        bad_rate_percentage = {'rate': '  + 60 %'}
        bad_rate_percentage2 = {'rate': '  + thirty %'}

        s = PySSML()
        s.prosody(good_attributes, 'helicopter')
        result = "<speak><prosody rate='slow' pitch='high' volume='loud'>helicopter</prosody></speak>"
        self.assertEqual(len(s.ssml()), len(result))
        s.clear()
        s.prosody(good_rate_percentage, 'helicopter')
        result = "<speak><prosody rate='40%'>helicopter</prosody></speak>"
        self.assertEqual(len(s.ssml()), len(result))
        s.clear()

        self.assertRaises(TypeError, s.prosody, **{'attributes': None, 'word': None})
        self.assertRaises(KeyError, s.prosody, **{'attributes': bad_attribute, 'word': 'clown'})
        self.assertRaises(ValueError, s.prosody, **{'attributes': bad_value, 'word': 'clown'})
        self.assertRaises(ValueError, s.prosody, **{'attributes': bad_rate_percentage, 'word': 'clown'})
        self.assertRaises(ValueError, s.prosody, **{'attributes': bad_rate_percentage2, 'word': 'clown'})
        self.assertRaises(AttributeError, s.prosody, **{'attributes': bad_attribute2, 'word': 'clown'})

    def test_sub(self):
        s = PySSML()
        s.sub('dog', 'cat')
        self.assertEqual(s.ssml(), "<speak><sub alias='dog'>cat</sub></speak>")
        s.clear()

        self.assertRaises(TypeError, s.sub, **{'alias': 'cloud', 'word': None})
        self.assertRaises(TypeError, s.sub, **{'alias': None, 'word': 'rain'})
        self.assertRaises(ValueError, s.sub, **{'alias': 'robot', 'word': ''})
        self.assertRaises(ValueError, s.sub, **{'alias': '', 'word': 'wheel'})
        self.assertRaises(AttributeError, s.sub, **{'alias': 'ball', 'word': {}})
        self.assertRaises(AttributeError, s.sub, **{'alias': {}, 'word': 'stick'})
