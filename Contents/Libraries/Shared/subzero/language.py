# coding=utf-8
from babelfish.exceptions import LanguageError

from babelfish import Language as Language_


repl_map = {
    "dk": "da",
    "nld": "nl",
}


class Language(Language_):
    @classmethod
    def fromietf(cls, ietf):
        if ietf in repl_map:
            ietf = repl_map[ietf]

        return Language_.fromietf(ietf)

    @classmethod
    def fromalpha3b(cls, s):
        if s in repl_map:
            s = repl_map[s]
            return Language_.fromietf(s)

        return Language_.fromalpha3b(s)
