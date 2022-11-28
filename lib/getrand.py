from random import choices

def result_generator(result):
    """Returns back random fruit"""

    results = ["Germany", "Brazil"]
    results.append(result)
    return choices(results)