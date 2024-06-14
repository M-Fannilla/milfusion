import pandas as pd
from pathlib import Path
from utils import SRC_DIR


def is_cropped(row):
    file_path = Path(row.file_path)
    cropped_file_path = (
            SRC_DIR
            / file_path.parent
            / 'cropped'
            / file_path.name
    )
    if cropped_file_path.exists():
        return True
    else:
        return False


def replace_file_path(row):
    file_path = Path(row.file_path)
    return (
            file_path.parent
            / 'cropped'
            / file_path.name
    ).as_posix()


if __name__ == "__main__":
    for dataset_path in [
        'ai_gen',
        'small_one_hot',
        'all_one_hot',
    ]:
        df = pd.read_csv(f'datasets/{dataset_path}.csv', index_col=0)
        start = df.shape[0]
        df['is_cropped'] = df.apply(is_cropped, axis=1)
        df = df[df['is_cropped']]
        df['file_path'] = df.apply(replace_file_path, axis=1)
        df.drop(['is_cropped'], axis=1, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv(f"datasets/cropped_{dataset_path}.csv")
        print(dataset_path, "reduced by", abs(df.shape[0] - start))
