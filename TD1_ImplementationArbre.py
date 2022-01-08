#Exercie 1 implémentation de l'arbre
class Tree:
    def __init__(self, lettre, parent):
        self.lettre = lettre
        self.enfant = None
        self.parent = parent

    def setEnfant(self, lettre):
        self.enfant = lettre

    def getLettre(self):
        return self.lettre

    def getEnfant(self):
        return self.enfant

    def getParent(self):
        return self.parent


if __name__ == '__main__':

    a = Tree("a", None)
    b = Tree("b", "a")
    c = Tree("c", "a")
    d = Tree("d", "a")
    e = Tree("e", "b")
    f = Tree("f", "b")
    g = Tree("g", "d")
    h = Tree("h", "d")
    i = Tree("i", "d")
    j = Tree("j", "e")
    k = Tree("k", "e")
    l = Tree("l", "e")
    m = Tree("m", "g")
    n = Tree("n", "i")
    o = Tree("o", "i")
    p = Tree("p", "m")

    a.setEnfant([b, c, d])
    b.setEnfant([e, f])
    d.setEnfant([g, h, i])
    e.setEnfant([j, k, l])
    g.setEnfant([m])
    m.setEnfant([p])
    i.setEnfant([n, o])
