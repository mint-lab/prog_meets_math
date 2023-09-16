def mean_var(data):
    n = len(data)
    if n > 0:
        mean = sum(data) / n
        sum2 = sum([datum**2 for datum in data])
        var = sum2 / n - mean**2
        return mean, var
    return None, None

if __name__ == '__main__':
    data = [3, 2, 9, 1, 0, 8, 7, 5 ]
    mean, var = mean_var(data)
    print(f'mean = {mean:.3f}, var = {var:.3f}')