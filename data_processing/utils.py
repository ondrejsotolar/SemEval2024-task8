import pandas as pd


def oversample(df: pd.DataFrame, label_key: str, with_replacement: bool) -> pd.DataFrame:
    """Oversample the minority classes in a dataframe.
    @:param df: source dataframe
    @:param label_key: key of the column with labels
    @:param with_replacement: sample the minority with or withour replacement
    @:return new instance of a dataframe
    """
    max_size = df[label_key].value_counts().max()
    lst = [df]
    for class_idx, group in df.groupby(label_key):
        lst.append(group.sample(max_size - len(group), replace=with_replacement))
    return pd.concat(lst)