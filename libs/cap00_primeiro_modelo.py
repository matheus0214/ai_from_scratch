xs = [1.0, 2.0, 3.0, 4.0]
ys = [3.0, 6.0, 9.0, 12.0]

w = 0.0
taxa = 0.01

for epoca in range(100):
    soma_erro = 0.0
    soma_ajuste = 0.0

    for x, y in zip(xs, ys):
        chute = w * x
        diferenca = chute - y
        soma_erro += diferenca ** 2
        soma_ajuste += 2 * diferenca * x

    erro = soma_erro / len(xs)
    ajuste = soma_ajuste / len(xs)

    w = w - taxa * ajuste
    if epoca % 10 == 0:
        print(f"epoca {epoca:3d} | w = {w:.4f} | erro = {erro:.4f}")

print(f"w final = {w:.4f}")
assert abs(w - 3.0) < 0.01, "w ainda esta longe de 3; revise o ajuste"
print("OK: seu primeiro modelo aprendeu")