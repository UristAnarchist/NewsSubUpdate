from django import template

WORD_LIST = ('подсолнух',
             'подсолнуха',
             'подсолнуху',
             'подсолнухом',
             'подсолнухе',
             'подсолнухи',
             'подсолнухам',
             'подсолнухами',
             'подсолнухов',
             'подсолнухах'
)

register = template.Library()

class StrException(Exception):
    def __str__(self):
        return 'Принимается только текст'

@register.filter()
def censor(text):
    if not isinstance(text, str):
        raise StrException
    else:
        t = text.split(' ')
        for i, b in enumerate(t):
            if b.lower() in WORD_LIST:
                t[i] = b[0] + '*' * int(len(b) - 1)
        return " ".join(t)
