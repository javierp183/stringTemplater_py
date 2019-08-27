""" Output Templater """
from string import Template

#Dict with common common key and values.
words = {
    'var': 'mundo',
    'name': 'javier'
}

class Templater:
    def create(self,text,words):
        t = Template(text)
        return t.substitute(words)
    
    def save_text(self,text,filename):
        f = open(filename,"w")
        f.write(text)


a = Templater()

out = a.create("hola $var, mi nombre es $name",words)
a.save_text(out,"miarchivo.txt")
