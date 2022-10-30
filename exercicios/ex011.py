b = float(input('Largura da parede: '))
h = float(input('Altura da parede: '))
a = h * b
l = (a / 2)
print(f'Sua parede tem a dimensao de {b}x{h} e sua area e de {a:.3f}m².')
print(f'Para pintar essa parede, voce precisara de {l:.4f}l de tinta.')
