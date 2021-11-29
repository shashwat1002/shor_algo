
def list_to_latex(M, N, matrix_rep):
    # takes a list (and M and N)
    # assumes an M X N matrix and returns appropriate latex

    begin = r"\begin{bmatrix} "
    end = r"\end{bmatrix} "

    final_string = begin

    for i in range(N):
        for j in range(M-1):
            final_string += str(matrix_rep[i][j])
            final_string += " & "
        final_string += str(matrix_rep[i][M-1])
        if i != N-1:
            final_string += r" \\ "
    
    final_string += end
    return final_string
