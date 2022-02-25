bf, kf, jf, fv, bk, ba, jk, ja, kk, ka = [" ╔═", "═╦═", "═╗ ", " ║ ", " ╠═", " ╚═", "═╣ ", "═╝ ", "═╬═", "═╩═"]
vv, n, m = "═" * 3, 16, 16
print(
    "\n".join([
        (bf if i == 0 else bk) + vv + vv.join([(kf if i == 0 else kk) for _ in range(m - 1)]) + vv + (jf if i == 0 else jk) + "\n" +
        fv + fv.join([f"{hex((i + 1)*(j + 1))[2:]:>3s}" for j in range(m)]) + fv for i in range(0, n)  
    ]) + "\n" + ba + vv + vv.join([ka for _ in range(m - 1)]) + vv + ja
)
