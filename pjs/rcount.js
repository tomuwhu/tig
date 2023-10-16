const f = (i = 1) => i > 10 ? 1 : (console.log(i), f(i + 1))
f()