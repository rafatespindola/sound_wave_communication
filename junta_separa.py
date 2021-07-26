import matplotlib.pyplot as plt
import numpy as np
import soundfile


def find_freq(freqs, noise):
    mask = freqs < noise # ve quais valores sao maiores que o ruido
    freqs[mask] = 0 # o que for maior que o ruido passa e o que for menor fica igual a zero
    f = [] # todas frequencias
    f_aux = [] # pedacos
    res = [] # resultado

    # acha os indices diferentes de 0, ou seja, acha as frequencias
    for i in range(len(freqs)):
        if freqs[i] != 0:
            f_aux.append(i+1)
        elif len(f_aux) > 0:
            f.append(f_aux)
            f_aux = []

    for x in f:
        if len(x) == 1:
            res.append(x[0])
        else:
            res.append(x[round(len(x)/2)])

    return res


if __name__ == '__main__':

    n = 40000 # numero de pontos no grafico
    tx = 40000 # tamanho do eixo X
    fs = 1/tx
    w = 2.0 * np.pi * fs # frequencia angular

    t = np.linspace(0, tx, n) # valor inicial, valor final, tamanho do vetor ou lista
    s1 = 5.0 * np.cos(1000.0*w*t)
    s2 = 5.0 * np.cos(5000.0*w*t)
    s3 = 5.0 * np.cos(3500.0*w*t)
    s = s1 + s2 + s3

    print()

    freq = np.fft.fftfreq(n) # retorna valores negativos e positivos
    mascara = freq > 0  # retorna um vetor com true e false

    fft_calculo = np.fft.fft(s)
    fft_abs = 2.0 * np.abs(fft_calculo/n)

    plt.figure(1)
    plt.title('No tempo')
    plt.plot(t, s)

    # plt.figure(2)
    # plt.title('Na frequência')
    # plt.stem(freq[mascara]*n, fft_abs[mascara])
    # #plt.xlim(0, 20)
    plt.show()

    frequencias = find_freq(fft_abs[mascara], 0.5)

    print("Frequências encontradas: ")

    for i in frequencias:
        print(i)
