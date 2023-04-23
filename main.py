from Population_growth import *
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # Verkrijg een grafiek van N(1) als functie van λ ∈ (0, 1]
    pop = population_growth(1)
    y, x = pop.calculate(0, 1, False, interval=0.01)

    plt.plot(x, y)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Population growth')
    plt.show()

    # b startwaarde = 0.21
    print(pop.Newton(0.21, 1264000))
