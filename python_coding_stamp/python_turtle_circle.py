import turtle as t

t.shape('turtle')
t.circle(120)

n=60
t.shape('turtle')
t.speed('fastest')

for i in range(n):
    t.circle(120)
    t.right(360/n)
