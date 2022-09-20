n=input('enter a paragraph')
class reverse:
    def process(self, n):
        return ' '.join(reversed(n.split( )))
    n=n[::-1]
    n=n.split( )
    for i in n:
        if '#' in i:
            i.replace("#","e")
            print(i)
            


print(reverse().process(n))