import re


class PySMML():
    INTERPRET_AS = ['characters', 'cardinal', 'number', 'ordinal', 'digits', 'fraction',
                    'unit', 'date', 'time', 'telephone', 'address']

    DATE_FORMAT = ['mdy', 'dmy', 'ymd', 'md', 'dm', 'ym', 'my', 'd', 'm', 'y']

    ROLE = ['ivona:VB', 'ivona:VBD', 'ivona:NN', 'ivona:SENSE_1']

    IPA_CONSONANTS = ['b', 'd', 'd͡ʒ', 'ð', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ŋ',
                      'p', 'ɹ', 's', 'ʃ', 't', 't͡ʃ', 'θ', 'v', 'w', 'z', 'ʒ']

    IPA_VOWELS = ['ə', 'ɚ', 'æ', 'aɪ', 'aʊ', 'ɑ', 'eɪ', 'ɝ', 'ɛ', 'i', 'ɪ', 'oʊ', 'ɔ', '',
                  'ɔɪ', 'u', 'ʊ', 'ʌ']

    X_SAMPA_CONSONANTS = ['b', 'd', 'dZ', 'D', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'N', 'p', 'r\\',
                          's', 'S', 't', 'tS', 'T', 'v', 'w', 'z', 'Z']

    X_SAMPA_VOWELS = ['@', '@`', '{', 'aI', 'aU', 'A', 'eI', '3`', 'E', 'i', 'I', 'oU', 'O', 'OI', 'U',
                      'U', 'V']

    IPA_SPECIAL = ['ˈ', 'ˌ', '.']

    X_SAMPA_SPECIAL = ['”', '%', '.']

    ALPHABETS = {
        'ipa': IPA_CONSONANTS + IPA_VOWELS + IPA_SPECIAL,
        'x-sampa': X_SAMPA_CONSONANTS + X_SAMPA_VOWELS + X_SAMPA_SPECIAL
    }

    def __init__(self):
        self.ssml_list = []

    def clear(self):
        self.ssml_list = []

    def _escape(self, text):
        return re.sub('&', ' and ', re.sub('[\<\>\"\']', '', str(text)))

    def speech_object(self):
        return {'type': 'SSML', 'speech': ' '.join(self.ssml_list)}

    def ssml(self, old_method=False):
        result = ' '.join(self.ssml_list)
        return result if old_method else '<speak>%s</speak>' % result

    def say(self, text):
        self.ssml_list.append('%s' % self._escape(text))

    def paragraph(self, text):
        self.ssml_list.append('<p>%s</p>' % self._escape(text))

    def sentence(self, text):
        self.ssml_list.append('<s>%s</s>' % self._escape(text))

    def pause(self, duration):
        self.ssml_list.append("<break time='%s'/>" % self._escape(duration))

    def audio(self, url):
        self.ssml_list.append("<audio src='%s'/>" % self._escape(url))

    def spell(self, text):
        self.ssml_list.append("<say-as interpret-as='spell-out'>%s</say-as>" % self._escape(text))

    def spell_slowly(self, text, duration):
        ssml = ''
        for c in self._escape(text):
            ssml += "<say-as interpret-as='spell-out'>%s</say-as> <break time='%s'/> " % (c, self._escape(duration))
        self.ssml_list.append(ssml.strip())

    def say_as(self, word, interpret, interpret_format=None):
        if interpret not in PySMML.INTERPRET_AS:
            raise ValueError('Unknown interpret as %s' % str(interpret))
        if interpret_format is not None and interpret_format not in PySMML.DATE_FORMAT:
            raise ValueError('Unknown date format %s' % str(interpret_format))
        if interpret_format is not None and interpret != 'date':
            raise ValueError('Date format %s not valid for interpret as %s' % (str(interpret_format), str(interpret)))
        format_ssml = '' if interpret_format is None else " format='%s'" % interpret_format
        self.ssml_list.append(
            "<say-as interpret-as='%s'%s>%s</say-as>" % (interpret, format_ssml, str(word)))

    def parts_of_speech(self, word, role):
        if role not in PySMML.ROLE:
            raise ValueError('Unknown role %s' % str(role))
        self.ssml_list.append("<w role='%s'>%s</w>" % (self._escape(role), self._escape(word)))

    def phoneme(self, word, alphabet, ph):
        if alphabet not in PySMML.ALPHABETS:
            raise ValueError('Unknown alphabet %s' % str(alphabet))
        # if ph not in PySMML.ALPHABETS[alphabet]:
        #     raise ValueError('Unknown ph %s in alphabet %s' % (str(ph), str(alphabet)))
        self.ssml_list.append(
            "<phoneme alphabet='%s' ph='%s'>%s</phoneme>" % (self._escape(alphabet), self._escape(ph), self._escape(word)))
