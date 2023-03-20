import matplotlib.pyplot as plt
import pandas as pd


def visualize_best_fits(df_train, df_ideal, lst):
    """
    Visualisierung der 4 best Fits. Es werden die Trainingsfunktionen und die dazugehörigen Idealfunktionen
    gegenübergestellt.
    :param df_train: Trainingsdatensatz
    :param df_ideal: Datensatz der idealen Funktionen
    :param lst: Liste der best Fits
    :return: NONE
    """
    fig, axs1 = plt.subplots(nrows=4, ncols=2, layout='tight')
    fig.suptitle('Trainingsdatensätze und dazugehörige ideale Funktion (Bedingung: LeastSquares)')

    ######

    ax1 = plt.subplot(421)
    ax1.plot(df_train.index, df_train[df_train.columns[0]], color='r', label='train: ' + df_train.columns[0])
    plt.legend()

    ax2 = plt.subplot(422)
    ax2.plot(df_ideal.index, df_ideal[lst[0]], color='g', label='ideal: ' + lst[0])
    plt.legend()

    ######

    ax3 = plt.subplot(423)
    ax3.plot(df_train.index, df_train[df_train.columns[1]], color='r', label='train: ' + df_train.columns[1])
    plt.legend()

    ax4 = plt.subplot(424)
    ax4.plot(df_ideal.index, df_ideal[lst[1]], color='g', label='ideal: ' + lst[1])
    plt.legend()

    ######

    ax5 = plt.subplot(425)
    ax5.plot(df_train.index, df_train[df_train.columns[2]], color='r', label='train: ' + df_train.columns[2])
    plt.legend()

    ax6 = plt.subplot(426)
    ax6.plot(df_ideal.index, df_ideal[lst[2]], color='g', label='ideal: ' + lst[2])
    plt.legend()

    ######

    ax7 = plt.subplot(427)
    ax7.plot(df_train.index, df_train[df_train.columns[3]], color='r', label='train: ' + df_train.columns[3])
    plt.legend()

    ax8 = plt.subplot(428)
    ax8.plot(df_ideal.index, df_ideal[lst[3]], color='g', label='ideal: ' + lst[3])
    plt.legend()

    # Full screen
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()

    plt.show()


def visualize_results(outliers, fits, df_ideal, lst):
    """
    Visualisierung der 4 idealen Funktionen, der Fits (Abweichung < sqrt(2)) und der Outliers (Abweichung > sqrt(2))
    :param outliers: Dictionary der Outliers
    :param fits: Dictionary der Fits
    :param df_ideal: Ideale Funktionen
    :param lst: Liste der best Fits
    :return: NONE
    """
    fig, axs1 = plt.subplots(layout='tight')
    fig.suptitle('Die 4 Idealfunktionen, welche am besten zu dem Testdatensatz passen (+ Outliers)')

    # die 4 gefunden idealen Funktionen plotten
    plt.plot(df_ideal.index, df_ideal[lst[0]], label='ideal: ' + lst[0], color='#D95319')
    plt.plot(df_ideal.index, df_ideal[lst[1]], label='ideal: ' + lst[1], color='#0072BD')
    plt.plot(df_ideal.index, df_ideal[lst[2]], label='ideal: ' + lst[2], color='#77AC30')
    plt.plot(df_ideal.index, df_ideal[lst[3]], label='ideal: ' + lst[3], color='#EDB120')

    # die "fits" aus den Testdaten plotten
    df_test_fits = pd.DataFrame.from_dict(data=fits, orient='index', columns=['Y-Test'])
    df_test_fits.reset_index(inplace=True)
    plt.scatter(df_test_fits['Y-Test'], df_test_fits['index'], marker='x', color='g', label='Fits (Test)')

    # die outliers der Testdaten plotten
    df_test_outliers = pd.DataFrame.from_dict(data=outliers, orient='index', columns=['Y-Test'])
    df_test_outliers.reset_index(inplace=True)
    plt.scatter(df_test_outliers['Y-Test'], df_test_outliers['index'], marker='x', color='r', label='Outliers (Test)')

    # Full screen
    mng = plt.get_current_fig_manager()
    mng.window.showMaximized()

    plt.legend()
    plt.show()
