from nodal_analysis import VLP, IPR, solve, create_plot


def main():
    vlp = VLP(0.3, 2)
    ipr = IPR(2, 10)
    create_plot(vlp, ipr, range(10))
    print('Дебит', solve(vlp, ipr)[0])
    print('Давление', solve(vlp, ipr)[1])


if __name__ == '__main__':
    main()
