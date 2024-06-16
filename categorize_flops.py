import tomllib


class DecisionTree:
    pass


def read_toml_to_decision_tree(category_toml):
    """
    Parse a toml file wtih a flop-categories table into a decions tree

    Args:
        category_toml (str): file name for category.toml
    """
    with open(category_toml, "rb") as f:
        d = tomllib.load(f)
