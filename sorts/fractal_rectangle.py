import graphics as gr

window = gr.GraphWin("recursion", 600, 600)
ALPHA = 0.2

def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
#     gr.Line(gr.Point(*A), gr.Point(*B)).draw(window)
#     gr.Line(gr.Point(*B), gr.Point(*C)).draw(window)
#     gr.Line(gr.Point(*C), gr.Point(*D)).draw(window)
#     gr.Line(gr.Point(*D), gr.Point(*A)).draw(window)
    for M,N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0]*(1-ALPHA) + B[0]*ALPHA, A[1]*(1-ALPHA) + B[1]*ALPHA)
    B1 = (B[0]*(1-ALPHA) + C[0]*ALPHA, B[1]*(1-ALPHA) + C[1]*ALPHA)
    C1 = (C[0]*(1-ALPHA) + D[0]*ALPHA, C[1]*(1-ALPHA) + D[1]*ALPHA)
    D1 = (D[0]*(1-ALPHA) + A[0]*ALPHA, D[1]*(1-ALPHA) + A[1]*ALPHA)
    fractal_rectangle(A1, B1, C1, D1, deep-1)

fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500))
