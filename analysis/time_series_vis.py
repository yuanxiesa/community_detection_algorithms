import pandas as pd
import matplotlib.pyplot as plt

def main():

    lp = pd.read_csv('lp_p1_p2.csv')
    louvain = pd.read_csv('louvain_p1_p2.csv')
    gn = pd.read_csv('gn_p1_p2.csv')

    # drop the last row (2023, incomplete data)
    louvain = louvain.iloc[:-1]
    lp = lp.iloc[:-1]
    gn = gn.iloc[:-1]

    # figure 1 louvain and lp
    plt.figure(figsize=(8, 5))
    plt.rcParams['font.family'] = 'Georgia'
    plt.plot(louvain['year'], louvain['percent 1st gen'], label='Louvain P1', marker='o', color='blue', markersize=10,
             markerfacecolor='none')
    plt.plot(louvain['year'], louvain['percent 2nd gen'], label='Louvain P2', marker='+', color='blue', markersize=10)
    plt.plot(lp['year'], lp['percent 1st gen'], label='LP P1', marker='o', color='orange', markersize=10,
             markerfacecolor='none')
    plt.plot(lp['year'], lp['percent 2nd gen'], label='LP P2', marker='+', color='orange', markersize=10)
    plt.xlabel('Year', fontsize=14, labelpad=10)
    plt.ylabel('Percentage (%)', fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.savefig('louvain_and_lp.png', dpi=300)

    # figure 2 Girvan-Newman
    plt.figure(figsize=(8, 5))
    plt.rcParams['font.family'] = 'Georgia'
    plt.plot(gn['year'], gn['percent 1st gen'], label='Girvan-Newman P1', marker='o', color='green', markersize=10,
             markerfacecolor='none')
    plt.plot(gn['year'], gn['percent 2nd gen'], label='Girvan-Newman P2', marker='+', color='green', markersize=10)
    # plt.plot(lp['year'], lp['percent 1st gen'], label='LP P1', marker='o', color='orange', markersize=10, markerfacecolor='none')
    # plt.plot(lp['year'], lp['percent 2nd gen'], label='LP P2', marker='+', color='orange', markersize=10)
    plt.xlabel('Year', fontsize=14, labelpad=10)
    plt.ylabel('Percentage (%)', fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.ylim(0, 100)
    plt.xlim(2003, 2023)
    plt.xticks(ticks=[2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023],
               labels=[2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017, 2019, 2021, 2023],
               fontsize=14)
    plt.savefig('gn.png', dpi=300)

    plt.figure(figsize=(8, 5))
    plt.rcParams['font.family'] = 'Georgia'
    plt.plot(range(0, len(louvain)), louvain['percent 1st gen'], label='Louvain P1', marker='o', color='blue',
             markersize=10, markerfacecolor='none')
    plt.plot(range(0, len(louvain)), louvain['percent 2nd gen'], label='Louvain P2', marker='+', color='blue',
             markersize=10)
    plt.plot(range(1, len(lp) + 1), lp['percent 1st gen'], label='LP P1', marker='o', color='orange', markersize=10,
             markerfacecolor='none')
    plt.plot(range(1, len(lp) + 1), lp['percent 2nd gen'], label='LP P2', marker='+', color='orange', markersize=10)
    plt.plot(range(0, len(gn)), gn['percent 1st gen'], label='GN P1', marker='o', color='green', markersize=10,
             markerfacecolor='none')
    plt.plot(range(0, len(gn)), gn['percent 2nd gen'], label='GN P2', marker='+', color='green', markersize=10)
    plt.xlabel('Year Span from the Publication Year', fontsize=14, labelpad=10)
    plt.ylabel('Percentage (%)', fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.ylim(0, 100)
    plt.xlim(-1, 19)
    plt.xticks(ticks=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
               labels=[0, 2, 4, 6, 8, 10, 12, 14, 16, 18],
               fontsize=14)
    plt.savefig('all_shifted.png', dpi=300)

if __name__ == '__main__':
    main()